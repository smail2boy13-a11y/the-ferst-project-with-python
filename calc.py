import time 
import cmath

# add
def add():
    mane =list(map (float, input("Enter all valieu siparet by space: ").split()))
    time.sleep(2)
    print (sum(mane))
# subtractin 
def subtraction():
    num_1 = float(input("Enter the 1st number: "))
    num_2 = float(input("Enter the 2ed number: "))
    time.sleep(2)
    print(num_1 - num_2)

# multiplication 
def multiplication():
    num_1 = float(input("Enter the 1st number: "))
    num_2 = float(input("Enter the 2st number: "))
    time.sleep(2)
    print(num_1 * num_2)

def division():
    pol = float(input("Enter the number: "))
    div = float(input("Enter the diviser: "))
    time.sleep(2)
    print(pol / div)

def factoriell():
    fact = int(input("Enter the factoriel: "))
    res = 1
    for x in range(1,fact+1):
        res *=x
    time.sleep(2)
    print(res)

def Quadratic_equation():
    print("Enter the numbers in the form 'ax² + bx + c = 0")
    x1 = 0
    x2 = 0
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    if a!= 0 :
        delta = ((b**2) - 4*a*c)
        if delta == 0:
            x1 = (b / (2*a))
            return x1
        elif delta > 0:
            x1 = ((-b - cmath.sqrt(delta))/2*a)
            x2 = ((-b + cmath.sqrt(delta))/2*a)
            time.sleep(2)
            print(f"x1= {x1}, x2= {x2}")
        else :
            x1 = ((-b - cmath.sqrt(delta))/2*a)
            x2 = ((-b + cmath.sqrt(delta))/2*a)
            time.sleep(2)
            print(f"x1= {x1}, x2= {x2}")

while True:
    print ("Hollo in the calculater")
    print ("for additieon inter 1")
    print("for subtraction enter 2")
    print ("for multiplication enter 3")
    print ("for division enter 4")
    print("for factoriell enter 5")
    print ("for Quadratic_equation enter 6")
    print ("for exit enter 7")
    gg = int(input("Enter the type number: "))
    time.sleep(2)
    if gg == 1:
        add()
    elif gg == 2:
        subtraction()
    elif gg == 3:
        multiplication()
    elif gg == 4:
        division()
    elif gg == 5:
        factoriell()
    elif gg == 6:
        Quadratic_equation()
    elif gg == 7:
        break
    else :
        print("are you dumb !??")
    input ("clic enter to reset ...")

