import random

def genKey():
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
           '5', '6', '7', '8', '9']
    x = 0
    newKey = ""
    while x < 17:
        digit = random.randint(0, 34)
        if x == 5 or x == 11:
            newKey += '-'
        else:
            newKey += symbols[digit]
        x += 1
    return newKey

def genUniqueKeyToFile():
    key = genKey()

    f = open("keys.txt", "a+")

    count = 0
    while True:
        line = f.readline()

        if line == key:
            key = genKey
        if not line or line != key:
            print("Your new unique key: "+key)
            f.write(key+'\n')
            break
        count += 1
    
    f.close()

genUniqueKeyToFile()

affirmatives = ["y", "Y", "yes", "Yes", "yeah", "Yeah", "yup", "Yup"]
negatives = ["n", "N", "no", "No", "nope", "Nope", "nah", "Nah"]
while True:
    again = input("Generate another key? (y/n): ")
    if again in affirmatives:
        genUniqueKeyToFile()
    elif again in negatives:
        print("Understandable, have a nice day.")
        break
    else:
        print("Didn't understand the answer!")
