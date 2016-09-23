import re

# Function to print data in pandas'/numpy's apply functions
def print_func(x):
	print(x)

def apply_patterns(string,patterns):
	for pattern in patterns:
		string = pattern.sub("",string)

	return string