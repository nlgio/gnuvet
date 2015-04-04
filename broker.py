#stolen from pycocuma

Providers=dict()


def Request(code ):
    #print "request %s" % code
    return Providers.get(code,None)


def UnRegister(code):
    del Providers[code]
    
def Register(code, it ):
    #print "registering %s for %s"  % ( it, code )
    Providers[code]=it
    
