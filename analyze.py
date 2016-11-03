import sys, operator

patterns = {}


with open(sys.argv[1]) as f:
	passwords = f.read().splitlines()

for password in passwords:
	pattern = ""
	for char in password:
		if char.islower():
			pattern += "?l"
		elif char.isupper():
			pattern += "?u"
		elif char.isdigit():
			pattern += "?d"
		else:
			pattern += "?s"
	try:
		patterns[pattern] += 100
	except KeyError:
		patterns[pattern] = 100


sorted_patterns = sorted(patterns.items(), key=operator.itemgetter(1), reverse=True)

total = len(passwords)
total *= 1.0

try:
	limit = sys.argv[2]
except IndexError:
	limit = 19

for i in range(0, int(limit)):
	print("{} ... freq: {}").format(sorted_patterns[i], sorted_patterns[i][1]/total)
	