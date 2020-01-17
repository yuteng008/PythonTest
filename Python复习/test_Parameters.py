
a = 9
def change():
    # a = 90
    global a
    print(a)
    a = 100

print(a)
change()
print(a)