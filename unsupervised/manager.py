#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe

'''

from unsupervised.classifier import Classifier
from utils.Xml_generator import Generator
import configuration.settings as settings

class UnsupervisedManager:
    def __init__(self , xml_file=""):
        self.__xml_file = xml_file
        self.__comments = []
        self.__labels = []
    
    def classify_multiple_comments(self):
        generator = Generator(self.__xml_file , True , 3)
        data = generator.get_vector_tagged_comments()
        for i in data:
            print data 
    
    def classify_comment(self , comment):
        obj = Classifier()
        obj.classify(comment)
        sentiment = obj.get_label()
        return sentiment 

if __name__ == '__main__':
    
     
    classifier = UnsupervisedManager(settings.testPeruvian)
    classifier.classify_multiple_comments()
    #comentario = "La tercera fue la vencida!! Felicidades al Real Madrid por ganar la Copa al eterno rival"
    #comentario2 = "es un desastre pesimo"
    #print classifier.classify_comment(comentario2)
    
 
