# Lottery
'''
    Ask the user to press any key. Display any 3 random space-separated digits between 0-9 e.g. 6 2 7.
    If any of them is 7, output "Congratulations!". 
    Else, output "Try again! Better luck next time.". 
    Repeat.
'''

import random

key = input("Press any key to start the lottery: ")
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lottery_digits = random.sample(digits , 3)
print(lottery_digits, end=" ")

if 7 in lottery_digits:
    print("\n Congratulations!")
else:
    print("\nTry again! Better luck next time.")

