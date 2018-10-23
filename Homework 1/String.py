s= input("What is the word?")
if s>=3 and s.endswith('ing'):
    print("%ly"%(s))
elif (not s.endswith('ing')):
    print("%ing"%(s))
else:
    print("%"%(s))
