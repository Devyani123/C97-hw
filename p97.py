import random

number=random.randint(1,9)

print('welcome to number quessing game')

print('guess the number')

num=int(input('guess a number between 1 to 9: '))


chances=5

while chances > 0:

    if(number==num):
        print("congratulations you have guessed the right number")

        break
    elif(number<num):
        print("guess a lesser number")
        
    else:
        print('guess a higher number')
    chances=chances-1 

    num=int(input('guess a number between 1 to 9: '))      

if chances ==0:
    print("oops you are out of chances try again later!")
    

