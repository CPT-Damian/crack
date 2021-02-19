import hashlib
from art import *

flag = 0

x = ("CRACK")
tprint(x, "rnd-xlarge")


pass_hash = input("Enter md5 hash: ")

word_list = input("Name of .txt file containing world list: ")

try:
    pass_file = open(word_list)
except:
    print("No file found bro.")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("Hash cracked. Let's goooo\n ")
        print("Hashed word is: " + word)
        quit()
        break


if flag == 0:
    print("Word not found in the list, sorry bruv. Try another wordlist :p")
