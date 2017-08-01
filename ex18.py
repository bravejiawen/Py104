def p_two(*args):
    arg1, arg2 = args
    print "arg1:%r, arg2:%r" %(arg1,arg2)
	

def p_one(arg1,arg2):
    print "arg1:%r, arg2:%r" %(arg1,arg2)
	
def one(arg1):
    print "arg1:%r"%(arg1)
	
def none():
    print "nothing"

p_two("i", "you")
p_one("i", "you")
one('i')
none()


	
