from turtle import *

def draw_square(side, fill=True):
    if fill:
        begin_fill()
    down()
    for line in range(0, 4):
        forward(side)
        left(90)
    up()
    if fill:
        end_fill() 

def draw_outer_square(side):
    draw_square(side, fill=False)

def move_to_next_point(current_level, current_side, current_square):
    if current_square == 0:
        forward(current_side)
        left(90)
        forward(current_side)
        left(270)
    elif current_square >= 1 and current_square <= 3:
        if current_square == 3:
            left(90)
        forward(current_side*3)
        if current_square == 3:
            left(270)
    elif current_square == 4: 
        left(90)
        forward(current_side*3)
        left(270)
    elif current_square == 5 or current_square == 6:
        left(180)
        forward(current_side*3)
        left(180)
    elif current_square == 7:
        left(270)
        forward(current_side*3)
        left(90)

def draw_level(current_level, outer_square_side):
    square_count = ((current_level-1)*9) + 1
    current_side = outer_square_side/(3**current_level)
    print(current_side)

    for current_square in range(0, square_count):
        move_to_next_point(current_level, current_side, current_square)
        draw_square(current_side)

def main():
    levels = 2
    outer_square_side = 300

    draw_outer_square(outer_square_side)
    home_point = pos()

    for current_level in range(1, levels+1):
        draw_level(current_level, outer_square_side)
        setpos(home_point)

    exitonclick()

if __name__=='__main__':
    # parse args : speed, outer square side

    speed(0)
    #speed("slowest")
    main()
