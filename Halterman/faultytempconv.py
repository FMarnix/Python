# File faultytempconv.py

#Establish some variables
 degreesF = 0
 degreesC = 0
# Define the relationships between F and C
degreesC = 5/9*(degreesF -32)
#Prompt user for degreesF
degreesF = eval(input('Enter the temperature in degrees F: '))
#Report the result
    print(degreesF, " degrees F = ", degreesC, 'degrees C')