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

for file in files:
	essay = open("../input/essays/" + file, "r").read()

	indices = []
	nopunc = ''.join(word for word in essay if word not in string.punctuation)
	tokens = nltk.word_tokenize(nopunc)
  
	

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
	results.write(str(length_score) + ";\n")







results.close()	
