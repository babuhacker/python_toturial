song = {"name": "pani pani", "artist": "badshah", "cast": "jacqueline fernandez", "realese date": "9-06-2021"}
while (True):
    guess = input("OK Guess The Song Name.?\n")
    if guess == song['name']:
        print("song matched", song["name"])
        break
    else:
        print("Sorry You Are Wrong")

while (True):
    guess = input("Now Guess The Artist Of Song\n")
    if guess == song['artist']:
        print("Artist matched", song["artist"])
        break
    else:
        print("Sorry Artist Mismatched")

while (True):
    guess = input("Now Tell Me Cast OF Song\n")
    if guess == song['cast']:
        print("Correct", song["cast"])
        break
    else:
        print("Wrong answer")

while (True):
    guess = input("Now Guess The Realese Date Of Song\n")
    if guess == song['realese date']:
        print("Date matched", song["realese date"])
        break
    else:
        print("Sorry Date Mismatched")

print("congratulations you won the game")
