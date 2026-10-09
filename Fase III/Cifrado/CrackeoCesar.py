# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# LspeAqyrhsAqyrhmep
# NuF BF8F CFmnFxl34k1nFn2FnuFlxwp1n2xmnF2np41rmjm,Fn23áwF3xmx2Frw5r3jmx2GFernwnwF2x1y1n2j2GGG
message = input('Ingresa el mensaje: ')
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key:
for key in range(1,len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is almost the same as the original program:

    # Loop through each symbol in `message`:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wrap-around:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
