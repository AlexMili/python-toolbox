import re

# Function to print data in pandas'/numpy's apply functions
def print_func(x):
	print(x)

# Apply regex patterns on a string
def apply_patterns(string,patterns):
	for pattern in patterns:
		string = pattern.sub("",string)

	return string

# Keys becomes values and vis versa in a dict
def invert_keys_values(mydict):
	return {v: k for k, v in mydict.items()}
