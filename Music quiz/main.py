import random
import os
import time
os.system('cls')  # Clears the terminal on Windows
print("Welcome to the song quiz!") #Intro text
time.sleep(2)
print("\nYou will be given the name of the artist and the initials of the song and you have to guess the name of the song!")
time.sleep(5)
os.system('cls')  # Clears the terminal on Windows
print("No personal infrmation is stored on the cloud or shared with any third parties.\nAll data is stored locally on your device.\n")
AA = input("\nEnter your name: ") #Player name input
time.sleep(2)
os.system('cls')  # Clears the terminal on Windows


 #Variable to keep track of time
stop = 0 #Variable to stop the game
score = 0 #initial score
print("Make sure you answer Every question with a CAPITAL LETTER AT THE START.") #Instructions
time.sleep(3)
print("You will get 3 points for a correct answer on the first try and 1 for a correct answer on the second try.") #Instructions
time.sleep(5)


Music = [] #List to store songs and artists
Fh = open("Music.txt","r")
for line in Fh:
  line = line.strip()
  s,a = line.split(":") #Split the song and artist
  Music.append([s,a]) #Add to list
Fh.close() #Close the file
print(Music)


qnum = 1
while stop == 0:
  #os.system('cls')  # Clears the terminal on Windows
  print("question",qnum)
  qnum += 1
  print("score = ",score)
  num = random.randint(0, len(Music)-1) #Select random song for question
  if num == num: # Prevents the same question being asked multiple times
    num = random.randint(0, len(Music)-1)
  else:
    num = num
  question = Music[num] #config the question
  Song = Music[num]
  answer = Song[1]
  print(question[0]) #Print the artist
  song = Song[1]
  song = song.lower()
  S_list = song.split
  for word in S_list():
    print(word[0]) #Print the initials of each word in the song title
  PA = input("Enter your answer: ") #Player answer
  if PA == answer: #Check if answer is correct
    print("correct")
    score += 3 #Add 3 points for first try
  else:
    print("last try")
    PA2 = input("Enter answer: ") #Second chance to answer
    if PA2 == answer: #Check if answer is correct
      print("correct")
      score += 1 #Add 1 point for second try
    else: #If both answers are wrong
      print("The correct answer is ", answer)
      print("Your final score was ",score)
      print("Game over")
      time.sleep(3)
      os.system("cls") # Clears the terminal on Windows
      stop += 1 #Ends the game


with open("scores.txt","a") as file: #Writes the score to a text file
  file.write(AA)
  file.write(" score = ")
  file.write(str(score))
  file.write("\n")


if score >= 50: #Only the top scores are added to the top scores list
  with open("Top_scores.txt","a") as file:
    file.write("\n")
    file.write(AA)
    file.write(" score = ")
    file.write(str(score))
else:
  print("\nYou did not get onto the top scores list! \n You need at least 50 points to get on the list.")


print("\nThank you for playing!")