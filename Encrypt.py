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