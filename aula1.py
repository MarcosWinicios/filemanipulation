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


def storeLinesFile(fname):
    with open(fname) as f:
        # Content_list is the list that contains the read lines
        content_list = f.readlines()
        print(content_list)


fileRead('/home/marcosw/Workspaces/Python/test.txt')
fileCreateWrite('/home/marcosw/Workspaces/Python/abc.txt')
storeLinesFile('/home/marcosw/Workspaces/Python/abc.txt')
