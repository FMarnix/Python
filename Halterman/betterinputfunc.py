#   get_int_in_range(first, last)
#   Forces the user to enter an integer within a 
#   specified range 
#   first is either a minimun or maximun acceptable value 
#   last is the correspoding other end of the range,
#   either is a maximun or minimun values
#   return an acceptable value from the user
def get_int_in_range (first, last):
    #  If the largr number is provided first,
    #  switch the parameters
    if first  > last:
       first, last = last, first
    # insist on values in the range first...last
    in_value = int(input("Please enter values in the range " + str(first) + "..." + str(last) + ": "))
    while in_value < first or in_value > last:
        print(in_value," is not in the range",first, "..."< last)
        in_value = int(input("Please try again: "))
    #   in_value at this point is guarantee to be within range
    return in_value;

# main
#      Tests the get_in_range function
def main():
      print(get_int_in_range(10, 20))
      print(get_int_in_range(20, 10))
      print(get_int_in_range(5, 5))
      print(get_int_in_range(-100, 100))
      
main()     # run the program
