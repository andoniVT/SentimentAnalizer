#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

import utils.Xml_generator as XML
import preprocessing.Comment_proceser as CP

class Processor(object):

    def __init__(self, xml_file , size , type , classM , nClasses):
        self.__xml_file = xml_file
        self.__size = size
        self.__vector_data = []
        self.__vector_data_polarity = []
        self.__type = type
        self.__classM = classM
        self.__nClasses =  nClasses

        if self.__type:
            self.__get__comments_data_polarity()
            self.__process_data()
            #print self.__vector_data_polarity
            
        else:
            self.__get__comments_data()
            self.__process_data()
            #print self.__vector_data
            
    
    def __get__comments_data(self):
        xml = XML.Generator(self.__xml_file , self.__type , self.__nClasses)
        auxiliar = xml.get_vector_comments()  
        for i in range(self.__size):
            self.__vector_data.append(auxiliar[i])
        #print self.__vector_data     

    def __get__comments_data_polarity(self):
        xml = XML.Generator(self.__xml_file , self.__type , self.__nClasses)
        auxiliar = xml.get_vector_tagged_comments()
        for i in range(self.__size):
            self.__vector_data_polarity.append(auxiliar[i])
            #print self.__vector_data_polarity[i]
        #print self.__vector_data_polarity

    def __process_data(self):
        if len(self.__vector_data)!=0:
            for i in range(self.__size):
                process = CP.Comment_proccesor(self.__vector_data[i] , self.__classM)
                self.__vector_data[i] = process.get_processed_comment()

        if len(self.__vector_data_polarity)!=0:
            for i in range(self.__size):
                process = CP.Comment_proccesor(self.__vector_data_polarity[i][0] , self.__classM)
                nuevo = process.get_processed_comment()
                value = (nuevo , self.__vector_data_polarity[i][1])
                self.__vector_data_polarity[i] = value
                #print self.__vector_data_polarity[i]

    def organize_data(self , xml_out):
        xml = XML.Generator(self.__xml_file , self.__type , self.__nClasses)
        if len(self.__vector_data)!=0:
            xml.set_vector_comments(self.__vector_data)
            xml.generate_xml(xml_out)

        if len(self.__vector_data_polarity)!=0:
            xml.set_vector_tagged_comments(self.__vector_data_polarity)
            xml.generate_xml(xml_out)

    def get_proccesed_data(self):
        if self.__type:
            return self.__vector_data_polarity
        else:
            return self.__vector_data
                    

if __name__ == '__main__':

    #procesador = Processor("hola" , 10)

    ruta = "Corpus/prueba.xml"
    print ruta     

    #procesador = Processor(ruta , 100 , True , True)
    #procesador.organize_data("este_XML.xml")

