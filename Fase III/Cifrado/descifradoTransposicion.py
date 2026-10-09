# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math

def main():
    myMessage = input('Ingresa el mensaje cifrado: ')
    espacios = 1
    while espacios > 0:
        clave = input('Ingresa tu palabra clave: ')
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    myKey = len(clave)

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to next column.

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
            #print("Iteración",row,": ",plaintext)

    return ''.join(plaintext)


# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
