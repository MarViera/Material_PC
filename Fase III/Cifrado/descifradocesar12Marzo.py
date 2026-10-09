message = input('Ingresa el mensaje: ')
espacios = 1
while espacios > 0:
    clave = input('Ingresa tu palabra clave para cifrar: ')
    espacios = clave.count(' ')
    if clave.isalpha() == False:
        espacios += 1
key = len(clave)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''
for symbol in message: #message está en texto claro
    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex - key

        #print(translatedIndex)
        
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

print(translated)

