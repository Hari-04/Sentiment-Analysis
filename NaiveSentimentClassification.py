# -*- coding: utf-8 -*-
from sklearn.model_selection import train_test_split
#from nltk.corpus import stopwords
import re
neg = open("/home/hari/Documents/NLP/HW3/hotelNegT-train.txt","r")
pos = open("/home/hari/Documents/NLP/HW3/hotelPosT-train.txt","r")

neg_review = []
pos_review = []
for i in neg:
    review = i.split("\t")
    neg_review.append(review[1])
for i in pos:
    review = i.split("\t")
    pos_review.append(review[1])

neg_train , neg_test = train_test_split(neg_review,test_size=0.2)
pos_train , pos_test = train_test_split(pos_review,test_size=0.2)

#calculating prior probabilities
prob_neg = len(neg_train) / float((len(neg_train) + len(pos_train)))
prob_pos = len(pos_train) / float((len(neg_train) + len(pos_train)))


print "Before",type(neg_train)

whole_word_dict = {}
'''
sample_test_case = "I am in USA. right now in boulder!!, wasn't aren't."
neg_train = []
neg_train.append(sample_test_case)
pos_train = []
pos_train.append(sample_test_case)

print "After",type(neg_train)
'''

def tokenize(s):
    cList = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'd've": "he would have",
        "he'll": "he will",
        "he'll've": "he will have",
        "he's": "he is",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "how's": "how is",
        "I'd": "I would",
        "I'd've": "I would have",
        "I'll": "I will",
        "I'll've": "I will have",
        "I'm": "I am",
        "I've": "I have",
        "isn't": "is not",
        "it'd": "it had",
        "it'd've": "it would have",
        "it'll": "it will",
        "it'll've": "it will have",
        "it's": "it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd": "she would",
        "she'd've": "she would have",
        "she'll": "she will",
        "she'll've": "she will have",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "so's": "so is",
        "that'd": "that would",
        "that'd've": "that would have",
        "that's": "that is",
        "there'd": "there had",
        "there'd've": "there would have",
        "there's": "there is",
        "they'd": "they would",
        "they'd've": "they would have",
        "they'll": "they will",
        "they'll've": "they will have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        "we'd": "we had",
        "we'd've": "we would have",
        "we'll": "we will",
        "we'll've": "we will have",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what'll've": "what will have",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "when's": "when is",
        "when've": "when have",
        "where'd": "where did",
        "where's": "where is",
        "where've": "where have",
        "who'll": "who will",
        "who'll've": "who will have",
        "who's": "who is",
        "who've": "who have",
        "why's": "why is",
        "why've": "why have",
        "will've": "will have",
        "won't": "will not",
        "won't've": "will not have",
        "would've": "would have",
        "wouldn't": "would not",
        "wouldn't've": "would not have",
        "y'all": "you all",
        "y'alls": "you alls",
        "y'all'd": "you all would",
        "y'all'd've": "you all would have",
        "y'all're": "you all are",
        "y'all've": "you all have",
        "you'd": "you had",
        "you'd've": "you would have",
        "you'll": "you you will",
        "you'll've": "you you will have",
        "you're": "you are",
        "you've": "you have"
    }
    sList = ["I","i","a","an","am","and","as","at","be","by","for","from","has","he","in","is","it","its","of","on","that","the","to","was","were","will","with"]
    #words = s.strip().split(" ")
    tokens = []
    regex = r"(\b[^\s]+\b)((?<=\.\w).)?"
    matches = re.finditer(regex, s)
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        tokens.append(match.group())

    '''
    for i in words:
        i = str(i.strip()).lower()
        if i.isdigit() or (i in sList):
            continue
        
        if ('.' in i):
            index = i.index(".")
            i = i[:index] + i[index+1:]
        if (',' in i):
            index = i.index(",")
            i = i[:index] + i[index + 1:]
        if ('!' in i):
            index = i.index("!")
            i = i[:index]
        if ('?' in i):
            index = i.index("?")
            i = i[:index]
        if i.isalpha():
            tokens.append(i)
        if i in cList:
            #temp = cList[i].split(" ")
            #for w in temp:
            tokens.append(i)
        
        tokens.append(i)
        '''
    return tokens

#def calc_neg_words():

neg_word_dict = {}
total_neg_words = 0
for i in neg_train:
    #print "Neg_train",i
    temp = tokenize(i)
    #print "Temp",temp
    for j in temp:
        if j not in whole_word_dict:
            whole_word_dict[j] = 1
        if j not in neg_word_dict:
            neg_word_dict[j] = 2
            total_neg_words += 1
        else:
            neg_word_dict[j]+= 1
            total_neg_words += 1

#    return total_neg_words,neg_word_dict


#total_neg_words,neg_word_dict = calc_neg_words()


#def calc_pos_words():

pos_word_dict = {}
total_pos_words = 0
for i in pos_train:
    temp = tokenize(i)
    for j in temp:
        if j not in whole_word_dict:
            whole_word_dict[j] = 1

        if j not in pos_word_dict:
            pos_word_dict[j] = 2
            total_pos_words += 1
        else:
            pos_word_dict[j]+= 1
            total_pos_words += 1

#    return total_pos_words,pos_word_dict


#total_pos_words,pos_word_dict = calc_pos_words()

total_words = len(whole_word_dict)


#Add one smoothing
#def smoothing():
for i in whole_word_dict:
    if i not in pos_word_dict:
        pos_word_dict[i] = 1
        #pos_word_dict["UNK"]+= 1
    if i not in neg_word_dict:
        neg_word_dict[i] = 1
        #neg_word_dict["UNK"] += 1


#fun.call
#smoothing()

print len(pos_word_dict) , len(neg_word_dict)

def sc_test(test):

    t_pos = 0
    t_neg = 0
    for i in range(len(test)):
        sample_test = tokenize(test[i])
        pos_prob = prob_pos
        #print "Initial pos prob:",pos_prob
        for i in sample_test:
            if i in pos_word_dict:
                temp = pos_word_dict[i] / float(total_pos_words+total_words)
            #else:
            #    temp = pos_word_dict["UNK"] / float(total_pos_words + total_words)
                pos_prob = pos_prob * temp

        neg_prob = prob_neg
        #print "Initial neg prob:", neg_prob
        for i in sample_test:
            if i in neg_word_dict:
                temp = neg_word_dict[i] / float(total_neg_words+total_words)
            #else:
            #   temp = neg_word_dict["UNK"] / float(total_neg_words + total_words)
                neg_prob = neg_prob * temp

        #print "pos:",pos_prob
        #print "neg:",neg_prob

        if pos_prob > neg_prob:
            #print "Positive review"
            t_pos+= 1
        else:
            #print "Negative review"
            t_neg+= 1

    print "Total pos:",t_pos
    print "Total neg:",t_neg

#for i in whole_word_dict:
#    print i
a = []
a.append("I didn't enjoy my experience in this hotel because their were insects in my hotel room and it seemed very dirty.")
a.append("Recently I traveled to Phenix City, Alabama to visit my brother who is in the army and stationed in Fort Benning, Georgia. The trip was lengthy and by the time I arrived in Phenix City I was absolutely worn out. I decided to check in at the Quality Inn. I ended up staying there for three nights and enjoyed everything about it. They had the absolute best hot continental breakfast that I have ever had at a hotel and my suite was always clean and stocked with fresh blankets and towels. If I had the opportunity, I would definitely stay there again.")
a.append("The Beachcomber Resort & Villas is what makes South Florida, South Florida. The moment I walked in I was taken back by the beautiful decor, and greeted by friendly staff. I was able to check in quickly, and with no hassle. The room was more amazing then expected! It had a BEAUTIFUL view! I looked out and saw ALL of Ft. Lauderdale on a crystal clear day. At this point, I decided I’d rather be on the beach then look at it, and no sooner then that I walked out the back door of the hotel, and was right on the beach. Beachcomber is amazing, the rooms, the service, the amenities all exceeded my very high expectations.")

#sc_test(pos_test)
#sc_test(neg_test)
#sc_test(a)
print "Over"