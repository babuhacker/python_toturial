
# | | 0
#-----1
# | | 2
#-----3
# | | 4
#01234
def drawfield(field):
    for row in range(5):#0,1,2,3,4
                        # 0,.,1,.,2
        if row % 2 == 0:#0,2,4
            practicalrow = int(row /2)#0,1,2
            for column in range(5):#0,1,2,3,4
                                   #0,.,1,.,2
                if column % 2 == 0:#0,2,,4
                    practicalcolumn = int(column/2)#0,1,2
                    if column != 4:
                        print(field[practicalcolumn][practicalrow],end = "")
                    else:
                        print(field[practicalcolumn][practicalrow])
                else:
                    print("|",end = "")
        else:
            print("-----")
player = 1
currentfield = [[" "," "," "],[" "," "," "],[" "," "," "]]
drawfield(currentfield)
while (True): #True == True
    print("players turn: ", player)
    moverow = int(input("please enter the row\n"))
    movecolumn = int(input("please enter the column\n"))
    if player == 1:
        #make move for player 1
        if currentfield[movecolumn][moverow] == " ":
            currentfield[movecolumn][moverow] = "X"
            player = 2
    else:
        # make move for player 2
        if currentfield[movecolumn][moverow] == " ":
            currentfield[movecolumn][moverow] = "O"
            player = 1
    drawfield(currentfield)
