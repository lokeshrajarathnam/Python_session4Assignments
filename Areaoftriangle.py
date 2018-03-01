# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:54:32 2018

@author: lokesh.r
"""
"""
Problem​ ​Statement​ ​1:
Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
"""

class Sides:
    
    def __init__(self,hypo,adj,opp):
        self._hypo = hypo
        self._adj = adj
        self._opp = opp
        
    def __str__(self):
        return "%d %d %d are sides of the Triangle " %(self._hypo, self._adj, self._opp)
    
class Area(Sides):
    
    def __init__(self,*v):
       super(Area,self).__init__(*v)
        
    def area(self):
        s = (self._hypo+self._adj+self._opp)/2
        area = (s*(s-self._hypo)*(s-self._adj)*(s-self._opp)) ** 0.5
        print("Area of the given triange is %f cm square" %(area))
        
A = int(input("Lenght of the Hypotenus"))
B = int(input("Lenght of the Adjecent"))
C = int(input("Lenght of the Opposit"))
s = Sides(A,B,C)
a = Area(s._hypo,s._adj,s._opp)
a.area()

"""
Problem​ ​Statement​ ​2:
Write a function filter_long_words() that takes a list of words and an integer n and returns the list
of words that are longer than n.
"""
def filter_long_words(li,n):
    a = [i for i in li if len(i)>n]
    print("List of words grater than lenght %d is %s" %(n,a))
    
filter_long_words(["hi","hello","adadfadsf","erwerw"],6)
    
