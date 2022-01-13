#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
# num vetor a média de cada aluno, imprima o número de alunos com média maior
# ou igual a 7.0.

def file_read(fname):  # Lendo conteúdo de uma arquivo
    txt = open(fname)
    print(txt.read())


def file_create_and_write(fname):
    with open(fname, "w") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises")
    txt = open(fname)
    print(txt.read())


file_read('/home/marcosw/Workspaces/Python/test.txt')
file_create_and_write('/home/marcosw/Workspaces/Python/abc.txt')
