l = lambda a,b: a+b

#print(l(10,10))

g = "Hello World"

def World(*args, **kwargs):
    a = args[1]
    b = kwargs.pop({"a": 3})
    return b


#print(World(3,4,{"a": 3,"b":3})) 

def Local():
    a = "I am local"
    def Lo():
        nonlocal a
        a+= "\nHei"
        def Cal():
            nonlocal a
            a+="\nFriend"
        Cal()
    Lo()
    return a

#print(Local())

# dunders int
class Dun():
    def __int__(self):
        print("HelloW")
    def user(name):
        print(name)


class greetings():
    def __int__(self):
        print("Hellow")
    def user(name):
        print(name)
new_user = greetings()
new_user