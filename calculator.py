#BUILDING A CALCULATOR
import re
print("CALCULATOR")
print("type 'quit' to exit \n")
previous =0
run=True

def solve():
    global previous
    global run
    if previous==0:
        equation=input("enter your equation")
    else:
        equation=input(str(previous))
    if equation=='quit':
        print("Thanks for using this calculator.See you later ")
        run=False
    else:
        equation=re.sub('[a-zA-Z:,(){}" "]','',equation)
        if previous==0:
            previous=eval(equation)
            print("your result is=",previous)
        else:
            previous=eval(str(previous)+equation)
            print("your result is=",previous)
    

while(run):
    solve()
    
