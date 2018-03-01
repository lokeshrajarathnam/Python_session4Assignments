# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:17:26 2018

@author: lokesh.r
"""
"""
Problem​ ​Statement​ ​1:
Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
"""
def list_words(li):
    list_len = []
    for i in li:
        list_len.append(len(i))
    print(list_len)
"""
Problem​ ​Statement​ ​2:
Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
a vowel, False otherwise.
"""
def vowel_test(st):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for i in vowel:
        if i == st:
            return True
    return False
        

l= ['python',"php",'java','plsql']
list_words(l)

o = vowel_test(input("press alphabet key :"))
print(o)