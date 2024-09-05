a=["hgkhjh","fjgjhg","juhkh"]

print(a[0])

# Python3 code to convert a tuple
# into a string using a for loop


def convertTuple(tup):
		
	str = ''
	for item in tup:
		str = str + item
	return str


# Driver code
tuple = (1, '2', 'e', 'k', 's')
str = convertTuple(tuple)
print(str)
