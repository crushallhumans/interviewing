# layer 4 - now draw ascii art indicating the improper char:
# "([{]})"
# ----^

# valid
# "alskjedhqwkejh"
# "kajs kqjwhe() kajs"
# "(((((())))))"
# ""
# "([{}])"

# invalid
# "(((((())"
# "aksj )( jask"
# "1"
# "aqksjdhqkwjehqwkejhkA"
# "kjahqw&*"
# "([{"
# "([{]})"



# talk through: 
#	changes necessary - no changes to the methd
#	this really pushes the migration of the test cases to a full test harness
#	more junior candidates might not really get the harnessing notion


# reformat test set
#	also add expected results!
testStrings = [
	["alskjedhqwkejh",True],
	["kajs kqjwhe() kajs",True],
	["(((((())))))",True],
	["",True],
	["([{}])",True],

	["(((((())",False],
	["aksj )( jask",False],
	["1",False],
	["aqksjdhqkwjehqwkejhkA",False],
	["kjahqw&*",False],
	["([{",False],
	["([{]})",False]
]

def testValid(str_input):
	# still need to define valid set
	#	silly gotcha here - need to add []{} chars to the valid set, useful for debugging mindset
	validChars = "abcdefghijklmnopqrstuvwxyz ()[]{}"

	# convert counter to stack
	c = []

	# create mapping of closes to opens
	#	opens to closes also works, but is harder in languages that don't have dict.values() calls
	#	more poorly: you can build a big ugly set of if/elses
	parens = {
		')' : '(',
		']' : '[',
		'}' : '{'
	}

	# add a counter
	d = 0

	# step through the string
	for i in str_input:

		# still need to check against valid set
		if i not in validChars:

			# short-circuit - any invalid is enough to False out the method
			# returning an array (current char, current index) instead of False
			return ([i, d])

		# now check for nesting
		# swap eq test for dictionary test
		# values for opens
		if i in parens.values():
			# we need to append the index and char, not just the char
			c.append([i ,d])

		# swap eq test for dictionary test
		# keys for closes
		elif i in parens.keys():
			# replace decrement with length test - if we pop an empty stack we'll throw
			# 	also possible to use the Exception on pop-empty to short-circuit, but 
			#	exception handling is a little out of scope for the time-compressed exercise
			if len(c) <= 0:
				# returning an array (current char, current index) instead of False
				return ([i, d])

			# pop and compare
			opener = c.pop()
			# need the first index of the popped value (now an array)
			if opener[0] != parens[i]:
				# returning an array (current char, current index) instead of False
				return ([i, d])

		#increment counter
		d += 1

	# all the way through - every char must be valid to be True
	# also c need to be zero - every increment (opened) had to be decremented (closed)
	# replace counter with arrlen check
	# if False, return last in stack
	if len(c) != 0:
		return c.pop()
	else:
		# what to return for True? ('', -1) works, as those are values you'll never see in a failure case
		return ['', -1]


# micro test harness
for i in testStrings:
	v = "T" if i[1] else "F"

	# print string and expected result
	print("%s %s" %(v, i[0]))

	# execute
	r = testValid(i[0])

	# did we get the proper result?
	if (
		((r[1] == -1) and (not i[1])) or
		((r[1] > -1) and (i[1]))
	):
		# if not, print error!
		print (r)
		print "WRONG VALIDATION"

	elif (r[1] > -1):
		# leader strip
		x = '--'

		# draw '-' as many times as returned by the method
		for j in range(0,r[1]):
			x += '-'

		# finally draw the caret
		x += '^'
		print x


