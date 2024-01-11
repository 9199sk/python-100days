questions=[
     
    ["which language was used to create fb?",
          "python","french","javascript",
          "php","none",4],
["which language was used to create fb?",
"python","french","javascript",
          "php","none",4],

["which language was used to create fb?",
"python","french","javascript",
          "php","none",4],

["which language was used to create fb?",
"python","french","javascript",
          "php","none",4],

["which language was used to create fb?",
"python","french","javascript",
          "php","none",4],
          ]

levels= [1000,2000,3000,5000,10000,20000,40000,
         80000,160000,320000]
money=0
for i in range(0,len(questions)):
    questions=questions[i]
    print(f"question for Rs.{levels[i]}")
    print(f"a.{questions[1]}          b. {questions[2]}")
    print(f"c.{questions[3]}          d. {questions[4]}")
    reply=int(input("enter your number(1-4)"))
    if(reply==questions[-1]):
      print(f"correct answer,you have won rs.{levels[i]}")
      if (i==4):
         money=10000
    elif (i==9):
           money=320000
    elif (i==14):
           money=300000
else:
    print("wrong answer")
























