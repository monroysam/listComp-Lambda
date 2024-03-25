remainder = lambda num: num % 2 #this will create the remainder as a function object
print(remainder(5))

product = lambda x, y: x * y #FINAL EXAM QUESTION (WHAT TYPE OF OBJECT IS PRODUCT: Funciton object)
print(product(2,3))
print(product(2,4))


def testfunc(num):
    return lambda x:x * num

result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9))

result10 = lambda x: x * 10
result100 = lambda x: x * 100

print(result10(9))
print(result100(9))