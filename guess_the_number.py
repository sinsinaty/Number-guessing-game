import random

LIVES = 10
SCORE = 0
HIGH_SCORE = 0

DONE = False

print("\t\t =============>  Welcome to the number guessing game developed by Python  <===============\n")
try:
    with open('high_score.txt', mode='r') as f:
        highscore = f.read()
except:
    with open('high_score.txt',mode='w') as f:
        highscore = f.write(HIGH_SCORE)

print(f"Your current HighScore is ' {highscore} '\n")
print("You have only 10 lives to guessing the number\n")

rand_num = int(random.randint(1, 100))

while True:
    while LIVES > 0:
        try:
            user_string = input("Choose a number between 1-100 : ")
            if user_string == "Q" or user_string == "q":
                DONE = True
                break
            user = int(user_string)
            if user > 100 or user < 1:          # To account for invalid guesses
                print("Guesses must be from 1 to 100")
                continue
            if user == rand_num:
                print("Congratulations You guessed it right.")
                SCORE = LIVES
                print(f"Your score is {SCORE} ")
                if SCORE > HIGH_SCORE:
                    print("This is also a new high score!!!")
                    HIGH_SCORE = SCORE

                    with open('high_score.txt', mode='w') as f:
                        f.write(str(HIGH_SCORE))

                print(f"The Current High Score Is {HIGH_SCORE}")
                break

            elif user > rand_num:
                LIVES -= 1
                print(
                    f"Too high! Please guess lower number.\n Current Lives= {LIVES}")
            elif user < rand_num:
                LIVES -= 1
                print(
                    f"Too Low! Please guess higher number.\n Current Lives= {LIVES}")
        except Exception as e:
            print(e)

    if (DONE == True):
        break

    print("\n\t\tLet's do this again\n")

    print("\t\t =============>  Welcome to the number guessing game developed by Python  <===============\n")
    print("You have only 10 lives to guessing the number\n")
    rand_num = int(random.randint(1, 100))

    LIVES = 10
    SCORE = 0
