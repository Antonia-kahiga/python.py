# to create a function use "def" the call that functon...

def hello():
    print("This is my first function.")
hello()
hello()

#calculate function
def calculate():
    x = 5
    y = 10
    print(x * y)
calculate()


# placing " " only puts a space b2n your words...
def names(fname, lname):
    print(fname + " " + lname)
names("Antonia", "Kahiga")
names("Jesse", "Walter")
names("Michael B", "Jordan")


def greetings(name, greeting="Hello"):
    print(greeting + " " + name)
greetings("Antonia")
greetings("Joan", "niaje")


def course(course, points="44.57"):
    print(points + " " + course)
course("You qualify for architecture")

#to get the max value in a certain number of variables...
def maxvalue(a, b, c, d, e, f):
    return max(a, b, c, d, e, f)
result = maxvalue(7, 9, 1, 8, 17, 45)
print(result)

#function to get minimum value...
def minvalue(g, h, i, j, k, l, m):
    return min(g, h, i, j, k, l, m)
result = minvalue(20, 196, 5, 15, 2, -196, -5)
print(result)

#function to sort number in a list...
def sort_list(list):
    return sorted(list)
answer=sort_list([3,9,0,2,7,1,5,4,2])
print(answer)

#function to print out numbers in a range...
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(5)