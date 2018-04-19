# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:43:33 2018

@author: Liam Edelman and Corey Habel
"""

import nltk
import re
import os
from bisect import bisect_left

punc = "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"

dictionary = open("../src/resources/dictionary.txt", "r")
dic = dictionary.read()
dictionary.close()
dictionary = re.split("\n", dic)
dictionary.append("the")
dictionary.append("of")
dictionary.append("to")
dictionary.append("my")
dictionary.append("for")
dictionary.append("if")
dictionary.append("If")
dictionary.append("You")
dictionary.append("When")
dictionary.append("We")
dictionary.sort()


# -*- coding: utf-8 -*-

def binary_search(a, x, lo=0, hi=None):
    hi = hi or len(a)
    pos = bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -1)

#Dictionary test
# =============================================================================
# test = open("test.txt", "r")
# essay = test.read()
# nopunc = ''.join(word for word in essay if word not in punc)
# tokens = re.split(" |\n|\t", nopunc)
# indices = []
# for i in range (0, len(tokens)):
#     if len(tokens[i]) == 0:
#         indices.insert(0, i)
# 
# for i in range (0, len(indices)):
#     del tokens[indices[i]]
#     
# print(len(tokens))
# 
# 
# mistakes = 0
# 
# for words in tokens:
#         exists = binary_search(dictionary, words)
#         array = len(nltk.corpus.wordnet.synsets(words))
#         if exists == -1 and array < 1:
#             print(words)
#             mistakes = mistakes + 1
# =============================================================================
        

results = open("../output/results.txt", "w")

# Store every file in the input folder
files = os.listdir("../input/essays/")

# Loop through and score every file
for file in files:
<<<<<<< HEAD
	essay = open("../input/essays/" + file, "r").read()

	# Tokenize every word
	indices = []
	nopunc = ''.join(word for word in essay if word not in string.punctuation)
	tokens = nltk.word_tokenize(nopunc)


	# Word length score
	length_score = 0
	word_count = len(tokens)

	if word_count < 150:
		length_score = 1

	elif word_count < 200:
		length_score = 2

	elif word_count < 250:
		length_score = 3

	elif word_count < 300:
		length_score = 4

	else:
		length_score = 5


	# Verb agreement score
	sentences = nltk.sent_tokenize(essay)

	for sentence in sentences:
		tokenized_sent = nltk.word_tokenize(sentence)
		pos_sent = nltk.pos_tag(tokenized_sent)

		mistakes = 0


		for tup in pos_sent:
			if 'NN' in tup:
				for tup in pos_sent:
					if "VBZ" or "VBD" or "VBG" not in tup:
						mistakes += 1
					elif "VBG" and 
				




	# Write results to file
	results.write(file + ";")
	results.write(str(length_score) + ";\n")


results.close()	
=======
    mistakes = 0
    essay = open("../input/essays/" + file, "r").read()
    
    nopunc = ''.join(word for word in essay if word not in punc)
    tokens = re.split(" |\n|\t", nopunc)
    indices = []
    for i in range (0, len(tokens)):
        if len(tokens[i]) == 0:
            indices.insert(0, i)
    
    for i in range (0, len(indices)):
        del tokens[indices[i]]
    	
    
    # Word length score
    length_score = 0
    word_count = len(tokens)
    
    if word_count  < 100:
        length_score = 0
    
    elif word_count < 150:
        length_score = 1
    
    elif word_count < 200:
        length_score = 2
    
    elif word_count < 250:
        length_score = 3
    
    elif word_count < 300:
        length_score = 4
    
    else:
        length_score = 5
    
    results.write(file + ";")
    results.write(str(length_score) + ";")

    spell_score = 0
    
    for words in tokens:
         exists = binary_search(dictionary, words)
         array = len(nltk.corpus.wordnet.synsets(words))
         if exists == -1 and array < 1:
             mistakes = mistakes + 1
    
    percent_wrong = mistakes / word_count
    print(percent_wrong)
    
    if percent_wrong > .12:
        spell_score = 0
    elif percent_wrong > .09:
        spell_score = 1
    elif percent_wrong > .06:
        spell_score = 2
    elif percent_wrong > .03:
        spell_score = 3
    else:
        spell_score = 4

    results.write(str(spell_score) + ";\n")



results.close()	
>>>>>>> 8b0dd1e427c5f08abce809e5645999e16707df20
