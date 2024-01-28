import random, sys

def gen_pwd(length, no_special_chars = False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_+=?/"
    if (no_special_chars == "-no_special_chars"):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    password = ""
    for x in range(0, eval(length)):
        password += alphabet[random.randint(0, len(alphabet)-1)]
    return password

if (sys.argv[1] == "-h" ):
    print("Usage: <length> <no_special_chars>")
elif (len(sys.argv) < 3):
    print(gen_pwd(sys.argv[1], False))
else:
    print(gen_pwd(sys.argv[1], sys.argv[2]))