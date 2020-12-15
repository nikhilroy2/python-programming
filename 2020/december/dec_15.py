person = ["sonchoy", "nikhil", 'toslim']
num = [2,3,54,65,3,2]
fruit = ["mango", "banana", "apple", 'jackfruit']
person.extend(num)
person.extend(fruit)
person.remove("nikhil")
person.clear()
print(person)