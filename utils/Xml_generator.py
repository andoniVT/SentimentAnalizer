'''
Created on 26/10/2014

@author: Andoni Valverde Tohalino
@email: andoni.valverde@ucsp.edu.pe
'''

# -*- coding: utf-8 -*-
import elementtree.ElementTree as ET
from elementtree.ElementTree import ElementTree


class Generator(object):
    #def __init__(self, xml_file , type):
    def __init__(self, xml_file , type , nClasses):    
        self.__xml_file = xml_file
        self.__vector_tagged_comments = []
        self.__vector_comments = []
        self.__type = type
        self.__nClasses = nClasses
        if self.__type:
            self.__get_tagged_data()
        if self.__type==False:
            self.__get_non_tagged_data()

    def __get_tagged_data(self):        
        tree = ET.parse(self.__xml_file)
        root = tree.getroot()
        if self.__nClasses == 2:
            for child in root:            
                texto = child[1].text
                polaridad = child[2].text
                if polaridad!= 'NEU':  
                    value = (texto , polaridad)
                    self.__vector_tagged_comments.append(value)
        else:
            for child in root:
                texto = child[1].text
                polaridad = child[2].text
                value = (texto , polaridad)
                self.__vector_tagged_comments.append(value)         

    def __get_non_tagged_data(self):
        tree = ET.parse(self.__xml_file)
        root = tree.getroot()
        for child in root:
            texto = child[1].text
            self.__vector_comments.append(texto)

    def get_vector_tagged_comments(self):
        return self.__vector_tagged_comments

    def get_vector_comments(self):
        return self.__vector_comments

    def set_vector_tagged_comments(self , vector):
        self.__vector_tagged_comments = vector

    def set_vector_comments(self, vector):
        self.__vector_comments = vector

    def generate_xml(self , xml_out):
        id = 1
        root = ET.Element("comentarios")
        if self.__type:
            for i in self.__vector_tagged_comments:
                if i[0]!="None":                    
                    comentario = ET.SubElement(root , "comentario")
                    id_comentario = ET.SubElement(comentario , "id")
                    id_comentario.text = str(id)
                    texto = ET.SubElement(comentario , "contenido")
                    texto.text = i[0]
                    polaridad = ET.SubElement(comentario , "polaridad")
                    polaridad.text = i[1]
                    id+=1
        id = 1
        if self.__type==False:
            for i in self.__vector_comments:
                if i!="None":
                    comentario = ET.SubElement(root , "comentario")
                    id_comentario = ET.SubElement(comentario , "id")
                    id_comentario.text = str(id)
                    texto = ET.SubElement(comentario , "contenido")
                    texto.text = i
                    id+=1

        tree = ET.ElementTree(root)
        tree.write(xml_out)


if __name__ == '__main__':

    ruta = "Corpus/prueba2.xml"    

    #procesador = Generator(ruta , False)
    #procesador.generate_xml("haber.xml")



