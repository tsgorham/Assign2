"""
Envelope  print
"""

BORDER = f'+{"":->50}+'
STAMP = f'|{"#### |":>51}'
SPACER = f'|{"|":>51}'

EDGE = f'{"|":20}'

ADDRESS_1 = 'George Costanza'
ADDRESS_2 = '1234 Fake St'
ADDRESS_3 = 'Del Boca Vista, FL, 90210'

ADDRESS_1 = 'George Costanza'
ADDRESS_2 = '1234 Fake St'
ADDRESS_3 = 'Del Boca Vista, FL, 90210'

print(BORDER)
print(STAMP)
print(STAMP)
print(STAMP)
print(SPACER)

print(f'{EDGE}{ADDRESS_1:<31}|')
print(f'{EDGE}{ADDRESS_2:<31}|')
print(f'{EDGE}{ADDRESS_3:<31}|')

print(SPACER)
print(BORDER)
