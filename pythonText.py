import random
import sys


#load the file to be read.
load_file = open("/usr/share/dict/words", "r")
read_it = load_file.read()

# 	print read_it 
x = raw_input("How many words would you like to be in your sentence? ")
sentence = ""

#if user input is a number then i equals that number else print error.
try:
   i = int(x)
except ValueError:
   print("That's not an number!") 

while i > 0:
	#generate random number between 0 and the last line of the file.
	random_number = random.randint(0,235886) 
	#split at the random number line.
	word = read_it.splitlines()[random_number]
	i -= 1
	#if last word no space else add space.
	if i == 0:
		sentence += str(word)
	else:
		sentence += str(word) + " "
#print sentence with first letter of first word capitalized and period at the end. 
print sentence.capitalize()+'.'

