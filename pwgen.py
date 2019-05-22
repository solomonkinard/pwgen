#!/usr/bin/python3

import string
import random
import argparse


lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = "`~!@#$%^&*()_+-=[]\\;',./{}|:\"<>?"


parser = argparse.ArgumentParser()
parser.add_argument(
	"--special",
	"-s",
	help="special characters",
	action="store_true"
)
parser.add_argument(
	"--num",
	"-n",
	type=int,
	help="special characters",
	default=20
)
args = parser.parse_args()

types = [lower, upper, digits]
if args.special:
	types.append(special)
for _ in range(args.num):
	print("{}".format(random.choice(random.choice(types))), end='')
print()
