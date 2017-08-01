# -*- coding: utf-8 -*-
#调用参数变量argv.
from sys import argv
#调用命令exists
from os.path import exists

script, from_file, to_file = argv

print "coping from %s to %s"% (from_file,to_file)

"""in_file = open(from_file)
indata = in_file.read()
"""
indata=open(from_file).read()
print "the input file is %d bytes long" %len(indata)

print "does the output file exists? %r" %exists(to_file)
print "ready,hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "alright, all done."

out_file.close()
#in_file.close()
