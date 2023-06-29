## Example 1: Using enumerate

my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
	print(index, val)

## Example 2: Start the indexing with non zero value

my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list, start=1):
	print(index, val)

## Example 3: Without using enumerate()

my_list = [21, 44, 35, 11]

for index in range(len(my_list)):
	value = my_list[index]
	print(index, value)
