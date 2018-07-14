f=lambda x:sorted(str(x))
x=99999
while not f(x*2) == f(x*3) == f(x*4) == f(x*5) == f(x*6): x += 9
print ("The element is x="),x
print("Proof")
print "x=",x,("\n2x="),2*x,("\n3x="),3*x,("\n4x="),4*x,("\n5x="),5*x,("\n6x="),6*x





