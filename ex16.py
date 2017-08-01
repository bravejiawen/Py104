# -*- coding: utf-8 -*-
#读写文件
#从sys模块里导入参数变量argv
from sys import argv
#将变量argv解包，两个参数依次赋给script,filename
script, filename = argv

print "we are going to erase %r." % filename
print "if you don't want that, hit CTRL-C (^C)."
print "if you do want that ,hit RETURN."
#获取输入的字符串...(没有用？)
raw_input("?")
# 以 写入 的模式打开文件，target 相当于磁带机 .truncate相当于做播放暂停或清除等动作
print "opening the file..."
target = open(filename, 'w')
#清空文件的内容
print "truncating the file.  bye!"
target.truncate()

print "now i'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "i'm going to write these to the file."
#做“录音”动作，写入内容
#下面注释为练习时代码
"""target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
#要求改为一行
#write只能读一个，所以将变量都赋值给另一个变量，啊哈哈，成功了
lines = "%s\n%s\n%s\n"%(line1,line2,line3)
target.write(lines)

#关掉并保存 
print "and finally, we close it."
target.close()