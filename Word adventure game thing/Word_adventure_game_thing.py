print("your on a road and you see a fork in the road")
print("Do you go left or right")
way = input("Left or Right? ")
if way == "left":
    print("You see a bear")
    print("do you run or fight")
    action = input("Run or Fight? ")
    if action == "run":
        print("you run away and live\n But you are lost")
        print("you see a house and a cave")
        print("do you go in the house or the cave")
        place = input("House or Cave? ")
        if place == "house":
            print("you go in the house and find a map")
            print("you find your way home")
            print("you win")
        else:
            print("you go in the cave and find a dragon")
            print("you die\n GAME OVER")
    else:
        print("you fight the bear and die\n GAME OVER")
else:
    print("you fall in a pit and die\n GAME OVER")
