#import random package
import random

#get random number between 1 and 10
#print(random.randint(0, 1))
choice = random.randint(0,3)

if choice == 0:
    print("Tails")
elif choice == 1:
    print("Heads")
else:
    print("Your quarter fell in the gutter.")

#get random number between 1 and 100
# print(random.randint(0, 10000))