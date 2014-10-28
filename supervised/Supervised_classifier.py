#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

import Vector_model as VM
import nltk.classify
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import cPickle
from configuration.settings import spanish_classifiers_two_classes_simple , spanish_classifiers_two_classes_tf_idf , \
    spanish_classifiers_three_classes_simple , spanish_classifiers_three_classes_tf_idf , \
    svm , naiveBayes , maxEntropia , decTree , path

default_path = path

class SuppervisedClassifier(object):
    def __init__(self , data=None , labels=None):
        print "Suppervised Classifier :"
        self.data = data
        self.labels = labels
        self.classifier = []        
        self.file_name = ""
        self.domain = 0
        self.nClasses = 0
        self.model = 0
        self.current_path = ''

    def train(self):
        pass 

    def classify(self , vector_comentarios):
        pass

    def classification_report(self , y_true , y_pred):
        print classification_report(y_true , y_pred)

    def save_classifier(self , file):
        with open(file , 'wb') as fid:
            cPickle.dump(self.classifier , fid)

    def load_classifier(self , file):
        with open(file , 'rb') as fid:
            clf_load = cPickle.load(fid)
        return clf_load

    def set_file_name(self , name):
        self.file_name = name + self.file_name

    def imprime(self):
        print self.file_name
    
    def set_path_values(self , domain , nClasses , model):
        self.domain = domain
        self.nClasses = nClasses 
        self.model = model
        
    def define_path(self):
        if self.domain == 1:
            if self.nClasses == 2:
                if self.model == 1:                    
                    self.current_path = spanish_classifiers_two_classes_simple
                else:                    
                    self.current_path = spanish_classifiers_two_classes_tf_idf
            if self.nClasses == 3:
                if self.model == 1:                
                    self.current_path = spanish_classifiers_three_classes_simple
                else:
                    self.current_path = spanish_classifiers_three_classes_tf_idf
        else:
            if self.nClasses == 2:
                if self.model == 1:
                    print 1
                else: 
                    print 2
            if self.nClasses == 3:
                if self.model == 1:
                    print 1
                else:
                    print 2 


class NaiveBayes(SuppervisedClassifier):
    def __init__(self , data=None , labels=None):        
        SuppervisedClassifier.__init__(self , data , labels)
        print "--Naive Bayes--"
        self.file_name = default_path + naiveBayes
    
    def define_path(self):
        SuppervisedClassifier.define_path(self)        
        self.file_name = self.current_path + naiveBayes
        
    def train(self):
        super(NaiveBayes , self).train()
        self.classifier = MultinomialNB()
        self.classifier = self.classifier.fit(self.data , self.labels)
        self.save_classifier(self.file_name)

    def classify(self , vector_comentarios):
        super(NaiveBayes , self).classify(vector_comentarios)
        predictions = []
        classifier = self.load_classifier(self.file_name)
        for i in vector_comentarios:
            value = classifier.predict(i)     
            predictions.append(value)
        return predictions
    
class SVM(SuppervisedClassifier):
    def __init__(self , data=None , labels=None):        
        SuppervisedClassifier.__init__(self , data , labels)
        print "--Support Vector Machine--"
        self.file_name = default_path + svm

    def define_path(self):
        SuppervisedClassifier.define_path(self)        
        self.file_name = self.current_path + svm        
        
    def train(self):
        super(SVM , self).train()
        self.classifier = LinearSVC()
        self.classifier = self.classifier.fit(self.data , self.labels)
        self.save_classifier(self.file_name)

    def classify(self , vector_comentarios):
        super(SVM , self).classify(vector_comentarios)
        predictions = []
        classifier = self.load_classifier(self.file_name)
        for i in vector_comentarios:
            value = classifier.predict(i)
            predictions.append(value)
        return predictions

class DecisionTree(SuppervisedClassifier):
    def __init__(self , data=None , labels=None):
        SuppervisedClassifier.__init__(self, data, labels)
        print "--Decision Tree--"
        self.file_name = default_path + decTree
    
    def define_path(self):
        SuppervisedClassifier.define_path(self)        
        self.file_name = self.current_path + decTree        
        
    def train(self):
        super(DecisionTree , self).train()
        self.classifier = DecisionTreeClassifier()
        self.classifier = self.classifier.fit(self.data , self.labels)
        self.save_classifier(self.file_name)

    def classify(self , vector_comentarios):
        super(DecisionTree , self).classify(vector_comentarios)
        predictions = []
        classifier = self.load_classifier(self.file_name)
        for i in vector_comentarios:
            value = classifier.predict(i)
            predictions.append(value)
        return predictions

class MaxEnt(SuppervisedClassifier):
    def __init__(self, data=None , labels=None):
        SuppervisedClassifier.__init__(self , data, labels)
        print "-- Entropia Maxima--"        
        self.file_name = default_path + maxEntropia

    def define_path(self):
        SuppervisedClassifier.define_path(self)        
        self.file_name = self.current_path + maxEntropia        
        
    def train(self):
        super(MaxEnt , self).train()
        self.classifier = LogisticRegression()
        self.classifier = self.classifier.fit(self.data , self.labels)
        self.save_classifier(self.file_name)

    def classify(self , vector_comentarios):
        super(MaxEnt , self).classify(vector_comentarios)
        predictions = []
        classifier = self.load_classifier(self.file_name)
        for i in vector_comentarios:
            value = classifier.predict(i)
            predictions.append(value)
        return predictions

if __name__ == '__main__':    
    '''
    path values:
      * domain:  spanish(1) - peruvian(2)
      * nClasses: 2-classes (2)  - 3-classes (3)
      * model:    vectorial (1) - tfidf(2)
    '''    
    vec = [[1,2,3,4,5] ,[1,2,3,4,5], [1,2,3,4,5] ,[1,2,3,4,5] ,[1,2,3,4,5] ]
    labels =  [1 , 0 , 1, 0 , 0]
    dt = MaxEnt(vec, labels)
    dt.set_path_values(1 , 2 , 1)
    dt.define_path()
    dt.train()     