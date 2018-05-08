# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:43:33 2018

@author: Liam Edelman and Corey Habel
"""

import nltk
#nltk.download('wordnet')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#ltk.download('treebank')
import re
import os
from bisect import bisect_left

from stanfordcorenlp import StanfordCoreNLP

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
files = os.listdir("../input/testing/essays/")

nlp = StanfordCoreNLP(r'resources\stanford-corenlp-full-2018-02-27')

# Loop through and score every file
for file in files:
				
    mistakes = 0
    essay = open("../input/testing/essays/" + file, "r").read()
    
    nopunc = ''.join(word for word in essay if word not in punc)
    tokens = re.split(" |\n|\t", nopunc)
    indices = []
    for i in range (0, len(tokens)):
        if len(tokens[i]) == 0:
            indices.insert(0, i)
    
    for i in range (0, len(indices)):
        del tokens[indices[i]]
    	
    ####################
    # Word length score
    ####################
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
    
    results.write(file + ";")
    results.write(str(length_score) + ";")


    #################
    # Spelling Score
    #################
    spell_score = 0
    
    for words in tokens:
         exists = binary_search(dictionary, words)
         array = len(nltk.corpus.wordnet.synsets(words))
         if exists == -1 and array < 1:
             mistakes = mistakes + 1
    
    percent_wrong = mistakes / word_count
    
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

    final_score = 2 * length_score - spell_score;

    score = ""

    if final_score > 6:
    	score = "high"
    else:
    	score = "low"


    ###################
   	# Sentence Parsing
   	###################
	
    sentences = nltk.sent_tokenize(essay)

    for sentence in sentences:
    	tokens = nlp.word_tokenize(sentence)
    	#print('Constituency Parsing:', nlp.parse(sentence))
   	
    results.write(str(spell_score) + ";")

    results.write("0;0;0;0;0;0;")

    results.write(score + '\n')


<<<<<<< HEAD
sentence = 'My dog with a broken leg I not want'
#print('Tokenize:', nlp.word_tokenize(sentence))
#print('Part of Speech:', nlp.pos_tag(sentence))
#print('Constituency Parsing:', nlp.parse(sentence))
=======
sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
#print('Tokenize:', nlp.word_tokenize(sentence))
#print('Part of Speech:', nlp.pos_tag(sentence))
tree = nlp.parse(sentence)
>>>>>>> 8a2b0bb5ba43f08ca394012cdcadc61669b6133a
#print('Dependency Parsing:', nlp.dependency_parse(sentence))
realtree = Tree.fromstring(tree)
print(realtree[0])

token_test = nlp.parse(sentence)

if 'FRAG' in token_test:
	print("frag")

nlp.close()




results.close()	
