class EmobilisStudents:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
     print(f"My name is {self.name} and I'm {self.age} years old.")
#ceating an object
myobject=EmobilisStudents("Antonia","17")
myobject.hello_me()

myobject=EmobilisStudents("Jesse Walter","20")
myobject.hello_me()

class Double:
    def __init__(self, name, birthday):
        self.name=name
        self.birthday=birthday
    def celebrate_me(self):
        print(f"I am {self.name} and my birthday is on {self.birthday}.")
myobject2=Double("Raphael","15th Feb")
myobject2.celebrate_me()


#create a class called magari, it should have model,make and year properties
#create minimum of the objects
class magari:
    def __init__(self, model, make, year):
        self.model=model
        self.make=make
        self.year=year
    def cars(self):
        print(f"This car is an {self.model} , {self.make} and year {self.year}.")
car1=magari("A-class","Mercedes-Benz","2022")
car1.cars()

cars2=magari("A3","Audi","2023,2022")
cars2.cars()

cars3=magari("A4","Honda","2023,2022")
cars3.cars()

class fruits:
    def __init__(amo, type, price, packagers):
        amo.type=type
        amo.price=packagers
        amo.packagers=price
    def matunda(amo):
        print(f"We are selling {amo.type} by {amo.packagers} for only {amo.price} a bag.")
f1=fruits("Apples","Manzanas LTD","Ksh. 120")
f1.matunda()

f2=fruits("Oranges","Naranjas Jugo","Ksh. 89")
f2.matunda()

f3=fruits("Grapes","Olives n Packs","Ksh. 145")
f3.matunda()