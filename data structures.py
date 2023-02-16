#lists in python
#all changes done before the print function
#list square brackets
myclassmate=["Antonia","Jesse","Quinn","Steffon"]
mynumber=[49,38,17,11,0]
myclassmate[2]="Sylvia"
myclassmate.append("Danny")
myclassmate.insert(4, "Kristine")
myclassmate.append("Joker")
myclassmate.insert(1, "Trixxy")
myclassmate.sort()
print(mynumber)
print(type(myclassmate))
print(myclassmate)
print("Comic Genius is "+myclassmate[1])

#tuple in python
#tuple circular brackets
myfavfruits=(1.5,"Tangerine","Watermelons","Beetroot","Apples","Grapes",17)
print(myfavfruits)
print(myfavfruits[0])

#sets datastructure
#sets curly braces
myfavcars={"Toyota","Mercedes","BMW","Nissan","Suzuki","Honda"}
myfavcars.add("Tesla")
print(myfavcars)

#dictionaries in python
#Curly braces
magari={
    "name":"Toyota",
    "Model":"Fortuner",
    "year":"2020"
}
print(magari)
print(magari[model])