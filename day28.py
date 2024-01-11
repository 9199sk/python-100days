#string formating in python
letter="hey my name is {0} and i am from {1} "
country= "india"
Name=  "Samir"
print(letter.format(Name,country))

#f- string
letter="hey my name is {Name} and i am from {country} "


price=56.0216
txt=f"for only{price:.3f} doolars!"
print(txt)

print(type(f"{2*30}"))

