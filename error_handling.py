
game = [[0, 0, 0],   #0
        [0, 0, 0],
        [0, 0, 0]]

def game_board(player=0, row=0, column=0, just_display=False):
        try:
                print("   0  1  2 ")
                if not just_display:
                        game[row][column] = player 
                for count,row in enumerate(game):
                         print(count,row)
        except IndexError as e:
                print("ERROR: Please check whether you entered anything except 0, 1 or 2?? \n",e)

#game_board(1, 2, 3 )
game_board(just_display=True)
game_board(player=1, row=3, column=1)


