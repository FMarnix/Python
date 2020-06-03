# Number of cars available
cars = 100
# Space available in each car 
space_in_a_car = 4.0
# the total number of drivers 
drivers = 30
# the total number of passengers
passengers = 90
# the cars that not be driven because the lack of drivers
cars_not_driven = cars - drivers
# the number of cars that will be driven
cars_driven = drivers
# the carpool capacity available 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
