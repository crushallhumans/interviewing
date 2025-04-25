# layer 0 - write a method to validate that a string input contains only 'a-z', ' ' and '()', return Boolean

# valid
# "alskjedhqwkejh"
# "kajs kqjwhe() kajs"
# "(((((())))))"
# "(((((())"
# "aksj )( jask"
# ""

# invalid
# "1"
# "aqksjdhqkwjehqwkejhkA"
# "kjahqw&*"


# pull test cases into test sets
validStrings = [
	"alskjedhqwkejh",
	"kajs kqjwhe() kajs",
	"(((((())))))",
	"(((((())",
	"aksj )( jask",
	""
]
invalidStrings = [
	"1",
	"aqksjdhqkwjehqwkejhkA",
	"kjahqw&*"
]


# push away: 
#	recursion
#	regex


def testValid(str_input):
	# define valid set
	validChars = "abcdefghijklmnopqrstuvwxyz ()"

	# step through the string
	for i in str_input:

		# check against valid set
		if i not in validChars:

			# short-circuit - any invalid is enough to False out the method
			return False

	# all the way through - every char must be valid to be True
	return True



# execute all test cases
# more poorly - retype cases and run one by one
print "valid"
for i in validStrings:
	print (i, testValid(i))
print "invalid"
for i in invalidStrings:
	print (i, testValid(i))

