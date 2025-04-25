# layer 2 - now allow [] {} as valid parenthesis pairs

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


# pull test cases into test sets
validStrings = [
	"alskjedhqwkejh",
	"kajs kqjwhe() kajs",
	"(((((())))))",
	""
	# add this one
	"([{}])"

]
invalidStrings = [
	"(((((())",
	"aksj )( jask",
	"1",
	"aqksjdhqkwjehqwkejhkA",
	"kjahqw&*"
	# add these two
	"([{"
	"([{]})"
]


# talk through: 
#	why is line 41 invalid

# push away:
#	adding two counters
#		it's not enough to track the proper nesting of more than one type
#		you need a stack to store the openers, so you know the last one to be opened

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


	# step through the string
	for i in str_input:

		# still need to check against valid set
		if i not in validChars:

			# short-circuit - any invalid is enough to False out the method
			return False

		# now check for nesting
		# swap eq test for dictionary test
		# values for opens
		if i in parens.values():
			c.append(i)

		# swap eq test for dictionary test
		# keys for closes
		elif i in parens.keys():
			# replace decrement with length test - if we pop an empty stack we'll throw
			# 	also possible to use the Exception on pop-empty to short-circuit, but 
			#	exception handling is a little out of scope for the time-compressed exercise
			if len(c) <= 0:
				return False

			# pop and compare
			opener = c.pop()
			if opener != parens[i]:
				return False

	# all the way through - every char must be valid to be True
	# also c need to be zero - every increment (opened) had to be decremented (closed)
	# replace counter with arrlen check
	return len(c) == 0



# execute all test cases
# more poorly - retype cases and run one by one
print "valid"
for i in validStrings:
	print (i, testValid(i))
print "invalid"
for i in invalidStrings:
	print (i, testValid(i))

