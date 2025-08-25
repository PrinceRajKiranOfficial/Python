#GLobal scope
sname = "Prince Raj Kiran"
def hi():#function creation
    #Local scope
    print(sname)

hi()#function call
print(sname)

def hello():
    age = 20  # local scope
    print(age)

hello()
# print(age)


name = "Prince Raj Kiran" #global scope 
print (type(name))

b = True #boolean
print(type(b))

c = 5 #int
print(type(c))

d = 5.5 #float
print(type(d))

e = 5 + 3j  #complex number
print(type(e))


