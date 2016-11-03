import sys

patterns = {}

with open(sys.argv[1]) as f:
	passwords = f.read().splitlines()

for password in passwords:
	value = []
	pattern = ""
	weight = 1
	for char in password:
		if char.islower():
			pattern += "?l"
			weight *= 26
		elif char.isupper():
			pattern += "?u"
			weight *= 26
		elif char.isdigit():
			pattern += "?d"
			weight *= 10
		else:
			pattern += "?s"
			weight *= 33
	try:
		patterns[pattern][0] += 1
	except KeyError:
		patterns[pattern] = [1, weight]


sorted_patterns = sorted(patterns.items(), key=lambda x:x[1][1])

total = len(passwords)
total *= 1.0

try:
	limit = sys.argv[2]
except IndexError:
	limit = 19

for i in range(0, int(limit)):
	print("{} ... freq: {}").format(sorted_patterns[i], (sorted_patterns[i][1][0]/total)*100)
