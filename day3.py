import re
def get_runners():
	return [part1, part2]

def preprocess(data_filename):
	with open(data_filename, 'r') as f:
		data = [x.strip("\n") for x in f.readlines()]

	return data

def part1(data_filename):
	data = preprocess(data_filename)
	regex = re.compile(r'(mul\(\d*\,\d*\))')
	total = 0
	for line in data:
		muls1 = regex.findall(line)
		muls2 = [x.replace("mul(", "").replace(")", "").split(",") for x in muls1]
		muls3 = [int(x)* int(y) for x, y in muls2]
		total += sum(muls3)
		# print(list(zip(muls1, muls2, muls3))) # you can do this?
	return total

def part2(data_filename):
	data = preprocess(data_filename)
	regex = re.compile(r"mul\(\d*,\d*\)|don't\(\)|do\(\)")
	total = 0
	data = "".join(data)
	instructions = regex.findall(data)
	flag = True
	for instruction in instructions:
		if "mul" in instruction and flag == True:
			x,y = instruction.replace("mul(", "").replace(")", "").split(",")
			total += int(x) * int(y)
		elif "'" in instruction:
			flag = False
		elif "do" in instruction:
			flag = True
	return total
	

print(part2("data/day3_test.txt"))
print(part2("data/day3_prod.txt"))
