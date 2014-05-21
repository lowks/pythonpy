import sys
import argparse
import math
import pickle
import re
import os
import shutil
import glob
import random
import json
import itertools
import itertools as it

try:
    import numpy as np
except: 
    pass
try:
    import matplotlib.pyplot as plt
except: 
    pass

if os.getenv("PYSTARTUP"):
    pass

parser = argparse.ArgumentParser()
parser.add_argument('evaluation', nargs='?', default='None')
parser.add_argument('-c', '--cmd')
parser.add_argument('--ji' '--json_in',
    dest='json_input', action='store_const',
    const=True, default=False)
parser.add_argument('--jo' '--json_out',
    dest='json_output', action='store_const',
    const=True, default=False)
parser.add_argument('-x' '--line_by_line',
    dest='line_by_line', action='store_const',
    const=True, default=False,
    help='sum the integers (default: find the max)')
parser.add_argument('-sv' '--split_values', 
    dest='split_values',
    default=False,
    help='sum the integers (default: find the max)')
parser.add_argument('--sub' '--substitute', 
    dest='substitute',
    nargs=2,
    default=False,
    help='sum the integers (default: find the max)')
parser.add_argument('-l', '--list_of_stdin',
    dest='list_of_stdin', action='store_const',
    const=True, default=False)
parser.add_argument('-fx', '--filter',
    dest='filter_result', action='store_const',
    const=True, default=False)
parser.add_argument('--i', '--ignore_exceptions',
    dest='ignore_exceptions', action='store_const',
    const=True, default=False)

args = parser.parse_args()

if args.json_input:
    stdin = (json.loads(x.rstrip()) for x in sys.stdin)
else:
    stdin = (x.rstrip() for x in sys.stdin)

if args.evaluation:
    args.evaluation  = args.evaluation.replace("`","'")
if args.cmd:
    args.cmd  = args.cmd.replace("`","'")

if args.cmd:
    exec(args.cmd)

if args.line_by_line:
    if args.ignore_exceptions:
        def safe_eval(text, x):
            try:
                return eval(text)
            except:
                return None
        result = (safe_eval(args.evaluation, x) for x in stdin)
    else:
        result = (eval(args.evaluation) for x in stdin)
elif args.list_of_stdin:
    l = list(stdin)
    result = eval(args.evaluation)
elif args.filter_result:
    result = (x for x in stdin if eval(args.evaluation))
elif args.split_values:
    result = (eval(args.evaluation) for sv in (re.split(args.split_values, x) for x in stdin))
elif args.substitute:
    result = (re.sub(args.substitute[0], args.substitute[1], x) for x in stdin)
else:
    result = eval(args.evaluation)

if hasattr(result, '__iter__'):
    for x in result:
        if x is not None:
            if args.json_output:
                print json.dumps(x)
            else:
                print x
elif result is not None:
    if args.json_output:
        print json.dumps(result)
    else:
        print result
