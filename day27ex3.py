#create a program capable of displaying question
#to the user likre kbc.
#use list data type to store the question and their correct answer
#kon bnega crorpati question

question=("how many elements are in the periodic table",
          "which animals lays the largest eggs?",
          "what is the most abundant gas in earth's atmosphere?",
          "how many bones are the human body?",
          "which planet in the solar system is the hottest?:")
          
option=(("a. 117","b.116","c.118","d.119"),
        ("a.whale","b.crocodile","c.Elephant","d.ostrich"),)
        # ("a.","b.","c.","d."),
        # ("a.","b.","c.","d.")

answer=("c.","b.","a.","d.")

guess=[]
amount_win=10000
print(question)
print(answer)