'''This is Version 2 of my simple shopping cart system. I have made changes based on the recommendations made by the stakeholders.
easygui has been added to it, and some inputs have been changed to buttonboxes.'''

#Importing easygui
import easygui

#Declaring the constants. These are what will be used to calculate the price of each item
total_price = 0
price_of_tomatoes = 0
price_of_bananas = 0
price_of_apples = 0

#A dictionary of the items and their prices. This will be used to display the prices of the items.
price_of_items = {'Tomatoes':3.90, 'Banana':3.00, 'Apple': 2.40}

#Creating a while loop so that invalid answers are caught.
while True:
    
    #Asking the user if they want to use the program. Buttonbox is used because it is unlikely for invalid answers to get through.
    start = easygui.buttonbox('Would you like to use this program: ', choices = ['Yes', 'No'])

    #If the user does not want to use the program
    if start.lower() == 'no': 
        easygui.msgbox('Thank you. Please come again.')
        break

    #If the user does want to use the program
    elif start.lower() == 'yes':
        easygui.msgbox('Thank you for choosing us.')

        #Creating a while loop so that invalid answers are caught
        while True:

            #Listing the prices
            purchase = easygui.buttonbox("What would you like to buy? If you are done shopping, click I'm done to finalize your transaction", choices = ['Banana for $3.00', 'Tomato for $3.90', 'Apple for $2.40', "I'm done"])

            #If the user wants to buy tomatoes
            if purchase == 'Tomato for $3.90':
                #Asking the user how many tomatoes they want to buy.
                while True:
                    try:
                        amount_of_tomatoes = easygui.integerbox('How many tomatoes do you want to buy: ')
                    except ValueError:
                        easygui.msgbox('Please only enter numbers.')
                        continue
                    break
                #Calculating the price of the tomatoes
                price_of_tomatoes = amount_of_tomatoes*3.9
                #Telling the user the price of the tomatoes
                easygui.msgbox(f'The price of your tomatoes is ${price_of_tomatoes}')

            #If the user wants to buy apples
            elif purchase == 'Apple for $2.40':
                #Asking the user how many apples they want to buy.
                while True:
                    try:
                        amount_of_apples = easygui.integerbox('How many apples do you want to buy: ')
                    except ValueError:
                        easygui.msgbox('Please only enter numbers.')
                        continue
                    break
                #Calculating the price of the apples
                price_of_apples = amount_of_apples*2.4
                #Telling the user the price of the apples
                easygui.msgbox(f'The price of your apples is ${price_of_apples}')

            #If the user wants to buy bananas
            elif purchase == 'Banana for $3.00':
                #Asking the user how many bananas they want to buy.
                while True:
                    try:
                        amount_of_bananas = easygui.integerbox('How many bananas do you want to buy: ')
                    except ValueError:
                        print('Please only enter numbers.')
                        continue
                    break
                #Calculating the price of the bananas
                price_of_bananas = amount_of_bananas*3
                #Telling the user the price of the bananas
                easygui.msgbox(f'The price of your bananas is ${price_of_bananas}')

            #If the user is finished shopping:
            elif purchase == "I'm done":
                #Calculating the total price
                total_price = price_of_apples+price_of_bananas+price_of_tomatoes
                #Telling the user the total price
                easygui.msgbox('----------TOTAL PRICE----------')
                easygui.msgbox(f'Price of apples: ${price_of_apples}')
                easygui.msgbox(f'Price of bananas: ${price_of_bananas}')
                easygui.msgbox(f'Price of tomatoes: ${price_of_tomatoes}')
                easygui.msgbox(f'Total price: ${total_price}')
                easygui.msgbox('THANK YOU FOR SHOPPING WITH US!')
                break

        break
        

                
    
    #If the user enters anything else        
    else:
        easygui.msgbox('This is not a valid answer. Please answer only with Yes or No.')

    
