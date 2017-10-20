import os
import palindrome

# print dir(palindrome)		# debug
# print __file__		# debug
current_dir = os.getcwd()

# Settings
chars_to_ignore = [" ", ",", "?", "!", ".", ":", ";", "\"", "'", "&", "\n"]

# Main
print "Longest Sentence: " + palindrome.longestFromFile("Guidelines/input.txt")
found_palindromes = palindrome.inFile("Guidelines/input.txt", chars_to_ignore)

print "Palindromes: "
if (found_palindromes != None):
	print "    Found " + str(len(found_palindromes)) + " palindromes"
	# for the_sentence in found_palindromes:
	# 	print the_sentence
else:
	print "    None were found"

print "Longest Palindrome: " + palindrome.longest(found_palindromes)

# print "Full List:"
# for pd in found_palindromes:
# 	print pd