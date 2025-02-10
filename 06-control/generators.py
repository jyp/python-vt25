
# while True or False:
# while False:
#     ...
# while True:
#     ...

def g():
    print("About to yield one")
    yield 1
    print("About to yield two")
    yield 2
    print("About to yield three")
    yield 3
    # return 234

print(g())
for i in g():
    print (i)
