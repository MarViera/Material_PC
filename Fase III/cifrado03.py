def crack_cesar(cifrado):
    print(f"Texto cifrado: {cifrado}\n")
    for desp in range(26):
        intento = ""
        for c in cifrado:
            if c.isalpha():
                if c.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                intento += chr((ord(c) - base - desp) % 26 + base)
            else:
                intento += c
        print(f"  Desp {desp:2d}: {intento}")

crack_cesar("Khoor Pxqgr Vhfuhwr")
