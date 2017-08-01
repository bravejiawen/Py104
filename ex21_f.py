# -*- coding: utf-8 -*-
#实现 24+34/100-1023
#print 24+34/100-1023=-999
def add(a, b):
    return a + b
	
def divide(a, b):
    return a / b
	
def substract(a, b):
    return a - b
	

print substract(add(24, divide(34, 100)), 1023)