# File: 	palindrome.py
# Name: 	Rolando Javier
# Created:	October 19, 2017
# Modified:	October 19, 2017
# Details:	This file contains methods useful for finding palindromes
# 
# Dependencies:
# 			re - Python regular expression library
# 			fileinput - Python file stream library

# Includes
import re
import fileinput

# Settings
DEBUG = False

# @function		debug
# @parameter	setting - boolean to determine debug mode
# @details 		This function simply changes the current DEBUG setting
# @returns		N/A
def debug (setting):
	option = "off"
	if (setting):
		option = "on"
	print "Turning Debug " + option
	DEBUG = setting
	return

# @function		doThing
# @parameter	string - a string definining the thing to do
# @details 		This function simply prints the thing you want it to do
# @returns		N/A
def doThing (string):
	some_arr = ["asd", "f"]
	print "So you want me to do \"" + string + "\"...?"
	return some_arr

# @function		sentences
# @parameter	string - a string containing at least one sentence (separated by periods/newlines)
# @details 		This function takes a string and returns an array of strings. Each string is a detected sentence.
# @returns		The array of detected sentences
def sentences (string):
	str_arr = [];	# empty array for our sentence matches
	length = len(string)
	position = 0
	cnt = 0
	while position < length:
		match = re.search(r'[\w| ,]*[\.!?]{1}', string[position:])
		grp = match.group()
		str_arr.append(grp)
		position += match.end()
		if (DEBUG):
			print position
		cnt = cnt + 1
	return str_arr

# @function		sentencesFromFile
# @parameter	fname - the name of the file to process
# @details 		This function takes a string and returns an array of strings. Each string is a detected sentence.
# @returns		The array of detected sentences
def sentencesFromFile (fname):
	str_arr = []
	for line in fileinput.input(fname):
		str_arr.append(line);
	return str_arr

# @function		longest
# @parameter	arr - the array of sentence strings to process
# @details 		This function returns the longest string found in arr
# @returns		The longest string within the array
def longest (arr):
	longest_len = 0
	longest_sentence = arr[0]
	for the_sentence in arr:
		if (len(the_sentence) > longest_len):
			longest_len = len(the_sentence)
			longest_sentence = the_sentence
	return longest_sentence

# @function		longestFromFile
# @parameter	fname - the name of the file to process
# @details 		This function finds the longest sentence in a file and returns it
# @returns		A string containing the longest sentence found in the file
def longestFromFile (fname):
	sentence_arr = sentencesFromFile(fname)
	longest_len = len(sentence_arr[0])
	longest_sentence = sentence_arr[0]
	for the_sentence in sentence_arr:
		if (len(the_sentence) > longest_len):
			longest_len = len(the_sentence)
			longest_sentence = the_sentence
	return longest_sentence

# @function		filterCharsIn
# @parameter	string - the string to process
# @parameter	blacklist - an array of characters to filter out
# @details 		This function takes an input string and removes any unwanted characters specified. If none are specified, no filtering is performed.
# @returns		A string with all blacklist characters filtered out. If blacklist was an empty array, the original string is returned
def filterCharsIn (string, blacklist):
	filtered_str = "";
	if (len(blacklist) != 0):
		for i in range(len(string)):
			char = string[i]
			regex_obj = re.compile("[" + "".join(blacklist) + "]")
			match = regex_obj.match(char)
			if (match == None):
				# print "Blacklist char not found at " + str(i) + "(" + string[i] + ")"	# Debug
				filtered_str += char
	else:
		filtered_str = string
	return filtered_str

# @function		palgorithm
# @parameter	string - the sentence string to process
# @details 		This function returns true if str is a palindrome, or false if otherwise
# @returns		True if string is a palindrome, or
# 				False otherwise
# @note			This function assumes that the string is FREE of conflicting letter case, punctuation characters and spaces/sentence terminators (i.e. no newlines, no commas, and no capitals)
def palgorithm (string):
	str_is_a_palindrome = True  # Innocent, til proven guilty XD
	str_is_even = True
	front_index = 0
	back_index = len(string) - 1
	end_condition = 1

	if (len(string) % 2 == 1):
		str_is_even = False;
	if (str_is_even):
		end_condition = 0
	while (back_index - front_index > end_condition):
		if (string[back_index] != string[front_index]):
			str_is_a_palindrome = False
			break
		back_index = back_index - 1
		front_index = front_index + 1
	# if (str_is_a_palindrome == False):
	# 	print string + " is not a palindrome"	# Debug
	return str_is_a_palindrome

# @function		inFile
# @parameter	fname - the name of the file to process
# @parameter	blacklist - an array of characters to ignore when looking for palindromes within the strings inside fname
# @details 		This function searches for palindromes within the specified file
# @returns		An array of strings that are palindromes
def inFile (fname, blacklist):
	palindrome_arr = []
	sentence_arr = sentencesFromFile(fname)
	for the_sentence in sentence_arr:
		formatted_str = filterCharsIn(the_sentence, blacklist)
		str_is_a_palindrome = palgorithm(formatted_str.lower())
		if (str_is_a_palindrome):
			# print the_sentence + " is a palindrome" + str(type(the_sentence))		# Debug
			palindrome_arr.append(the_sentence)
	return palindrome_arr
