import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#old_code
import re
import nltk

neg_review = []
pos_review = []
total_review = []
total_sentiment = []
combined_rev_sen = []
combined_feaVec_sen = []
total_featureVec = []

def replaceTwoOrMore(s):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)


def getFeatureVector(text,sWords):
    featureVector = []
    #split tweet into words
    words = text.split()
    for w in words:
        w = replaceTwoOrMore(w)
        w = w.strip('\'"?,.')
        val = re.search(r"^[a-zA-Z]*$", w)  #^[a-zA-Z][a-zA-Z0-9]*$
        if(w in sWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector

def extract_features(sentence):
    t_words = set(sentence)
    features = []
    for word in total_featureVec:
        if word in t_words:
            features.append(1)
        else:
            features.append(0)
    return features


neg = open("/home/hari/Documents/NLP/HW3/hotelNegT-train.txt","r")
pos = open("/home/hari/Documents/NLP/HW3/hotelPosT-train.txt","r")

neg_tupl = []
neg_tupl.append(0)
#neg_tupl.append(1)

pos_tupl = []
pos_tupl.append(1)
#pos_tupl.append(0)

for i in neg:
    review = i.split("\t")
    neg_review.append(review[1])
    '''
    temp = "0 |" + str(review[1])
    combined_rev_sen.append(temp)
    total_review.append(review[1])
    total_sentiment.append(neg_tupl)
    '''

for i in pos:
    review = i.split("\t")
    pos_review.append(review[1])
    '''
    temp = "1 |" + str(review[1])
    combined_rev_sen.append(temp)
    total_review.append(review[1])
    total_sentiment.append(pos_tupl)
    '''

neg_train,neg_test = train_test_split(neg_review,test_size=0.2)
pos_train,pos_test = train_test_split(pos_review,test_size=0.2)



for i in neg_train:
    temp = "0 |" + str(i)
    combined_rev_sen.append(temp)
    total_review.append(i)
    total_sentiment.append(neg_tupl)

for i in pos_train:
    temp = "1 |" + str(i)
    combined_rev_sen.append(temp)
    total_review.append(i)
    total_sentiment.append(pos_tupl)


print combined_rev_sen[1]

#stopWords = ["i","a","an","and","as","at","be","by","for","from","has","he","in","is","it","its","of","on","that","the","to","was","were","with"]
stopWords = []
stp = open("/home/hari/Documents/NLP/HW3/stopwords.txt","r")
for i in stp:
    i = i.strip()
    stopWords.append(i)

print "stopwords len:", len(stopWords), stopWords[8]
print "total reviews:", len(total_review)

for i in range(len(total_review)):

    featureVec = getFeatureVector(total_review[i],stopWords)
    total_featureVec.extend(featureVec)
    combined_feaVec_sen.append((featureVec,total_sentiment[i]))

total_featureVec = list(set(total_featureVec))
print "features size: ", len(total_featureVec)
#training_set = nltk.classify.util.apply_features(extract_features, total_review)
training_set = []
rev_features = []
for i in range(len(total_review)):

    rev_features.append(extract_features(combined_feaVec_sen[i][0]))

training_set = zip(rev_features,total_sentiment)

print type(training_set)
print type(training_set[0]),len(training_set[0])
print training_set[0]

t_features = len(total_featureVec)
#print t_features
count = 0
for i in rev_features:
    if 1 in i:
        indices = [i for i, x in enumerate(i) if x == 1]
        print indices
#print "Total sentences that contain 1 are:", count
#print "label for 0:",combined_feaVec_sen[0][1]
input_matrix = np.matrix(rev_features)
print input_matrix.shape[1]
output_matrix = np.matrix(total_sentiment)
print output_matrix.shape

def sigmoid(scores):
    return 1 / (1 + np.exp(-scores))

def log_likelihood(features, target, weights):
    scores = np.dot(features, weights)
    ll = np.sum( target*scores - np.log(1 + np.exp(scores)) )
    return ll

def logistic_regression(features, target, num_steps, learning_rate, add_intercept=False):
    if add_intercept:
        intercept = np.ones((features.shape[0], 1))
        features = np.hstack((intercept, features))

    weights = np.zeros(features.shape[1])

    for step in xrange(num_steps):
        scores = np.dot(features, weights)
        predictions = sigmoid(scores)

        # Update weights with gradient
        output_error_signal = target - predictions
        gradient = np.dot(features.T, output_error_signal)
        weights += learning_rate * gradient

        # Print log-likelihood every so often
        if step % 10000 == 0:
            print log_likelihood(features, target, weights)

    return weights

weights = logistic_regression(input_matrix, output_matrix,
                     num_steps = 30, learning_rate = 5e-5, add_intercept=True)
