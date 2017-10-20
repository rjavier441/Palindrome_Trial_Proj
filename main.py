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

print "Full List:"
for pd in found_palindromes:
	print pd

# Mock of the entire palindrome search process
# sentence_arr = palindrome.sentencesFromFile("Guidelines/input.txt")
# for some_str in sentence_arr:
# 	print ""
# 	print ""
# 	# some_str = "Amore, Roma."
# 	print "Is \"" + some_str + "\" a palindrome? Let's see..."
# 	some_formatted_string = palindrome.filterCharsIn("Amore, Roma.", chars_to_ignore)
# 	print "The formatted string is \"" + some_formatted_string + "\""
# 	is_palind = palindrome.palgorithm(some_formatted_string.lower())
# 	if (is_palind):
# 		print "\"" + some_str + "\" is a palindrome"
# 	else:
# 		print "\"" + some_str + "\" is not a palindrome"