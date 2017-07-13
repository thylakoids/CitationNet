class myDecorator(object):

    def __init__(self, f):
        print "inside myDecorator.__init__()"
        self.f = f

    def __call__(self):
        print "inside myDecorator.__call__()"
        self.f()

@myDecorator
def aFunction():
    print "inside aFunction()"

print "Finished decorating aFunction()"

aFunction()