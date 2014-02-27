#!/usr/bin/python
#!encoding: UTF-8
#Lo que hace el programa es que te pide dos enteros, los lee y luego realiza la operación, teniendo especial cuidado con que el valor de a nunca puede ser 0.

a=float(raw_input('valor de a: '))
b=float(raw_input('valor de b: '))

if (a != 0):
  x= -b/a
  print 'solucion: ', x
else
print'No tiene solucion'
