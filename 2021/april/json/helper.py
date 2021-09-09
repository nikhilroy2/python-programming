import json

data = open('my_text.txt',  "w")
data.write(" Are you hello?")
data.close()


result = open('my_text.txt', 'r')

print(result.read())