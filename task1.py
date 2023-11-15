def func():
    x=20
    print(x)
func()
##it is localvariable
x=20
def func():
    x=40
    print(x)##it is decleare first
func()
print(x)##it is genrate after the function
##global x
x=20
def func():
    global x
    x=40
    print(x)
func()
print(x)
