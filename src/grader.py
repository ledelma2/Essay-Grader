# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:43:33 2018

@author: Liam Edelman and Corey Habel
"""

import nltk
import re
import os

EssayFile = open("test.txt", "r")
essay = EssayFile.read()

punc = "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"
nopunc = ''.join(word for word in essay if word not in punc)
tokens = re.split(" |\n|\t", nopunc)
indices = []
for i in range (0, len(tokens)):
    if len(tokens[i]) == 0:
        indices.insert(0, i)

for i in range (0, len(indices)):
    del tokens[indices[i]]

print(len(tokens))
  
mistakes = 0

for words in tokens:
    array = len(nltk.corpus.wordnet.synsets(words))
    if array < 1:
        print(words)
        mistakes = mistakes + 1


# -*- coding: utf-8 -*-

results = open("../output/results.txt", "w")

# Store every file in the input folder
files = os.listdir("../input/essays/")

for file in files:
	essay = open("../input/essays/" + file, "r").read()

	indices = []
	nopunc = ''.join(word for word in essay if word not in punc)
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