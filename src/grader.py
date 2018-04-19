# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:43:33 2018

@author: Liam Edelman
"""

import nltk
import string
import os

results = open("../output/results.txt", "w")

# Store every file in the input folder
files = os.listdir("../input/essays/")

# Loop through and score every file
for file in files:
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
