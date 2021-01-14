from random import randint
import random
from more_itertools import random_permutation

UppercaseLetter1 = chr(randint(65, 90))
#print(UppercaseLetter1)

UppercaseLetter2 = chr(randint(65,90))
#print(UppercaseLetter2)

LowercaseLetter1 = chr(randint(65,90)).lower()
#print(LowercaseLetter1)

LowercaseLetter2 = chr(randint(65,90)).lower()
#print(LowercaseLetter2)

digit1 = str(randint(0,9))
#print(digit1)

digit2 = str(randint(0,9))
#print(digit2)


punctuationSign1 = chr(randint(33, 39))
#print(punctuationSign1)


punctuationSign2 = chr(randint(33,39))
#print(punctuationSign2)


password = str(UppercaseLetter1 + UppercaseLetter2 + LowercaseLetter1 + LowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2)
print(''.join(random_permutation(password)))






