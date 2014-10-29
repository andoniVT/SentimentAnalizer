#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe

'''

from unsupervised.classifier import Classifier

class UnsupervisedManager:
    def __init__(self):
        pass
    
    def classify_comment(self , comment):
        obj = Classifier()
        obj.classify(comment)
        sentiment = obj.get_label()
        return sentiment 

if __name__ == '__main__':
    
    classifier = UnsupervisedManager()
    comentario = "La tercera fue la vencida!! Felicidades al Real Madrid por ganar la Copa al eterno rival"
    comentario2 = "es un desastre pesimo"
    print classifier.classify_comment(comentario2)
    
 
