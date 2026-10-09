import unicodedata
from codecs_to_hex import to_hex

#text = 'français'

text = 'áàäâÁÀÄÂ'

#text = 'Hola mundo!'

print('Raw   : {!r}'.format(text))
for c in text:
    print('  {!r}: {}'.format(c, unicodedata.name(c))) #\' \'
input()
print('UTF-8 : {!r}'.format(to_hex(text.encode('utf-8'), 1)))#encode: str --> byte
print('UTF-16: {!r}'.format(to_hex(text.encode('utf-16'), 2)))
