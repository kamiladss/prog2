import random
def game():
    
    print("Hello! What is your name?")
    name=input()
    rn=random.randint(1,20)
    cn=0
    ng=0
    print("Well, "+name+ ", I am thinking of a number between 1 and 20. Take a guess.")
    while ng!=rn:
        ng=int(input())
        if ng==rn:
            print("Good job,"+name+"! You guessed my number in ",cn+1," guesses!")
        
        elif ng<rn and ng>0:
            cn+=1
            print("Your guess is too low. Take a guess.")
        elif ng>rn and ng<21:
            cn+=1
            print("Your guess is too high. Take a guess.")
        else:
            print("Some error!!!!!!")

game()