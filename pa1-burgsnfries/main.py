from PIL import Image, ImageDraw, ImageFont

# Dictionary to store ordered items and their quantities.
# For the time being, you don't need to worry about dictionaries but if you are curious feel
# free to look at the documentation: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
order = {}

def GenerateReceiptImage(receipt_text, filename="receipt.png"):
    """Generates an image with the receipt content and saves it."""
    # Create a blank image
    image = Image.new("RGB", (400, 600), "white")
    draw = ImageDraw.Draw(image)

    # Load font (default system font)
    font = ImageFont.load_default()

    # Define text position
    x, y = 20, 20

    # Draw the text on the image
    for line in receipt_text.split("\n"):
        draw.text((x, y), line, fill="black", font=font)
        y += 25  # Move down for the next line

    image.save(filename)
    print(f"Receipt saved as {filename}")

def AddItemToOrder(item, amount):
    """Adds an item and its quantity to the order."""
    order[item] = amount

def ModifyItem(list_ingredients):
    """Allows the user to add or remove ingredients from an item."""
    details = ""
    while True:
        print("Would you like to remove or add an ingredient?")
        print("1. Remove")
        print("2. Add")
        print("3. Exit")
        choice = int(input())  # User selects an option

        if choice == 3:
            break  # Exit the loop if the user chooses to stop modifying

        print(f"The ingredients are {list_ingredients}")
        ingredient = input("Which ingredient would you like to modify?\n").lower()

        if choice == 1:  # Remove ingredient
            details = RemoveIngredient(list_ingredients, details, ingredient)

        elif choice == 2:  # Add ingredient
            details = AddIngredient(list_ingredients, details, ingredient)
    return details  # Return modified ingredient details

def GetSubTotalIterator():
    """Calculates the subtotal of the order."""
    total = 0
    for item, amount in order.items():
        total = GetSubTotal(item, amount, total)  # Function assumed to calculate item subtotal

    print(f"Your subtotal is ${total}")
    return total

def Pay():
    """Calculates and displays the total cost of the order, including tax and tip."""
    print("Your receipt:")
    subtotal = GetSubTotalIterator()
    discount = 0
    if subtotal > 50:
        discount = 10
        print('Congrats! You have earned a $10 discount for being such a pleasureable client! Thanks, Come again.')
    elif subtotal > 25:
        discount = 5
        print('Congrats! You have earned a $5 discount for being such a pleasureable client! Thanks, Come again.')
        subtotal = subtotal - discount
    tip = AddTip(subtotal)
    tax = AddIVU(subtotal)
    total = subtotal + tip + tax



    receipt_text = "Jack’s Diner Receipt\n"
    receipt_text += "-" * 30 + "\n"
    for item, amount in order.items():
        receipt_text += f"{item} x{amount}\n"
    receipt_text += "-" * 30 + f"\nSubtotal: ${total:.2f}\n"
    receipt_text += "Thank you for dining with us!\n"

    print(receipt_text)

    GenerateReceiptImage(receipt_text)

    print(f"Your total is ${total:.2f}")
    print("Thank you for dining at Jack's Diner!")

def Main():
    """Handles the menu system and ordering process."""
    print("Welcome to Jack's Diner!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Order a burger")
        print("2. Order a side")
        print("3. Order a drink")
        print("4. Order a milkshake")
        print("5. Order a combo")
        print("6. Pay")
        menu = int(input())  # User selects an option from the menu

        if menu == 1:
            BurgerMenu()  # Function assumed to display burger options
        elif menu == 2:
            SidesMenu()  # Function assumed to display side options
        elif menu == 3:
            DrinksMenu()  # Function assumed to display drink options
        elif menu == 4:
            MilkshakesMenu()# Function assumed to display milkshake options
        elif menu == 5:
            ComboMenu() # New Function assumed to display combomune options
        elif menu == 6:
            print("\nYour final order:")
            for item, amount in order.items():
                print(f"{item} x{amount}")
            Pay()  # Proceed to payment
            break  # Exit the ordering system

def BurgerMenu():
    # TODO Task 1: Implement the burger menu selection logic. Display available burger options,
    #   show ingredients for each, and allow the user to modify the selected item.
    print('Which burger would you like to order?\n1. Hamburger\n2. BBQ Burger\n3. Cheeseburger')
    prefer = int(input())

    if prefer == 1:
        burger = 'Hamburger'
        ingredients = ['Bread','Beef Patty','Lettuce','Tomato','Cheese','Onions']
    elif prefer == 2:
        burger = 'BBQ Burger'
        ingredients = ['Bread','Beef Patty','BBQ Sauce','Caramelized Onions']
    elif prefer == 3:
        burger = 'Cheeseburger'
        ingredients = ['Bread','Beef Patty','Cheese','Pickles','Ketchup']
    print(f'{burger} comes with:')
    for ingredient in ingredients:
        print('-'+ ingredient)
    print('Would you like to remove an ingredient?\n1. Yes\n2. No')
    remove_choice = int(input())

    details = ''
    if remove_choice == 1:
        print(f'The ingredients are {ingredients}')
        ingredient_remove = input('Which ingredient would you like to remove?\n').strip().capitalize()

        if ingredient_remove in ingredients:
            print(f'Removing ingredient: {ingredient_remove}')
            details += 'No ' + ingredient_remove + ','
            ingredients.remove(ingredient_remove)
    else:
        print('Ingredient not found.')

    print('Would you like to add an ingredient?\n1. Yes\n2. No')
    add_choice = int(input())
    if add_choice == 1:
        print(f'The ingredients are {ingredients}')
        ingredient_add = input('Which ingredient would you like to add?\n')
        if ingredient_add in ingredients:
            print("Adding more ingredient: "+ ingredient_add)
            details += "More " + ingredient_add + ','
        else:
            print('Ingredient not found.')
    amount = int(input("How many would you like ?\n"))
    order[burger + " "+ details] = order.get(burger + " "+ details, 0) + amount


def SidesMenu():
    # TODO Task 2: Implement the sides menu selection logic. Allow the user to choose side items
    #   and ask for the quantity to add to the order.
    print('Which side would you like to order?\n1. Loaded Cheese Fries\n2. French Fries\n3. Onion Rings')
    menus = int(input())
    if menus == 1:
        side = 'Loaded Cheese Fries'
    elif menus == 2:
        side = 'French Fries'
    elif menus == 3:
        side = 'Onion Rings'
    else:
        print('Invalid choice.')
    amount = int(input('How many would you like ?\n'))
    AddItemToOrder(side,amount)


def DrinksMenu():
    # TODO Task 3: Implement the drinks menu selection logic. Display available drinks and call the appropriate
    #   menu function for each drink type.
    print('Which drink would you like to order?\n1. Soda\n2. Lemonade\n3. Coffee\n4. Water')
    choice_drink = int(input())
    if choice_drink == 1:
        drink = SodaMenu()
    elif choice_drink == 2:
        drink = LemonadeMenu()
    elif choice_drink == 3:
        drink = CoffeeMenu()
    elif choice_drink == 4:
        drink = 'Water'
    amount = int(input(f'How many {drink} would you like ?'))
    AddItemToOrder(drink, amount)


def SodaMenu():
    # TODO Task 3: Implement the soda menu selection logic. Allow the user to choose a soda type
    #   and return the selected item.
    print('Which soda would you like?\n1. Cola\n2. Sprite\n3. Root Beer')
    dif_soda = int(input())
    if dif_soda == 1:
        return 'Cola'
    elif dif_soda == 2:
        return 'Sprite'
    elif dif_soda == 3:
        return 'Root Beer'


def LemonadeMenu():
    # TODO Task 1: Implement the lemonade menu selection logic. Allow the user to choose a lemonade flavor
    #   and return the selected item.
    print('Which lemonade would you like?\n1. Classic Lemonade\n2. Strawberry Lemonade\n3. Peach Lemonade')
    dif_lemon = int(input())
    if dif_lemon == 1:
        return 'Classic Lemonade'
    elif dif_lemon == 2:
        return 'Strawberry Lemonade'
    elif dif_lemon == 3:
        return 'Peach Lemonade'
    pass

def CoffeeMenu():
    # TODO Task 3:: Implement the coffee menu selection logic. Allow the user to choose a coffee type
    #   and return the selected item.
    print('Which coffee would you like?\n1. Black Coffee\n2. Latte\n3. Cappuccino')
    dif_coffee= int(input())
    if dif_coffee == 1:
        return 'Black Coffee'
    elif dif_coffee == 2:
        return 'Latte'
    elif dif_coffee == 3:
        return 'Cappuccino'

    pass

def MilkshakesMenu():
    # TODO Task 4:: Implement the milkshakes menu selection logic. Allow the user to choose a milkshake flavor
    #   and return the selected item.
    print('WHich milkshake flavor would you like ?\n1. Vanilla\n2. Strawberry\n3. Chocolate')
    choice_milkshake = int(input())
    if choice_milkshake == 1:
        milkshake = 'Vanilla Milkshake'
    elif choice_milkshake == 2:
        milkshake = 'Strawberry Milkshake'
    elif choice_milkshake == 3:
        milkshake = 'Chocolate Milkshake'
    amount = int(input(f'How many {milkshake} would you like ?'))
    AddItemToOrder(milkshake, amount)

    pass

def ComboMenu():
    print("Which combo would you like?")
    print("1. Hamburger + Fries + Soda")
    print("2. BBQ Burger + Fries + Soda")
    print("3. Cheeseburger + Fries + Soda")
    combo_choice = int(input())

    if combo_choice == 1:
        combo = "Hamburger + Fries + Soda"
    elif combo_choice == 2:
        combo = "BBQ Burger + Fries + Soda"
    elif combo_choice == 3:
        combo = "Cheeseburger + Fries + Soda"
    else:
        print("Invalid choice.")
        return
    amount = int(input("How many would you like?\n"))
    order[combo] = order.get(combo, 0) + amount

def GetSubTotal(item, amount, total):
    # TODO Task 5: Complete the logic for calculating the subtotal of the order.
    #   You should calculate the price based on the item, and update the total accordingly.
    #   Add the price calculation logic for various items and print the item details.
    if "+" in item:
        if "Hamburger" in item:
            price = 12
        elif "BBQ Burger" in item:
            price = 14
        elif "Cheeseburger" in item:
            price = 10
    else:
        if 'Hamburger' in item:
            price = 8
        elif 'BBQ Burger' in item:
            price = 10
        elif 'Cheeseburger' in item:
            price = 9
        elif "Loaded Cheese Fries" in item:
            price = 5
        elif "French Fries" in item:
            price = 3
        elif "Onion Rings" in item:
            price = 3
        elif "Soda" in item:
            price = 2
        elif "Lemonade" in item:
            price = 3
        elif "Coffee" in item:
            price = 4
        elif "Water" in item:
            price = 1
        elif "Milkshake" in item:
            price = 6
        else:
            price = 0

    item_prices = price * amount
    print(item, "x", amount, " $", item_prices, ".00")
    total += item_prices

    return total
    # if "+" in item:
    #     if "Hamburger" in item:
    #         price = 12
    #     elif "BBQ Burger" in item:
    #         price = 14
    #     elif "Cheeseburger" in item:
    #         price = 10
    # else:
    #     if 'Hamburger' in item:
    #         price = 8
    #     elif 'BBQ Burger' in item:
    #         price = 10
    #     elif 'Cheeseburger' in item:
    #         price = 9
    # # if item == "Hamburger + Fries + Soda":
    # #     price = 12
    # # elif item == "BBQ Burger + Fries + Soda":
    # #     price = 14
    # # elif item == "Cheeseburger + Fries + Soda":
    # #     price = 10
    # # elif "Burger" in item:
    # #     price = 8
    #     elif "Loaded Cheese Fries" in item:
    #         price = 5
    #     elif "French Fries" in item:
    #         price = 3
    #     elif "Onion Rings" in item:
    #         price = 3
    #     elif "Soda" in item:
    #         price = 2
    #     elif "Lemonade" in item:
    #         price = 3
    #     elif "Coffee" in item:
    #         price = 4
    #     elif "Water" in item:
    #         price = 1
    #     elif "Milkshake" in item:
    #         price = 6
    #     else:
    #         price = 0
    #
    #     item_prices = price * amount
    #     print(item, "x", amount, " $", item_prices, ".00")
    #     total += item_prices
    #     return total


def AddTip(total):
    # TODO Task 6: Implement the logic for adding a tip based on user input.
    #   The user should choose between 10%, 15%, or 20% or 'No' tip.
    #   Calculate the tip and return the updated total.
    print("Would you like to leave a tip?")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    print("4. No")
    tips = int(input())
    if tips == 1:
        tip = total * 0.10
    elif tips == 2:
        tip = total * 0.15
    elif tips == 3:
        tip = total * 0.20
    elif tips == 4:
        tip = 0
    print("Tip: $" + str(round(tip, 2)))
    return tip

def AddIVU(total):
    # TODO Task 7: Implement the logic for adding IVU (tax) to the total.
    #   The IVU rate is 11.5%. Return the updated total.
    tax = total * 0.115
    print("IVU: $" + str(round(tax, 2)))
    return tax

def RemoveIngredient(list_ingredients, details, ingredient):
    # TODO Task 8: Implement logic to check if the ingredient exists in list_ingredients,
    #   update details accordingly, and print the appropriate message.
    if ingredient in list_ingredients:
        print("Removing ingredient:" + ingredient)
        details += "No " + ingredient + ","
    else:
        print("Ingredient not found.")
    return details

def AddIngredient(list_ingredients, details, ingredient):
    # TODO Task 8: Implement logic to check if the ingredient exists in list_ingredients,
    #   update details accordingly, and print the appropriate message.
    if ingredient in list_ingredients:
        print("Adding more ingredient:" + ingredient)
        details += "More " + ingredient + ","
    else:
        print("Ingredient not found.")
    return details


Main()