## Using Dictionary

# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels, 0)

# count the vowels
for char in ip_str:
	if char in count:
		count[char] += 1

print(count)

## Using a list and a dictionary comprehension

# Using dictionary and list comprehension

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# count the vowels
count = {x: sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)
