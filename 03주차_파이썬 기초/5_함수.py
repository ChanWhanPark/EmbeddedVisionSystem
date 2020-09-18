def firstTime():
    print("파이썬 처음 아닌데;;")

firstTime()
firstTime()

def chat(name1, name2, time1):
    print("%s야 지금 몇시니?" % name1)
    print("%d시야 %s야" % (time1, name2))

chat("준수", "찬환", 11)

def sum(a, b):
    return a+b

x = sum(1, 2)
print(x)