#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''
import utils.Xml_generator as XML
import preprocessing.Comment_proceser as CP
from scipy import spatial
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD as LSA
import cPickle
from configuration.settings import vector_models_two_classes , vector_model_three_classes , prueba

class VectorModel(object):
    
    def __init__(self, xml_file , nClasses , domain):
        self.__xml_file = xml_file
        self.__nClasses = nClasses
        self.__domain = domain
        self.__all_data = []
        self.__comments = []
        self.__labels = []
        self.__vectorizer = []
        self.__corpus_simple_vector = []
        self.__transformer = []
        self.__corpus_tf_idf = []
        self.__prepare_corpus()

    def __prepare_corpus(self): 
        # 1 -> espanish   2-> peruvian
        if self.__domain == 1:
            if self.__nClasses == 2:
                path = vector_models_two_classes
            if self.__nClasses == 3:
                path = vector_model_three_classes
        else:
            if self.__nClasses == 2:
                path = 'falta'
            if self.__nClasses == 3:
                path = 'falta2'
             
        
        xml = XML.Generator(self.__xml_file , True , self.__nClasses) 
        self.__all_data =  xml.get_vector_tagged_comments()
        for i in self.__all_data:
            self.__comments.append(i[0])
            self.__labels.append(i[1])        
        

        self.__vectorizer = CountVectorizer()
        vector = self.__vectorizer.fit_transform(self.__comments)
                        
        self.__corpus_simple_vector = vector.toarray()
        
        file_name1 = path + "/vectorizerSimple.pk1"
        with open(file_name1 , 'wb') as fid:
            cPickle.dump(self.__vectorizer , fid)
        
        file_name11 = path + "/simple_corpus.pk1"
        with open(file_name11 , 'wb') as fid:
            cPickle.dump(self.__corpus_simple_vector , fid)

        self.__transformer = TfidfTransformer()
        tfidf = self.__transformer.fit_transform(self.__corpus_simple_vector)
        self.__corpus_tf_idf = tfidf.toarray()
        file_name2 = path + "/vectorizerTF_IDF.pk1"
        with open(file_name2 , 'wb') as fid:
            cPickle.dump(self.__transformer , fid)
        
        file_name22 = path + "/tf_idf_corpus.pk1"
        with open(file_name22 , 'wb') as fid:
            cPickle.dump(self.__corpus_tf_idf , fid)
                
        
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
     
    xml_file = prueba
    
    model = VectorModel(xml_file , 3 , 1)
    
    comentario = ["Agradezco a trabajadores y sindicatos la desconvocatoria de la huelga en el aeropuerto"]
     
    vec = model.get_comment_frequency_vector(comentario)
    vec2 = model.get__comment_tf_idf_vector(comentario)
    for i in vec2:
        print i
    
    
     