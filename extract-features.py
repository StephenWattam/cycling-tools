#!/bin/env python3
'''Read a directory full of GPX files and output a CSV containing a series of per-ride metrics on each.'''

import sys, os
import gpxpy
import imp
import csv
import itertools

FEATURE_DIR = './features'


# find extractors
def load_from_file(filepath):
    class_inst = None
    expected_class = os.path.splitext(os.path.basename(filepath))[0]

    mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

    if file_ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, filepath)

    elif file_ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, filepath)

    klass = None
    if hasattr(py_mod, expected_class):
        klass = getattr(py_mod, expected_class)

    return klass

def gpx_to_rows(gpx, features, feature_order):

    rows = []
    for track in gpx.tracks:
        
        row = []
        for key in feature_order:

            fx = features[key](gpx, track)
            
            # Retrieve 1+ values and add to list
            values = fx.get()

            if not isinstance(values, list):
                values = [values]
            for v in values:
                row.append(v)

            # Explicitly tidy up object
            del(fx)

        rows.append(row)

    return rows



# =======================================================================================
# Entry point
#
dirname = sys.argv[1]
csvname = sys.argv[2]


# Load Features them
print("Looking for features in %s..." % FEATURE_DIR)
features = {}
for fn in os.listdir(FEATURE_DIR):
    fn = os.path.join(FEATURE_DIR, fn)
    if os.path.isfile(fn):

        # Dynamically load class
        kls = load_from_file(fn)
        if kls is not None:
            features[kls.__name__] = kls

# Extract feature keys, sort by name, then
# get their stated names and flatten list
feature_order = sorted(list(features.keys()))
feature_headers = [features[f].names() for f in feature_order]
feature_headers = sum([x if isinstance(x, list) else [x] for x in feature_headers], [])
print("Found %i features" % len(features))



# For every track, instantiate the features
with open(csvname, 'w') as io:
    cout = csv.writer(io)

    # Header line
    cout.writerow(['filename'] + feature_headers)

    # Find files and process
    for fn in os.listdir(dirname):
        fn = os.path.join(dirname, fn)
        if os.path.isfile(fn):
            print(" - %s" % fn)
            with open(fn, 'r') as io:

                # Parse, FX and write
                gpx = gpxpy.parse(io)
                for r in gpx_to_rows(gpx, features, feature_order):
                    cout.writerow([fn] + r)

