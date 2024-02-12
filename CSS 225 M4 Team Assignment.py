print("choose what to eat for lunch:")
print("1. Burger")
print("2. Pizza")
print("3. Sliders")
print("4. Fries")
print("5. Steak")
print("0. Exit")

option = input("What would you like to eat: ?")
Burger = "1"
Pizza = "2"
Slider = "3"
Fries = "4"
Steak = "5"
Exit = "0"

if option == "1":
    print("You have selected a Burger! How would you like that cooked?")
elif option == "2":
    print("You have selected pizza! What toppings would you like?")
elif option == "3":
    print("You have selected sliders! how many would you like?")
elif option == "4":
    print("You have ordered Fries!")
elif option == "5":
    print("You have ordered a steak! How would you like it cooked?")
elif option == "0":
    print("Glad you came! Come again!")
else:
    print("That's not on the menu!")

    
