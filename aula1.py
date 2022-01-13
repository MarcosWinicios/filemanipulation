#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
# num vetor a média de cada aluno, imprima o número de alunos com média maior
# ou igual a 7.0.

def fileRead(fname):  # Lendo conteúdo de uma arquivo
    txt = open(fname)
    print(txt.read())


def fileCreateWrite(fname):  # Criar um arquivo, escrever e mostrar o conteúdo:
    with open(fname, "w") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())


def storeLinesFile(fname):  # Armazenar as linhas de um arquivo em uma lista:
    with open(fname) as f:
        # Content_list is the list that contains the read lines
        content_list = f.readlines()
        print(content_list)


def storeLinesFile2(fname):  # Armazenar as linhas de um arquivo em uma lista
    content_array = []
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        for line in f:
            content_array.append(line)
        print(content_array)


def writeListInFile(list=[]):  # Escrever uma lista em um arquivo:
    with open('/home/marcosw/Workspaces/Python/abc.txt', "w") as myfile:
        for c in list:
            myfile.write("%s\n" % c)
    content = open('/home/marcosw/Workspaces/Python/abc.txt')
    print(content.read())


fileRead('/home/marcosw/Workspaces/Python/test.txt')
fileCreateWrite('/home/marcosw/Workspaces/Python/abc.txt')
storeLinesFile('/home/marcosw/Workspaces/Python/abc.txt')
storeLinesFile2('/home/marcosw/Workspaces/Python/abc.txt')

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
writeListInFile(color)
storeLinesFile('/home/marcosw/Workspaces/Python/abc.txt')
