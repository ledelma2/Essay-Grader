# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:43:33 2018

@author: Liam Edelman
"""

import nltk
import string

EssayFile = open("test.txt", "r")
essay = EssayFile.read()

indices = []
nopunc = ''.join(word for word in essay if word not in string.punctuation)

tokens = nltk.word_tokenize(nopunc)
  
print(len(tokens))