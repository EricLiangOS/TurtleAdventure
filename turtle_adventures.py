#-----import statements-----
import random
import turtle
import time
import leaderboard


#-----game configuration----
#Leaderboard condigurations
score = 0
username = input("Username: ")
leaderboard_values = []

#Set up grid (Number corresponds to color, 0 is empty, 1 is wall)
grid = []
length = 30
height = 30
for i in range(height):
    row = []
    for j in range(length):
        row.append(1)
    grid.append(row)

standard_font = ("Times New Roman", 24, "normal")
small_font = ("Times New Roman", 18, "normal")

sprite_x = 0
sprite_y = 0
sprite = [sprite_x,sprite_y]

score = 0

leaderboard_file_name = "leaderboard.txt"

#Set up screen configurations
wn = turtle.Screen()
wn.tracer(False)
wn.bgcolor("aqua")
wn.setup(1000,850)
wn.title("Turtle Adventure")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.shape("square")

num_of_bombs = 1
num_of_lasers = 2
num_of_path_clears = 1
teleport_num = 1
powerup_shuffles = 2

#Function that redraws grid after every block
def draw_grid():
    global grid
    global score
    global num_of_path_clears
    global num_of_bombs
    global num_of_lasers
    global teleport_num
    global powerup_shuffles

    wn.tracer(False)
    pen.clear()
    top = 325
    left = -300
    
    colors = ["white","black", "blue", "red","gold", "purple", "lime", "green", "pink", "brown"]
    
    #Redraw grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            i_pos = top - (i * 20)
            j_pos = left + (j * 20)

            pen.color(colors[grid[i][j]])
            pen.setpos(j_pos, i_pos)
            pen.stamp()

    #Display inventory
    pen.setpos(-380,-310)
    pen.color(colors[5])
    pen.stamp()
    pen.setpos(-190,-310)
    pen.color(colors[6])
    pen.stamp()
    pen.setpos(0,-310)
    pen.color(colors[7])
    pen.stamp()
    pen.setpos(190,-310)
    pen.color(colors[8])
    pen.stamp()
    pen.setpos(380,-310)
    pen.color(colors[9])
    pen.stamp()

    pen.color("black")
    pen.setpos(0,375)
    pen.write("Turtle Adventure", move=True, align="center", font= standard_font )
    pen.setpos(150,340)
    pen.write("Score: " + str(int(score)), move=False, align="center", font= small_font)
    pen.setpos(0,-293)
    pen.write("Inventory", move=False, align="center", font= small_font)
    pen.setpos(-380,-350)
    pen.write("Bombs: " + str(num_of_bombs), move=False, align="center", font= small_font)
    pen.setpos(-190,-350)
    pen.write("Lasers: " + str(num_of_lasers), move=False, align="center", font= small_font)
    pen.setpos(0,-350)
    pen.write("Teleports: " + str(teleport_num), move=False, align="center", font= small_font)
    pen.setpos(190,-350)
    pen.write("Path Clears: " + str(num_of_path_clears), move=False, align="center", font= small_font)
    pen.setpos(380,-350)
    pen.write("Powerup Shuffles: " + str(powerup_shuffles), move=False, align="center", font= small_font)

    if check_lose():
        player_lose()
        return



def move_left():
    global grid
    global sprite_x
    global sprite_y
    global score
    global num_of_bombs
    global num_of_lasers
    global teleport_num
    global num_of_path_clears
    global powerup_shuffles
    #Check if sprite can move left (and not collide with maze or wall)
    if sprite_x > 0:
        if grid[sprite_y][sprite_x - 1] != 1 and grid[sprite_y][sprite_x - 1] != 2:
            if grid[sprite_y][sprite_x - 1] == 4:
                player_wins()
                return
            elif grid[sprite_y][sprite_x - 1] == 5:
                num_of_bombs += 1
            elif grid[sprite_y][sprite_x - 1] == 6:
                num_of_lasers += 1
            elif grid[sprite_y][sprite_x - 1] == 8:
                num_of_path_clears += 1
            elif grid[sprite_y][sprite_x - 1] == 7:
                teleport_num += 1
            elif grid[sprite_y][sprite_x - 1] == 9:
                powerup_shuffles += 1
            grid[sprite_y][sprite_x] = 2
            sprite_x -= 1
            grid[sprite_y][sprite_x] = 3
            score += 1
            draw_grid()
        
def move_right():
    global grid
    global sprite_x
    global sprite_y
    global score
    global num_of_bombs
    global num_of_lasers
    global teleport_num
    global num_of_path_clears
    global powerup_shuffles

    #Check if sprite can move right (and not collide with maze or wall)    
    if sprite_x < height-1:
        if grid[sprite_y][sprite_x + 1] != 1 and grid[sprite_y][sprite_x + 1] != 2:
            if grid[sprite_y][sprite_x + 1] == 4:
                player_wins()
                return
            elif grid[sprite_y][sprite_x + 1] == 5:
                num_of_bombs += 1
            elif grid[sprite_y][sprite_x + 1] == 6:
                num_of_lasers += 1
            elif grid[sprite_y][sprite_x + 1] == 8:
                num_of_path_clears += 1
            elif grid[sprite_y][sprite_x + 1] == 7:
                teleport_num += 1
            elif grid[sprite_y][sprite_x + 1] == 9:
                powerup_shuffles += 1

            grid[sprite_y][sprite_x] = 2
            sprite_x += 1
            grid[sprite_y][sprite_x] = 3
            score += 1
            draw_grid()
                    
def move_up():
    global grid
    global sprite_x
    global sprite_y
    global score
    global num_of_bombs
    global num_of_lasers
    global teleport_num
    global num_of_path_clears
    global powerup_shuffles

    #Check if sprite can move up (and not collide with maze or wall)    
    if sprite_y > 0:
        if grid[sprite_y-1][sprite_x] != 1 and grid[sprite_y- 1][sprite_x ] != 2:
            if grid[sprite_y - 1][sprite_x ] == 4:
                player_wins()
                return
            elif grid[sprite_y - 1][sprite_x ] == 5:
                num_of_bombs += 1
            elif grid[sprite_y - 1][sprite_x] == 6:
                num_of_lasers += 1
            elif grid[sprite_y - 1][sprite_x ] == 8:
                num_of_path_clears += 1
            elif grid[sprite_y - 1][sprite_x] == 7:
                teleport_num += 1
            elif grid[sprite_y - 1][sprite_x] == 9:
                powerup_shuffles += 1
            grid[sprite_y][sprite_x] = 2
            sprite_y -= 1
            grid[sprite_y][sprite_x] = 3
            score += 1
            draw_grid()
        
def move_down():
    global grid
    global sprite_x
    global sprite_y
    global score
    global num_of_bombs
    global num_of_lasers
    global teleport_num
    global num_of_path_clears
    global powerup_shuffles

    #Check if sprite can move down (and not collide with maze or wall)    
    if sprite_y < length-1:
        if grid[sprite_y+1][sprite_x] != 1 and grid[sprite_y + 1][sprite_x ] != 2:
            if grid[sprite_y + 1][sprite_x] == 4:
                player_wins()
                return
            elif grid[sprite_y + 1][sprite_x ] == 5:
                num_of_bombs += 1
            elif grid[sprite_y + 1][sprite_x] == 6:
                num_of_lasers += 1
            elif grid[sprite_y + 1][sprite_x ] == 8:
                num_of_path_clears += 1
            elif grid[sprite_y + 1][sprite_x] == 7:
                teleport_num += 1
            elif grid[sprite_y + 1][sprite_x] == 9:
                powerup_shuffles += 1
            grid[sprite_y][sprite_x] = 2
            sprite_y += 1
            grid[sprite_y][sprite_x] = 3
            score += 1
            draw_grid()

def use_bomb():
    global grid
    global sprite_x
    global sprite_y
    global score
    global num_of_bombs
    i_offset = [-2,-1,0,1,2]
    j_offset = [-2,-1,0,1,2]

    if num_of_bombs <= 0:
        return
    for r in i_offset:
        for k in j_offset:
            if sprite_x + k>=0 and sprite_x+k<length and sprite_y + r>=0 and sprite_y+r<height:
                if grid[sprite_y + r][sprite_x+k] != 1 and grid[sprite_y + r][sprite_x+k] != 2:
                    continue
                grid[sprite_y + r][sprite_x+k] = 0
                score += 1
    
    num_of_bombs -= 1
    grid[sprite_y][sprite_x] = 3
    draw_grid()

def horizontal_laser():
    global grid
    global sprite_x
    global sprite_y
    global score
    global num_of_lasers

    if num_of_lasers <= 0:
        return
    for i in range(6):
        if sprite_x - i>=0 and sprite_x + i<length:
            if grid[sprite_y][sprite_x+i] == 1 or grid[sprite_y][sprite_x+i] == 2:
                grid[sprite_y][sprite_x+i] = 0
            if grid[sprite_y][sprite_x-i] == 1 or grid[sprite_y][sprite_x-i] == 2:
                grid[sprite_y][sprite_x-i] = 0
            score += 1
    
    num_of_lasers -= 1
    grid[sprite_y][sprite_x] = 3
    draw_grid()

def vertical_laser():
    global grid
    global sprite_x
    global sprite_y
    global score
    global num_of_lasers

    if num_of_lasers <= 0:
        return
    for i in range(6):
        if sprite_y - i>=0 and sprite_y + i<height:
            if grid[sprite_y+i][sprite_x] == 1 or grid[sprite_y+i][sprite_x] == 2:
                grid[sprite_y+i][sprite_x] = 0
            if grid[sprite_y-i][sprite_x] == 1 or grid[sprite_y-i][sprite_x] == 2:
                grid[sprite_y-i][sprite_x] = 0
            score += 1
    
    num_of_lasers -= 1
    grid[sprite_y][sprite_x] = 3
    draw_grid()

def clear_path():
    global grid
    global num_of_path_clears

    if num_of_path_clears <= 0:
        return

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                grid[i][j] = 0
    
    num_of_path_clears -= 1
    draw_grid()

def teleport():
    global grid
    global teleport_num
    global sprite_x
    global sprite_y
    global score

    if teleport_num <= 0:
        return
    i_offset = [-3,-2,-1,0,1,2,3]
    j_offset = [-3,-2,-1,0,1,2,3]


    grid[sprite_y][sprite_x] = 0
    sprite_x = random.randint(0,28)
    sprite_y = random.randint(0,28)
    while grid[sprite_y][sprite_x] != 0:
        sprite_x = random.randint(0,28)
        sprite_y = random.randint(0,28)

    for r in i_offset:
        for k in j_offset:
            if sprite_x + k>=0 and sprite_x+k<length and sprite_y + r>=0 and sprite_y+r<height:
                if grid[sprite_y + r][sprite_x+k] != 1 and grid[sprite_y + r][sprite_x+k] != 2:
                    continue
                grid[sprite_y + r][sprite_x+k] = 0
                score += 1
    teleport_num -= 1
    grid[sprite_y][sprite_x] = 3
    draw_grid()

def shuffle_powerups():
    global grid
    global powerup_shuffles

    if powerup_shuffles<= 0:
        return

    #First clear all previous powerups
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]>=5:
                grid[i][j] = 0

    #Function that randomly adds powerups players can collect
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0 and random.randint(1,150) == 42:
                grid[i][j] = 5
            elif grid[i][j] == 0 and random.randint(1,225) == 18:
                grid [i][j] = 6
            elif grid[i][j] == 0 and random.randint(1,390) == 36:
                grid [i][j] = 7
            elif grid[i][j] == 0 and random.randint(1,780) == 274:
                grid [i][j] = 8
            elif grid[i][j] == 0 and random.randint(1,999) == 654:
                grid [i][j] = 9

    powerup_shuffles -= 1
    draw_grid()
    
#Checks if player lost
def check_lose():
    global sprite_y
    global sprite_x
    global grid
    global num_of_path_clears
    global num_of_bombs
    global num_of_lasers
    global teleport_num
    global length

    if sprite_x == 29 and sprite_y == 29:
        player_wins()
        return False

    if num_of_path_clears>0 or num_of_lasers>0 or num_of_bombs>0 or teleport_num>0:
        return False

    if sprite_y != 0 and grid[sprite_y-1][sprite_x] == 0:
        return False
    
    if sprite_y != height-1 and grid[sprite_y+1][sprite_x] == 0:
        return False

    if sprite_x != 0 and grid[sprite_y][sprite_x-1] == 0:
        return False

    if sprite_x != length -1 and grid[sprite_y][sprite_x+1] == 0:
        return False

    time.sleep(2)
    return True

#Shows player they won, sees if they made leaderboard, displays leaderboard
def player_wins():
    global leaderboard_file_name
    global score
    global username

    wn.clear()
    wn.bgcolor("dimgrey")

    wn.tracer(False)
    made_leaderboard = leaderboard.update_leaderboard(leaderboard_file_name,leaderboard_values,username,score)
    leaderboard.draw_leaderboard(made_leaderboard,leaderboard_file_name, pen, int(score),True)

#Shows player they lost, displays leader
def player_lose():
    wn.clear()
    wn.bgcolor("dimgrey")
    wn.tracer(False)
    leaderboard.draw_leaderboard(False,leaderboard_file_name, pen, -1, False)


wn.update()
wn.listen()
wn.onkeypress(lambda: move_left(), "a")
wn.onkeypress(lambda: move_right(), "d")
wn.onkeypress(lambda: move_up(), "w")
wn.onkeypress(lambda: move_down(), "s")
wn.onkeypress(lambda: use_bomb(), "r")
wn.onkeypress(lambda: horizontal_laser(), "q")
wn.onkeypress(lambda: vertical_laser(), "e")
wn.onkeypress(lambda: clear_path(), "Q")
wn.onkeypress(lambda: teleport(), "E")
wn.onkeypress(lambda: shuffle_powerups(), "R")

#Used to see if there are filled blocks around
i_offset = [-1,0,1]
j_offset = [-1,0,1]


grid[0][0] = 0

    
#Draws the walls of the maze
for i in range(len(grid)):
    for j in range(len(grid[i])):
        counter = 0
        for r in i_offset:
            for k in j_offset:
                if not (r== 0 and k == 0) and i+r>=0 and j+k>=0 and r+i<len(grid) and j+k<len(grid[i]) and i**2 - j**2 != 0:
                    if grid[i+r][k+j] == 0:
                        counter += 1
                    
        
        if counter >=1:
            possibilities = [0]
            for k in range(counter-1):
                possibilities.append(1)
            grid[i][j] = random.choice(possibilities)

white_columns = []
white_rows = []

path_x = 0
path_y = 0
counter = 0

for i in range(3):
    #Add a possibile path to the end (Make it random)
    while path_x != length-1 and path_y != height-1:
        for i in range(random.randint(1,height-1-path_y)):
            grid[path_y][path_x] = 0
            path_y += 1
        for i in range(random.randint(1,length-1-path_x)):
            grid[path_y][path_x] = 0
            path_x += 1

    if path_x == height-1:
        for i in range(length-1-path_y):
            grid[path_y][path_x] = 0
            path_y += 1
    elif path_y == length-1:
        for i in range(height-1-path_x):
            grid[path_y][path_x] = 0
            path_x += 1

        for i in range(30-path_x):
            grid[path_y][path_x] = 0
            path_x += 1

need_to_fill_in = []

#Fill in boxes of black with white (For more complexity)
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[i])-1):
        if grid[i+1][j] == 1 and grid[i-1][j] == 1 and grid[i][j+1] == 1 and grid[i][j-1] == 1:
            need_to_fill_in.append([i,j])

for coordinate in need_to_fill_in:
    grid[coordinate[0]][coordinate[1]] = 0

grid[height-1][length-1] = 4
grid[0][0] = 3


shuffle_powerups()




draw_grid()
wn.update()



wn.mainloop()
