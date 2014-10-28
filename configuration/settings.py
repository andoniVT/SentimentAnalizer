#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

'''
    path 
'''
#path_cicc = '/home/ucsp/Dropbox/Propuesta-implementacion/CODE/SentimentAnalizer'
path_cicc = '/home/ucsp/workspace/SentimentManager'
#path_home = '/home/andoni/Dropbox/Ciencia de la Computacion/Semestre 2014-II/Seminario de Tesis/Propuesta-implementacion/CODE/SentimentAnalizer'
path_home = '/home/andoni/Escritorio/PythonProjets/SentimentAnalizer'
#path = path_cicc
path = path_home

'''
    resource
'''
big_text = path + '/resource/big2.txt'
stop_words = path + '/resource/stopwords_spanish.txt'

'''
    data test and training
'''
trainSpanish = path + '/data/train/theTrainSpanish.xml'
trainPeruvian = path + '/data/train/theTrainPeruvian.xml'
testSpanish = path + '/data/test/theTestSpanish.xml'
testPeruvian = path + '/data/test/theTestPeruvian.xml'
prueba = path + '/data/train/prueba.xml'


'''
    suppervised classifiers
'''
spanish_path = path + '/data_trained/classifiers_trained/spanish'
spanish_classifiers_two_classes_simple = spanish_path +  '/2_classes/simple'
spanish_classifiers_two_classes_tf_idf = spanish_path + '/2_classes/tf-idf'
spanish_classifiers_two_classes_lsa = spanish_path + '/2_classes/lsa'

spanish_classifiers_three_classes_simple = spanish_path + '/3_classes/simple'
spanish_classifiers_three_classes_tf_idf = spanish_path + '/3_classes/tf-idf'
spanish_classifiers_three_classes_lsa = spanish_path + '/3_classes/lsa'

svm = '/SupportVectorMachineCorpus.pk1'
naiveBayes = '/NaiveBayesCorpus.pk1'
maxEntropia = '/MaximaEntropiaCorpus.pk1'
decTree = '/DecisionTreeCorpus.pk1'

'''
    vector model
'''
vspanish_path = path + '/data_trained/vector_model/spanish'
vector_models_two_classes =  vspanish_path + '/2_classes'
vector_model_three_classes = vspanish_path + '/3_classes'



if __name__ == '__main__':
    
    print vector_models_two_classes
