from math import log

def tf(word,doc):
    all_num=sum([doc[key] for key in doc])
    return float(doc[word])/all_num

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

if __name__=='__main__':
    doc1={'mik1':28,'aa':16,'web':14,'be':2,'python':1}
    doc2={'mik2':21,'ab':11,'web':14,'chal':5}
    doc3={'mik3':126,'bc':116,'web':74,'lelo':12,'foot':1}
    doc4={'mik4':8,'cd':3,'arbit':2,'da':1,'fork':1}

    doc_list=[doc1,doc2,doc3,doc4]
    i=1
    for doc in doc_list:
        print '-'*20
        print 'doc%d' % i
        for word in doc:
            print '"%s":%f' % (word,tfidf(word,doc,doc_list))
        i+=1

