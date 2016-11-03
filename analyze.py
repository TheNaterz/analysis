import sys

patterns = {}

with open(sys.argv[1]) as f:
	passwords = f.read().splitlines()

for password in passwords:
	value = []
	pattern = ""
	keyspace = 1
	for char in password:
		if char.islower():
			pattern += "?l"
			keyspace *= 26
		elif char.isupper():
			pattern += "?u"
			keyspace *= 26
		elif char.isdigit():
			pattern += "?d"
			keyspace *= 10
		else:
			pattern += "?s"
			keyspace *= 33
	try:
		patterns[pattern][0] += 1
	except KeyError:
		patterns[pattern] = [1, keyspace]

sorted_patterns = sorted(patterns.items(), key=lambda x:x[1][0], reverse=True)
maximum_pop = sorted_patterns[0][1][0]

lower_eff = 2500000000
upper_eff = lower_eff*3600

patterns_2 = {}

for p in patterns:
	value = []
	effort = (patterns[p][1] - lower_eff)*1.0
	if effort < 0:
		effort = 1
	elif effort > (upper_eff-lower_eff):
		effort = 0
	else:
		effort = effort / (upper_eff-lower_eff)

	cost = ((patterns[p][0]*1.0)/maximum_pop)*effort
	patterns_2[p] = [cost, patterns[p][0], patterns[p][1]]

sorted_patterns_2 = sorted(patterns_2.items(), key=lambda x:x[1], reverse=True)
for i in range(0,19):
	print("{}").format(sorted_patterns_2[i])
