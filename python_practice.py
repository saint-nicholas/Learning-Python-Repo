#This program is meant to greet a customer, and take their order
print("Hello there !!!!!") #Greeting

name = input("What is your name?\n") #Getting the customer's name

print("Hello there " + name + ". Welcome to the coffee shop") #Welcoming the customer using their name

menu = "Coffee, Lattes, Croissants, Bagels and Eggs" #Assigning the daily menu items

print("Today we have " + menu) #Relaying the available menu items to the customer

order = input("What would you like to order?\n") #Getting the customer's order

print("Ok " + name + " you ordered " + order + "\nWe'll have that right out for you!") #Confirming that the customer's order has been submitted