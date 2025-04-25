# layer 1 - now validate that all parentheses in the string are properly balanced and nested

# valid
# "alskjedhqwkejh"
# "kajs kqjwhe() kajs"
# "(((((())))))"
# ""

# invalid
# "(((((())"
# "aksj )( jask"
# "1"
# "aqksjdhqkwjehqwkejhkA"
# "kjahqw&*"


# pull test cases into test sets
validStrings = [
	"alskjedhqwkejh",
	"kajs kqjwhe() kajs",
	"(((((())))))",
	# pull these two into invalid
	#"(((((())",
	#"aksj )( jask",
	""
]
invalidStrings = [
	"(((((())",
	"aksj )( jask",
	"1",
	"aqksjdhqkwjehqwkejhkA",
	"kjahqw&*"
]


# talk through: 
#	what is balanced
#	what is nested
#	how can you represent those facts while stepping through the string


def testValid(str_input):
	# still need to define valid set
	validChars = "abcdefghijklmnopqrstuvwxyz ()"

	# add a counter
	c = 0

	# step through the string
	for i in str_input:

		# still need to check against valid set
		if i not in validChars:

			# short-circuit - any invalid is enough to False out the method
			return False

		# now check for nesting
		# increment if open
		if i == '(':
			c += 1

		# decrement if closed
		elif i == ')':
			c -= 1
			# short-circuit: if we ever enter negative space, we've closed too many parens
			if c < 0:
				return False


	# all the way through - every char must be valid to be True
	# also c need to be zero - every increment (opened) had to be decremented (closed)
	return c == 0



# execute all test cases
# more poorly - retype cases and run one by one
print "valid"
for i in validStrings:
	print (i, testValid(i))
print "invalid"
for i in invalidStrings:
	print (i, testValid(i))

