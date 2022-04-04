#Formatting strings

brand = 'Apple'
exchangeRate = 1.235235245

message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)

print(message)

'''
We use the %s, %d and %4.f formatters as placeholders in the string

These placeholders will be repalced with the variable brand, the value 1299 and the variable
exchangeRate respectively, as indicated in the round brackets

>>The price of this Apple laptop is 1299 USD and the exchange rate is 1.24 USD to 1 EUR

The %s formatter is used to represent a string
While the %d formatter represents an integer

If we want to add spaces before an integer, we can add a number between % and d
to indicate the desired length of the string

For instance "%5d" % (123) will give us " 123"(with 2 spaces in front and a
total length of 5).
