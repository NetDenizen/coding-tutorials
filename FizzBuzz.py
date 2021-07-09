# This is a comment, purely for human beings to read.
# Text after a # will be ignored by the Python interpreter, until the next line.

# To run this script, enter 'python3 FizzBuzz.py'

# This is an import statement.
# 'from sys' specifies the module to import from, in this case 'sys'.
# 'import stdout'
#
# The 'sys' module is from the standard library, which is included with the Python interpreter.
# It is responsible in part for interfacing with the rest of your operating system.
# The stdout object represents where we will write output to.
from sys import stdout

# This is a function definition.
# We can call this later to print the appropriate message for each number.
# 'i' is a parameter to the function, and represents it.
def CheckFizzBuzz(i):
	# This is a conditional block, where we choose which message to print.
	# Note, Python uses space to specify 'scope'.
	# Tabs and spaces are both fine, as long as you don't mix them.
	# Otherwise the interpreter will produce an error.
	# Everything indented after the function definition, is part of that function.

	# Conditional blocks start with  an 'if' statement.
	# This is the only necessary part.

	# Let's break down this first statement.

	# First, we perform modulo division on our variable 'i'.
	# '%' is the modulo operator, and basically takes the remainder.
	# '==' (note the double equal signs) is a comparison operator.
	# We can tell that if the remainder of modulo 3 is 0, the number is divisible by 3.

	# The second expression is separated by an 'and', which requires both expressions evaluate to being true.
	# If the first expression does not evaluate to be true (i % 3 does not equal 0), then the second is not tested.
	# This is called 'short-circuiting'.
	if i % 3 == 0 and i % 5 == 0:
		stdout.write("FizzBuzz") # If the condition is true, we write FizzBuzz to the terminal.
	elif i % 3 == 0: # elif, or else if the last condition was false, we test this condition.
		stdout.write("Fizz")
	elif i % 5 == 0: # Ditto.
		stdout.write("Buzz")
	# Finally, we have an else statement.
	# It represents a final option taken if none of the other conditions are true.
	# 'pass' fills in the block, and does nothing.
	# We could completely leave this part 'else' out, but it's included for the sake of demonstration.
	else:
		pass

# Here we have a 'main' function.
# This actually isn't necessary, but I think it's a good stylistic choice.
# It becomes more relevant if you're making a library that can be imported like at the beginning of this script.
# Not really a huge deal here, though.
def main(): # No parameters, empty parentheses.
	# This is a for loop. Let's break it down.
	# These are commonly applied to a series, and process every item in it in a consistent manner.
	# i is a variable updated to represent each item. It can be an arbitrary name, though.
	# range is an iterable. It can be 'iterated' in a for loop using the 'in' directive.
	# For 1-100, We pass '1' as the start parameter, and '101' as the end parameter, since the final number is NOT included.
	for i in range(1, 101):
		# So, for each number, we:
		# Write the number to the display. Note, it has to be converted to a text string using 'str'.
		# Otherwise, we would get an error.
		# Write does not do the conversion for us.
		stdout.write( str(i) )
		# We just put some formatting.
		stdout.write(": ")
		# And then print the appropriate Fizz/Buzz/FizzBuzz
		CheckFizzBuzz(i)
		# Finally, we print a special character to move to the next line.
		# This is represented by '\n'.
		# The backslash is the 'escape' character used to specify other characters.
		# If you want to print a literal backslash, you would just do '\\'.
		# Note, '' and "" are also interchangeable for representing Python strings.
		# The only difference is that you can put the other character inside, without needing to escape it.
		stdout.write('\n')

# Finally, all code included directly in the body of the script is run immediately.
# __name__ is an internal variable, which specifies the current module of the Python script.
# So, if we run it directly, we're in __main__, and run the main function.
if __name__ == '__main__':
	main()
