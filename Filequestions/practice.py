with open("sample.txt",'r') as first, open("sample1.txt",'r') as second, open("thirdsample.txt",'w+') as third:
    firstfile=first.read()
    secondfile=second.read()
    thirdfile=third.write(firstfile+secondfile)






















