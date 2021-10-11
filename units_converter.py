from currency_converter import CurrencyConverter

c = CurrencyConverter()

while True:
    try:
        value = float(input('USD-RUB converter, enter the number value: '))
    except ValueError:
        print('Invalid inputs, please, try again!')
    else:
        break

print(c.convert(value, 'USD', 'RUB'))

# Here is some conflict
