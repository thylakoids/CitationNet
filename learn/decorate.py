#coding=utf-8
def f1(arg):
    print "f1"
    rl = arg()
    print rl
    return rl + "f1"
    
@f1
def f2(arg = ""):
    print "f2"
    return arg + "f2r"

print "start"
print f2
#print f2("1") 出错
#print f1(None)
