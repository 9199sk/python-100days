#my program code to decode
sk=input("enter a message:")
words=sk.split(" ")
coding=input(" 1 for coding or 0 for decoding")
coding=True if(coding=="1") else False
print(coding)
if(coding):
    nwords=[]
    for word in words:
        if (len(word)>=3):
            r1="dsf"
            r2="jsf"
            sknew=r2+word[1:]+word[0]+r2
            nwords.append(sknew)
        else:
            nwords.append(word[::-1])
            print("".join(nwords))

    else:
        nwords=[]
    for word in words:
        if (len(word)>=3):
            r1="dsf"
            r2="jsf"
            sknew=r2+word[1:]+word[0]+r2
            nwords.append(sknew)
# else:
#     nwords.append(word[::-1])
#     print("".join(nwords))

