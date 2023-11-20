import random
import string

affirmatives = ["y", "Y", "yes", "Yes", "yeah", "Yeah", "yup", "Yup"]
negatives = ["n", "N", "no", "No", "nope", "Nope", "nah", "Nah"]

def genKey():
    try:
        keyAmount = int(input("Amount of keys [integer] (default: 1): "))
    except:
        keyAmount = int(1)

    keys = []
    for i in range(keyAmount):
        chars = string.ascii_uppercase + string.digits
        key = '-'.join(''.join(random.choice(chars) for _ in range(5)) for _ in range(3))
        i += 1
        keys.append(key)
        print(key)

    isSaved = str(input("Would you like to save the key(s) [yes/no] (default: no)? "))

    if isSaved in affirmatives:
        saveName = str(input("Where would you like to save them [filename] (default: keys.txt)? "))
        if saveName == "":
            saveName = str("keys")
        with open(f"{saveName}.txt", 'w') as f:
            for key in keys:
                f.write(f"{key}\n")
        print(f"Keys saved to {saveName}.txt")
    elif isSaved in negatives:
        print("Skipping the saving part.")

genKey()

while True:
    genMore = str(input("Would you like to generate more keys [yes/no] (default: no)? "))

    if genMore in affirmatives:
        genKey()
    elif genMore in negatives or genMore == "":
        print("Understandable, have a nice day.")
        break
    else:
        print("Didn't understand the answer!")