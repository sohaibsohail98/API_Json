#import json
#create a class exchange_rates
#with required attributes
# fetch the data from exchange_rates.json
#display the data
#display the type of the data
#display exchange rates with specific currencies
# method to return the exchange rates



import json
class Exchange_Rates:

        def __init__(self):
            #This opens the exchange_rates file and assign it to a alias
            with open("exchange_rates.json", "r") as exchange_files:
                data = json.load(exchange_files) #Creating a variable and loading the json file
                for e in data: #
                    if e == "rate":
                        print(data["rate"])

                print(data)
                currency = input("What currency would you like the exchange rate of, please see list.\n") # /n is for next line to add input
#             display exchange rates with specific currencies
                print(data["rates"][currency])
#
#
e = Exchange_Rates
e.__init__(Exchange_Rates)

