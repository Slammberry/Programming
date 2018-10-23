s= input("What is the word?")
If(s>=3 and s.endswith('ing')):
    print("%ly"%(s))
Elif(not s.endswith('ing')):
    print("%ing"%(s))
Else:
    print("%"%(s))
