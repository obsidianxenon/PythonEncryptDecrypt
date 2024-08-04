import time
print("Welcome")
time.sleep(1.5)
print("Encryption software")
time.sleep(1.5)
pref = input("Encrypt or Decrypt (e/d): ")

if (pref) == "e":
    letterin = input("Message: ")
    keyin = input("Key: ")

    def rotate(message, key):
        key = int(keyin)
        new = ""
        if (key) > 26:
            while (key) > 26:
                key = key - 1
        elif (key) < 0:
            while (key) < 0:
                key = key + 1
        numkey = key % 10

        for letter in message:
            if letter.islower():
                changed = ord(letter) + int(key)
                if (changed) > ord("z"):

                    changed = changed - 26
                if (changed) < ord("a"):
                    changed = changed + 26
                new = new + chr(changed)

            elif letter.isupper():
                changed = ord(letter) + int(key)
                if (changed) > ord("Z"):
                    changed = changed - 26
                if (changed) < ord("A"):
                    changed = changed + 26
                new = new + chr(changed)

            elif letter.isdigit():
                changed = ord(letter) + int(numkey)
                if (changed) < ord("0"):
                    changed = changed + 10
                if (changed) > ord("9"):
                    changed = changed - 10
                new = new + chr(changed)

            else:
                new = new + letter

        return new
    
    new = rotate(letterin, keyin)
    print(new)

elif (pref) == "d":
    message = input("Encrypted Message: ")
    key = input("Key: ")
    out = ""
    numkey = int(key) % 10

    for letter in message:
        if int(key) > 26:
            while int(key) > 26:
                key = int(key) - 1

        elif int(key) < 0:
            while int(key) < 0:
                key = int(key) + 1
        

        if letter.islower():
            decoded = ord(letter) - int(key)
            if decoded > ord("z"):
                decoded = decoded - 26
            if decoded < ord("a"):
                decoded = decoded + 26
            out = out + chr(decoded)

        elif letter.isupper():
            decoded = ord(letter) - int(key)
            if decoded > ord("Z"):
                decoded = decoded - 26
            if decoded < ord("A"):
                decoded = decoded + 26
            out = out + chr(decoded)

        elif letter.isdigit():
            decoded = ord(letter) - int(numkey)
            if decoded < ord("0"):
                decoded = decoded + 10
            if decoded > ord("9"):
                decoded = decoded - 10

            out = out + chr(decoded)

        else:
            out = out + letter

    print(out)