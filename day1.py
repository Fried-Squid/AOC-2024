def get_runners():
	return [part1, part2]

def preprocess(data_filename):
	with open(data_filename) as f:
		data = f.read().strip()
	data = [x.split() for x in data.split('\n')]
	data = [list(map(int, x)) for x in list(zip(*data)) ]
	return data

def part1(data_filename):
	with open(data_filename) as f:
		data = f.read().strip()
	data = preprocess(data_filename)
	data = [sorted(x) for x in data]
	data = [abs(x[0] - x[1]) for x in list(zip(*data)) ]
	return sum(data)

def part2(data_filename):
	with open(data_filename) as f:
		data = f.read().strip()
	data = preprocess(data_filename)
	return sum([x * data[1].count(x) for x in data[0]])
