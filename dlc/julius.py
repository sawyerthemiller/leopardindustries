import os

os.system('cls' if os.name == 'nt' else 'clear')
run = "y"
while str(run) == "y" :
    print ("Welcome to Julius")
    print ("by Leopard Industries")
    print()
    key = input("Shift value (ignored for bruteforce)? ")
    oper = input("Do you want to (e)ncode, (d)ecode, or (b)ruteforce? ")

    if oper == "e" :
        
        plaintext = input("Plaintext? ")
        plaintext = plaintext.upper()
        
        encList = []
        
        for char in plaintext:
            asciiNum = ord(char)
            if asciiNum < ord('A') or asciiNum > ord('Z'):
                encList.append(char)
            else:
                asciiNum = asciiNum + int(key)
                if asciiNum > ord('Z'):
                    asciiNum = asciiNum - 26
                text = chr(asciiNum)
                encList.append(text)
                
        encrypted = ''.join(encList)
        print()
        encrypted = encrypted.lower()
        print (encrypted)
        print ()
        
    elif oper == "d":
        
        ciphertext = input("Ciphertext? ")
        ciphertext = ciphertext.upper()
        
        decList = []
        
        for char in ciphertext:
            asciiNum= ord(char)
            if asciiNum < ord('A') or asciiNum > ord('Z'):
                decList.append(char)
            else:
                asciiNum = asciiNum - int(key)
                if asciiNum < ord('A'):
                    asciiNum = asciiNum + 26
                text = chr(asciiNum)
                decList.append(text)
                
        decrypted = ''.join(decList)
        print()
        decrypted = decrypted.lower()
        print(decrypted)
        print ()
        
    elif oper == "b" :

        ciphertext = input("Ciphertext? ")
        print()
        ciphertext = ciphertext.upper()
        print("Results displayed below.")
        print()
        
        decList = []
        
        key = 0
        
        key
        while int(key) <= 25 :
            key = int(key) + 1
            for char in ciphertext:
                asciiNum= ord(char)
                if asciiNum < ord('A') or asciiNum > ord('Z'):
                    decList.append(char)
                else:
                    asciiNum = asciiNum - int(key)
                    if asciiNum < ord('A'):
                        asciiNum = asciiNum + 26
                    text = chr(asciiNum)
                    decList.append(text)
                    
            decrypted = ''.join(decList)
            decrypted = decrypted.lower()
            print("(" + str(key) + ") " + decrypted)
            print()
            decList = []
        print()
    run = input ("Again y/n? ")
    os.system('cls' if os.name == 'nt' else 'clear')



