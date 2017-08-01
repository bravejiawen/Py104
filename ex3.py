# -*- coding: utf-8 -*-
print "i will now count mu chickens:"
#%为取余数，优先级为 */ +-
print "hens",25 + 30 / 6
print "roosters",100 - 25 * 3 % 4

print "now i will count the eggs:"
#得出来的为整数--为提高精确度，增加了float,但是一定要改数字精度？
#原：print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6  =7
print 3 + 2 + 1 - 5 + 4 % 2 - float(1.00 / 4.00) + 6

print "is it true that 3 + 2 < 5 - 7?"
#<为判断，输出ture 或者false
print 3 + 2 < 5 - 7
#不加“”，可进行运算
print "what is 3 + 2?",3 + 2
print "what is 5 - 7?",5 - 7

print "oh, that's why it's false. "

print "how about some more"

print "is it greater?", 5 > -2
print "is it greater or equal?", 5 >= -2
print "is it less or equal?", 5 <= -2