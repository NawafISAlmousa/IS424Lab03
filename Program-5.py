def hello_Dec(h):

    def wrapper():
        x= int(input("Enter a number of repetitions: "))
        for i in range(x):
            h()
    return wrapper
@hello_Dec
def hello():
   print ('Hello')
hello()