#This program is meant to greet a customer, and take their order
print("Hello there !!!!!") #Greeting

name = input("What is your name?\n") #Getting the customer's name

print("Hello there " + name + ". Welcome to the coffee shop") #Welcoming the customer using their name

menu = "Coffee, Lattes, Croissants, Bagels and Eggs" #Assigning the daily menu items

print("Today we have " + menu) #Relaying the available menu items to the customer

order = input("What would you like to order?\n") #Getting the customer's order

price = 7 #assigning the same price to all menu items for the sake of simplicity

number_of_items = input("How many " + order + "s would you like?\n") #asking the customer how many items they would like

total = int(number_of_items) * price #calculating the total price based on the number of items ordered

print("Ok " + name + " you ordered " + number_of_items + " " + order + "s. Your total is going to come to $" + str(total) + ".\nWe'll have that right out for you!") #Confirming that the customer's order has been submitted and giving them their total



