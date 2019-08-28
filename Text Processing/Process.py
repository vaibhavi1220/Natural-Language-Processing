
import nltk
import sys
from pprint import pprint
from nltk import *
import fileinput
from nltk import word_tokenize
from collections import defaultdict
from nltk.corpus import brown
from collections import defaultdict
from nltk.text import Text
counts = defaultdict(int)
count = defaultdict(int)
wrds = defaultdict(int)


def process(sentence):
    for (w1,t1), (w2,t2) in nltk.bigrams(sentence):
        if (t1=='DT' and t2=='NN'): 
            counts[t2] += 1
            print(w1+'|'+t1, w2+'|'+t2) # [_print-words]

	        
    for (wo1,ta1), (wo2,to2) in nltk.bigrams(sentence):
        if (t1=='DT' and to2=='NNS'): 
            count[to2] += 1
            print(wo1,ta1, wo2, to2) # [_print-words]

def process3(sentence):    
    for (w1,t1), (w2,t2) in nltk.bigrams(sentence):
        if (w1=='the' and w2=='ground'): 
            wrds[w1] += 1
            print(w1, w2) # [_print-words]
    
def process4(sentence):
    for (w1,t1), (w2,t2) in nltk.bigrams(sentence):
        if (w1=='the' and w2=='ground'):
		print(sentence)

def hello():
	with open('inp.txt','rU') as input_file:
		for data in input_file.readlines():
		    str1 = ''.join(str(e) for e in data)
		    tokens = nltk.word_tokenize(str1)
		    tag = nltk.pos_tag(tokens)
 		process(tag)
		
		process3(tag)
		process4(tag)
		    
	
hello()

print(counts['NN'])     
print(' ')
print(count['NNS'])
print(' ')
print(wrds['the'])

