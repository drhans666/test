#! python3
#strongPasswordDetector - detects passwords that are strong: min 8 char long,
# contain upper/lowercase char, at least one digit'''
import re


print('Validation of password strenght'.center(50, '='))
print('Enter Your Password: ')
password = input()

def ifPasswordStrong():
#checks for char number and lowercase
    passwordRegexLvl1 = re.compile(r'([a-z]{8})+')
    strongPassLvl1 = passwordRegexLvl1.search(password)
    if strongPassLvl1 == None:
        print("Your password isn't strong. At least 8 char, upper/lowercase, one digit")
    else:
#checks for uppercase
        passwordRegexLvl2 = re.compile(r'([A-Z])+')
        strongPassLvl2 = passwordRegexLvl2.search(password)
        if strongPassLvl2 == None:
            print("Your password isn't strong. At least 8 char, upper/lowercase, one digit")
        else:
#checks for digit
            passwordRegexLvl3 = re.compile(r'([0-9])+')
            strongPassLvl3 = passwordRegexLvl3.search(password)
            if strongPassLvl3 == None:
                print("Your password isn't strong. At least 8 char, upper/lowercase, one digit")
            else:
                print('Your password is strong')

ifPasswordStrong()