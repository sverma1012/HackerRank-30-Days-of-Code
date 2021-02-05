import sys


S = input().strip()

try: # convert the string and try printing it.
    convert = int(S)
    print(convert)
except: # if there is an error, then print the error message.
    print('Bad String')