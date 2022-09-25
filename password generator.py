#random password generator
import random

locase_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppcase_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','<','>','?',',','.','/','+',]

maximum_length = 16
all = locase_characters + uppcase_characters + numbers + symbols

temp = random.sample(all,maximum_length)
password = "".join(temp)


print("Welcome to password generator")

ready = input("Do you want a password? ")

if ready.lower() != "yes":
    quit()

print("here it is!\n")

print(password)

