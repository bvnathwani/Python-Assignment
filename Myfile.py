a = [3.14,'cat',11,'cat','True']
print(a.index('cat'))
a.append(99)
print(a)
a.remove("cat")
print(a)
b = (42,)
print(b)

spam ={"cat":100,"dog":200}
print(spam.values())
print("cat" in spam)
print(spam.keys())

if "color" not in spam:
    spam["color"] ="black"

print(spam)


spam["name"] = "black"
print(spam)
spam.setdefault('check','black')

s = "Hello"
print(s.upper())
print(s.upper().isupper())
print(s.upper().lower())
print(s)








