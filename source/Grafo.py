# -*- coding: utf-8 -*-

from ListaAdj import ListaAdj

# Representação de Infinito
INF = 1E8

'''
Classe que constrói o grafo a partir do arquivo e da
Estrutura de dados escolhidos
'''
class Grafo(object):

    '''
    Construtor da classe
    '''
    def __init__(self, tipo_estrutura, path, arquivo = None):
        self.__arquivo = arquivo
        self.__tipo_estrutura = tipo_estrutura
        self.__path = path

    '''
    Efetua a leitura no arquivo
    '''
    def __leituraArquivo(self):
        self.__arquivo = open(self.__path, 'r')
        return self.__arquivo.readlines()

    '''
    Cria o grafo
    '''
    def _cria(self):

        linhas = self.__leituraArquivo()

        nroVertices = linhas[0].split()
        nroVertices = int(nroVertices[0])
        
        g = ListaAdj(nroVertices)
        
        # Busca cada vértice do grafo e os adiciona em uma lista de inteiros
        vertices = set([])
        for i in range(1, len(linhas)):
            linha = linhas[i].split()
            vertices.add(linha[0])
            vertices.add(linha[1])
        vertices = set(map(int, vertices)) # Parsing dos vertices para int

        # Cria o grafo sem valores
        for i in vertices:
            g._add(str(i))
        
        # Popula o grafo
        for i in range(1, len(linhas)):
            linha = linhas[i].split()
            if(len(linha) == 2): # Se for nao-valorado
                g._add(linha[0], linha[1], 1)
                
            else: # Se for valorado
                g._add(linha[0], linha[1], float(linha[2]))
                
        return g