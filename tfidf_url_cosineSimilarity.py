from __future__ import division
from math import log
import nltk
import re
import pprint
from numpy import dot
from numpy.linalg import norm
from urllib import urlopen

doc_list = []

proxies = {'here goes your proxy :3128'}


url1 = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
raw1 = urlopen(url1, proxies=proxies).read()
text1 = nltk.clean_html(raw1)
tokens1 = nltk.word_tokenize(text1)

url2 = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
raw2 = urlopen(url1, proxies=proxies).read()
text2 = nltk.clean_html(raw2)
tokens2 = nltk.word_tokenize(text2)

def tf(word,doc):
    all_num = 0
    for key in doc:
        all_num = all_num + len(key.split())
    word_num = 0
    for key in doc:
        if (key == word):
            word_num = word_num + 1
    return word_num/all_num

def idf(word,doc_list):
    all_num=len(doc_list)
    word_count=0
    for doc in doc_list:
        if word in doc:
            word_count+=1
    return log(all_num/word_count)

def tfidf(word,doc,doc_list):
    score=tf(word,doc)*idf(word,doc_list)
    return score

def cosine_sim(list_final):
    print "vector 1: "
    print list_final[0]
    print "vector 2: "
    print list_final[1]
    dp = float(dot(list_final[0],list_final[1]))
    np = float((norm(list_final[0]))*(norm(list_final[1])))
    if(np == 0):
        np = 1
    print "Similarity: %s" % float(dp / np)


if __name__=='__main__':
    doc1 = tokens1
    doc2 = tokens2
    list_final = []
    doc_list=[doc1,doc2]
    i=1
    for doc in doc_list:
        list_sim = []
        for word in doc:
            score = tfidf(word,doc,doc_list)
            list_sim.append(score)
        list_final.append(list_sim)
        i+=1
    cosine_sim(list_final)

    
