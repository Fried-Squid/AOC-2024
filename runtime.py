import datetime

# Get target day from current day of the month
date = datetime.datetime.now()
day = date.day

# Import the relevant module based on the day of the month - file nomenclature is dayN.py
module = __import__('day' + str(day))

# The module has a function called get_runners which returns a list of Callable objects for each part of the puzzle
runners = module.get_runners()

# First, run the functions for test data
for runner in runners:
    print("Test data:")
    print(runner("./data/day" + str(day) + "_test.txt"))

# Then, run the functions for the real data
for runner in runners:
    print("Real data:")
    print(runner("./data/day" + str(day) + "_prod.txt"))

# End of runtime.py
