#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe

'''
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from unsupervised.classifier import Classifier
from utils.Xml_generator import Generator
import configuration.settings as settings
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class UnsupervisedManager:
    def __init__(self , xml_file=""):
        self.__xml_file = xml_file
        self.__comments = []
        self.__labels = []
    
    def classify_multiple_comments(self):
        generator = Generator(self.__xml_file , True , 3)
        data = generator.get_vector_tagged_comments()
        for i in data:
            self.__comments.append(i[0])
            self.__labels.append(i[1])
        clasificados = []    
        for i in self.__comments:
            sentiment =  self.classify_comment(i)
            clasificados.append(sentiment)
        return clasificados
                    
    def classify_comment(self , comment):
        obj = Classifier()
        obj.classify(comment)
        sentiment = obj.get_label()
        return sentiment
    
    def show_report(self , y_predicted):
        y_true= []
        y_predicted_new = []
        
        
        
        for i in range(len(self.__labels)):
            if self.__labels[i] == 'P':
                y_true.append(1)
            if y_predicted[i] == 'positivo':
                y_predicted_new.append(1)
            if self.__labels[i] == 'N':
                y_true.append(-1)
            if y_predicted[i] == 'negativo':
                y_predicted_new.append(-1)
            if self.__labels[i] == 'NEU':
                y_true.append(0)
            if y_predicted[i] == 'neutral':
                y_predicted_new.append(0)
                        
        print classification_report(y_true, y_predicted_new)
        print confusion_matrix(y_true, y_predicted_new)
         


if __name__ == '__main__':
    
     
    classifier = UnsupervisedManager(settings.trainSpanish)
    predicted = classifier.classify_multiple_comments()
    classifier.show_report(predicted)
    
    #comentario = "La tercera fue la vencida!! Felicidades al Real Madrid por ganar la Copa al eterno rival"
    #comentario2 = "es un desastre pesimo"
    #print classifier.classify_comment(comentario2)
    
 
    