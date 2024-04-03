message = input("Encrypted Message: ")
key = int(input("Key: "))
out = ""

for letter in message:
    if int(key) > 26:
        while int(key) > 26:
            key = int(key) - 1

    elif int(key) < 0:
        while (key) < 0:
            key = int(key) + 1

    numkey = key % 10

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