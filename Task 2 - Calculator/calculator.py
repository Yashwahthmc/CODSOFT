def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error! Division by zero."
    return x/y
def modulus(x,y):
    return x%y
def power(x,y):
    return x**y
print("Welcome to Yashwanth's Calculator!")
print("Select operation:")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\n6.Power\n7.Exit")
while True:
    choice=input("\nEnter choice(1/2/3/4/5/6/7):")
    if choice=='7':
        print("Thank you for using the calculator!")
        break
    if choice in ['1','2','3','4','5','6']:
        try:
            n1 = float(input("Enter first number:"))
            n2=float(input("Enter second number:"))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
        if choice=='1':
            print("Result:",add(n1,n2))
        elif choice=='2':
            print("Result:",subtract(n1,n2))
        elif choice=='3':
            print("Result:",multiply(n1,n2))
        elif choice=='4':
            print("Result:",divide(n1,n2))
        elif choice=='5':
            print("Result:",modulus(n1,n2))
        elif choice=='6':
            print("Result:",power(n1,n2))
    else:
        print("Invalid choice. Try again.")
