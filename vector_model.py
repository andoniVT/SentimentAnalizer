#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import TruncatedSVD as LSA

class VectorModel(object):
    
    def __init__(self, vec_comments):
        self.__vec_comments = vec_comments
        self.__vectorizer = []
        self.__corpus_simple_vector = []
        self.__transformer = []
        self.__corpus_tf_idf = []
        self.__transformer2 = []
        self.__corpus_lsa = []
        self.__prepare_models()

    def __prepare_models(self):                         
        self.__vectorizer = CountVectorizer()
        vector = self.__vectorizer.fit_transform(self.__vec_comments)                        
        self.__corpus_simple_vector = vector.toarray()
    
        self.__transformer = TfidfTransformer()
        tfidf = self.__transformer.fit_transform(self.__corpus_simple_vector)
        self.__corpus_tf_idf = tfidf.toarray()
       
        self.__transformer2 = LSA(n_components=10 , random_state=42)
        vec_lsa = self.__transformer2.fit_transform(self.__corpus_tf_idf)
        self.__corpus_lsa = vec_lsa
                        
    def get_comment_frequency_vector(self , comments):
        vec_comments = []
        for i in comments:
            vec_comments.append(i)
        vectores = self.__vectorizer.transform(vec_comments).toarray()            
        return vectores

    def get__comment_tf_idf_vector(self , comments):
        vector = self.get_comment_frequency_vector(comments)
        result = self.__transformer.transform(vector).toarray()
        return result

    def get_lsa_vector(self , comments):
        vector = self.get__comment_tf_idf_vector(comments)        
        result = self.__transformer2.transform(vector)
        return result    

if __name__ == '__main__':    
     
    corpus = ["Agradezco a trabajadores y sindicatos la desconvocatoria de la huelga en el aeropuerto" ,
                   "Los que esta noche van a la redonda a celebrar la victoria del Equipo Real Madrid ",
                   "Vuestro odio es nuestra fuerza!!!!!",
                   "Menos mal que esta Jugador-Iker_Casillas Casillas de capitan hoy",
                   "Volver a pitar el himno, volver a tirarnos el balon a la cara"]
    
    model = VectorModel(corpus)
    
    comentario = ["La tercera fue la vencida!! Felicidades al Real Madrid por ganar la Copa al eterno rival"]
     
    vec_tradicional = model.get_comment_frequency_vector(comentario)
    vec_tf_idf = model.get__comment_tf_idf_vector(comentario)
    vec_lsa = model.get_lsa_vector(comentario)
    
    print vec_tradicional
    print vec_tf_idf
    print vec_lsa
    