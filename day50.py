#readlines (method)
s=open('myfile.txt','r')
while True:
    line=s.readline()
    print(line)
    if not line:
       
     print(line,type(line))
    
     break


#write line method in python
s=open('my3file.txt','w')
lines=['line 1\n','line 2\n','line 3\n',]
s.writelines(lines)
s.close








