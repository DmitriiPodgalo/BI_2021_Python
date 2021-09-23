from currency_converter import CurrencyConverter

c = CurrencyConverter()

while True:
    try:
        value = float(input('RUB-USD converter, please, enter the number value: '))
    except ValueError:
        print('Invalid inputs, please, try again!')
    except:
        print('Unknown error, please, try again!')
    else:
        break

print(c.convert(value, 'RUB', 'USD'))

# Something will be there.
# The second line.
