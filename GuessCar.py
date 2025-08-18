print( '''                                                                                                                                              
    mmmm   mm    mm  mmmmmmmm    mmmm      mmmm              mmmmmmmm  mm    mm  mmmmmmmm           mm      mm   mmmm    mmmmmm    mmmmm    
  ##""""#  ##    ##  ##""""""  m#""""#   m#""""#             """##"""  ##    ##  ##""""""           ##      ##  ##""##   ##""""##  ##"""##  
 ##        ##    ##  ##        ##m       ##m                    ##     ##    ##  ##                 "#m ## m#" ##    ##  ##    ##  ##    ## 
 ##  mmmm  ##    ##  #######    "####m    "####m                ##     ########  #######             ## ## ##  ##    ##  #######   ##    ## 
 ##  ""##  ##    ##  ##             "##       "##               ##     ##    ##  ##                  ###""###  ##    ##  ##  "##m  ##    ## 
  ##mmm##  "##mm##"  ##mmmmmm  #mmmmm#"  #mmmmm#"               ##     ##    ##  ##mmmmmm            ###  ###   ##mm##   ##    ##  ##mmm##  
    """"     """"    """"""""   """""     """""                 ""     ""    ""  """"""""            """  """    """"    ""    """ """"" ''')

print("**********************************************************************************************************************************************") #welcome message("")
import random #imported random module
car_list = ["nano","jaguar","alto","innova","kia","swift","verna","fortuner","thar","lamborgini","defender","mercedes"] #car list

lives = 6

chossen_car=random.choice(car_list) #shuffeled words
print("your word is" , chossen_car)    #printed that random word

#step 2 = replacing the word with a blank sign  
placeholder = ""
word_length=len(chossen_car)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

#step 3 = guessing the letter & checking if the letter is in the word or not
correct_letters = []
game_over = False
while not game_over:
    guess = input("guess a letter = ")
    print("you guessed", guess)

    display = ""
    for letter in chossen_car:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chossen_car:
        lives -= 1
        print("you lose a life, lives left", lives)
        if lives == 0:
            game_over = True
            print("you lose")

    if "_" not in display:
        game_over = True
        print("you win")




