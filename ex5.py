# -*- coding: utf-8 -*-
my_name = 'jiawen'
my_age = 25
my_height = 158 #cm
my_weight = 45 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'brown'

#%r 会显示所有内容，%s，把变量的值或字符串放到%s所在的位置，区别：%r用来做调试最好。
print "let's talk about %s." % my_name
#too long ,how to get two line?
print "she's got %s eyes and %s hair.%s tall,%s weight" %(my_eyes,my_hair,my_height*0.01,my_weight*2)

