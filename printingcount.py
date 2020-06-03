# This function gives us the total amount of the number of copies
def amount(x, y):
      return x * y 
      
# This function adds extra services
def extra(z):
      return z 


print("Select operation")
print("1.Copy black and white")
print("2.Copy color")
print("3.Copy black and white and biding")
print("4.Copy color and biding")

 # Take input for the user
choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter number of copies: "))
num2 = 0.02
num3 = 0.15
num4 = 2.50
 
if choice == '1':
    print(amount(num1, num2))
    
elif choice == '2':
     print(amount(num1, num3))
     
elif choice ==' 3':
    print(amount(num1,num2) + num4)
    
elif choice == '4':
    print(amount(num1,num3) + num4)
    
else:
    print("Thank you for  your preference we hope to make business in the future")
