def board_game(rows, columns):
    maximum_columns = 160
    maximum_rows = 160
    if columns <= maximum_columns and rows <= maximum_rows:
        for row in range(5):
            if row % 2 == 0:
                for column in range(5):
                    if column % 2 == 1:
                        if column != 5:
                            print(" | | ")
                    print("--------")


print(board_game)
