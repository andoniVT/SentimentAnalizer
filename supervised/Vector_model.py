#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

#sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
# -*- coding: utf-8 -*-
import utils.Xml_generator as XML
import preprocessing.Comment_proceser as CP
from scipy import spatial
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
import cPickle
from configuration.settings import vector_models_two_classes , vector_model_three_classes

class VectorModel(object):
    
    def __init__(self, xml_file , nClasses):
        self.__xml_file = xml_file
        self.__nClasses = nClasses
        self.__all_data = []
        self.__comments = []
        self.__labels = []
        self.__vectorizer = []
        self.__corpus_simple_vector = []
        self.__transformer = []
        self.__corpus_tf_idf = []
        self.__prepare_corpus()

    def __prepare_corpus(self):
        xml = XML.Generator(self.__xml_file , True , self.__nClasses) 
        self.__all_data =  xml.get_vector_tagged_comments()
        for i in self.__all_data:
            self.__comments.append(i[0])
            self.__labels.append(i[1])

        self.__vectorizer = CountVectorizer()
        '''
        aux = 1
        for i in self.__comments:
            if i is None:
                print "index: " + str(aux)
                print i 
                print "None"
                print "\n\n"
            else:
                print str(aux) + ": "  + i
            aux+=1

        print len(self.__comments)'''
        vector = self.__vectorizer.fit_transform(self.__comments)
                        
        self.__corpus_simple_vector = vector.toarray()
        file_name1 = "vector_model/vectorizerSimple.pk1"
        with open(file_name1 , 'wb') as fid:
            cPickle.dump(self.__vectorizer , fid)

        self.__transformer = TfidfTransformer()
        tfidf = self.__transformer.fit_transform(self.__corpus_simple_vector)
        self.__corpus_tf_idf = tfidf.toarray()
        file_name2 = "vector_model/vectorizerTF_IDF.pk1"
        with open(file_name2 , 'wb') as fid:
            cPickle.dump(self.__transformer , fid)
        
    def get_comment_frequency_vector(self , comments):
        vectores = []
        vec_comments = []
        for i in comments:
            comm = CP.Comment_proccesor(i , True)
            comentario_procesado = comm.get_processed_comment()
            vec_comments.append(comentario_procesado)
        vectores = self.__vectorizer.transform(vec_comments).toarray()            
        return vectores

    def get__comment_tf_idf_vector(self , comments):
        vector = self.get_comment_frequency_vector(comments)
        result = self.__transformer.transform(vector).toarray()
        return result

    def get_lsi_vector(self , comment):
        pass
        '''
        comm = CP.Comment_proccesor(comment , True)
        comentario_procesado = comm.get_processed_comment()
        new_vec = self.__dictionary.doc2bow(comentario_procesado.lower().split())        
        vec_tf_idf = self.__tfidf[new_vec]
        vec_lsi = self.__lsi[vec_tf_idf]
        return vec_lsi
        '''

    def get_frequency_corpus(self):
        return [self.__corpus_simple_vector , self.__labels]
        
    def get_tf_idf_corpus(self):
        return [self.__corpus_tf_idf , self.__labels]

    def get_lsi_corpus(self):
        pass
        #return [self.__corpus_lsi , self.__vector_polarity]

if __name__ == '__main__':    
     
    xml_file = "este_XML.xml"
    '''
    model = VectorModel(xml_file)
    comentario = ["Y ese jugador q tanto admira la aficion y no da la cara cuando hay q estar. Si no siente los colores q se vaya. Mas huevos. Leo Messi"]
    vec_simple = model.get_comment_frequency_vector(comentario)
    vec_tf_idf = model.get__comment_tf_idf_vector(comentario)
    print vec_simple
    print vec_tf_idf
    '''
    
    print "hello"
     