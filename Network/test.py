#tests

def f(x):
    return {
        'a': 1,
        'b': 2,
        'hej':5, 

    }.get(x, 9) 

def doSomething():
	print "YaY"
	


def b(x):
    {
        'a': 1,
        'hej': doSomething(),
    }.get(x, 9) 

def c(x):
    {
        'a': 1,
        'hej': doSomething(),
    }.get(x.split[0], 9) 


text = "hej 1234"
#print text
print text.split()[0]
#b(text.split()[0])
c(text)


