# -*- coding:utf-8 -*-
from sys import argv

script, input_file = argv
#定义了三个函数，第一个输出显示文件内容，第二个位置回到文档最开始的字节，第三个输出显示文档的一行
#readline 执行完一次后位置会留在当前，再次执行时输出下一行
def print_all(f):
    print f.read()
#seek（）回到文件最开始的地方	
def rewind(f):
    f.seek(0)
	#在print语句后加’ ,‘ 使打印完后不自动换行
def print_a_line(line_count, f):
    print line_count, f.readline(),
	
current_file = open(input_file)

print "first let's print the whole file:\n"

print_all(current_file)

print "now rewind"
#位置指针重新指向开头
rewind(current_file)

print "print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)