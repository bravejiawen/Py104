# -*- coding: utf-8 -*-
#读文件
from sys import argv
script, filename = argv

target = open(filename)

print "here print your filename %r" %filename

print target.read()