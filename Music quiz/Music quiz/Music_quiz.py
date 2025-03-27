import random

AA = input("enter your player name ")
if AA == "Snowman Scott":
 print("authenticated!")
else:
  print("you are not allowed to play! Bye Bye")
  exit()
AP = input("enter your password")
if AP == "123":
  print("Welcome in")
else:
  print("Stop trying to get in!")
  exit()
stop = 0
score = 0
#start text
print("Make sure you answer Every question with a CAPITAL LETTER AT THE START.")

Music = []
Fh = open("Music.txt","r")
for line in Fh:
  line = line.strip()
  s,a = line.split(":")
  Music.append([s,a])

qnum = 1
while stop == 0:
  print("question",qnum)
  qnum += 1
  print("score = ",score)
  num = random.randint(0, len(Music)-1)
  question = Music[num]
  Song = Music[num]
  answer = Song[1]
  print(question[0])
  song = Song[1]
  song = song.lower()
  S_list = song.split
  for word in S_list():
    print(word[0])
  PA = input("enter your answer")
  if PA == answer:
    print("correct")
    score += 3
  else:
    print("last try")
    PA2 = input("enter answer")
    if PA2 == answer:
      print("correct")
      score += 1
    else:
      print("The correct answer is ", answer)
      print("Your final score was ",score)
      print("game over")
      stop += 1
  
file = open("scores.txt","a")
file.write(AA)
file.write("\n")
file.write(str(score))

file = open("Top_scores.txt","a")
if score >= 50 :
  file.write(AA)
  file.write(" score = ")
  file.write(str(score))