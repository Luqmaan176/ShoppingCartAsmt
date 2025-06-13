'''This is Version 3 of my easygui shopping cart program. I have made changes based on stakeholder feedback, and have also added a 'Remove Item' function.'''

#Importing easygui
import easygui

#Declaring constants
price_of_apples = 0
price_of_bananas = 0
price_of_tomatos = 0

#Asking the user if they want to use the program
start = easygui.buttonbox('Would you like to use this program?', choices = ['Yes', 'No'])

#If the user does not want to use the program
if start == 'No':
    easygui.msgbox('Thank you. Please come again.')

#If the user does want to use the program
elif start == 'Yes':
    easygui.msgbox('Thank you for choosing Auckland Shopping Mart!')

    while True:
        #Printing all the user's available options
        options = easygui.buttonbox("What would you like to do? If you are done, click 'I'm done' to finalize your transaction. ", choices = ['Apples for $2.40/kg', 'Bananas for $3.00/kg', 'Tomatos for $3.90/kg', 'Remove Item', "I'm done"])

        #If the user wants to buy an apple
        if options == 'Apples for $2.40/kg':
            enter_apples = easygui.enterbox('How many kilos of apples would you like to buy?')
            num_of_apples = float(enter_apples)
            price_of_apples = num_of_apples*2.4
            easygui.msgbox(f'The price of your apples is ${price_of_apples:.2f}')

        #If the user wants to buy a banana
        elif options == 'Bananas for $3.00/kg':
            enter_bananas = easygui.enterbox('How many kilos of bananas would you like to buy?')
            num_of_bananas = float(enter_bananas)
            price_of_bananas = num_of_bananas*3
            easygui.msgbox(f'The price of your bananas is ${price_of_bananas:.2f}.')

        #If the user wants to buy a tomato        
        elif options == 'Tomatos for $3.90/kg':
            enter_tomatos = easygui.enterbox('How many kilos of tomatos would you like to buy?')
            num_of_tomatos = float(enter_tomatos)
            price_of_tomatos = num_of_tomatos*3.9
            easygui.msgbox(f'The price of your tomatos is ${price_of_tomatos:.2f}.')

        #If the user wants to remove an item.
        elif options == 'Remove Item':
            remove_item = easygui.buttonbox('Which item would you like to remove?', choices = ['Apple', 'Banana', 'Tomato'])

            #If the user wants to remove an item, the program will ask how many they want to remove, and then calculate the new price of the item.
            if remove_item == 'Apple':
                while True:
                    num_remove_apple = easygui.integerbox('How many kilos of apples would you like to remove?')
                    if num_remove_apple > num_of_apples:
                        easygui.msgbox('The number you wish to remove is greater than the amount you wish to purchase.')
                    else:
                        break
                price_of_apples = price_of_apples - (num_remove_apple*2.4)
                easygui.msgbox(f'The new price of your apples is ${price_of_apples:.2f}.')

            elif remove_item == 'Banana':
                while True:
                    num_remove_banana = easygui.integerbox('How many kilos of bananas would you like to remove?')
                    if num_remove_banana > num_of_bananas:
                        easygui.msgbox('The number you wish to remove is greater than the amount you wish to purchase.')
                    else:
                        break
                price_of_bananas = price_of_bananas - (num_remove_banana*3)
                easygui.msgbox(f'The new price of your bananas is ${price_of_bananas:.2f}.')

            elif remove_item == 'Tomato':
                while True:
                    num_remove_tomato = easygui.integerbox('How many kilos of tomatos would you like to remove?')
                    if num_remove_tomato > num_of_tomatos:
                        easygui.msgbox('The number you wish to remove is greater than the amount you wish to purchase.')
                    else:
                        break
                price_of_tomatos = price_of_tomatos - (num_remove_tomato*3.9)
                easygui.msgbox(f'The new price of your tomatos is ${price_of_tomatos:.2f}.')

        #If the user is finished shopping.
        elif options == "I'm done":
            #Telling the user the total price.
            easygui.msgbox('----------TOTAL PRICE----------')
            easygui.msgbox(f'The price of your apples is ${price_of_apples:.2f}.')
            easygui.msgbox(f'The price of your bananas is ${price_of_bananas:.2f}.')
            easygui.msgbox(f'The price of your tomatos is ${price_of_tomatos:.2f}.')
            #Calculating the total price.
            total_price = price_of_apples+price_of_bananas+price_of_tomatos
            easygui.msgbox(f'Your total price is ${total_price}')
            while True:
                #Getting the user to pay for the items.
                payment = easygui.enterbox(f'Please pay by entering the total price')
                decimal = float(payment)
                #If the amount payed is less than needed.
                if decimal < total_price:
                    easygui.msgbox('This amount is smaller than your total price. Please enter the price again.')

                #If the amount payed is greater than or equal to what is needed.
                elif decimal >= total_price:
                    #Calculating the remainder.
                    remainder = decimal-total_price
                    #Printing a thank you message, and giving the user their remainder.
                    easygui.msgbox(f'Thank you for paying. Your remainder is ${remainder}. Please come again.')
                    break

            break
        
