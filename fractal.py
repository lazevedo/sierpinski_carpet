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

def move_to_next_point(current_side):
    forward(current_side)
    left(90)
    forward(current_side)
    left(270)

def draw_level(current_level, outer_square_side):
    square_count = ((current_level-1)*9) + 1
    current_side = outer_square_side/(current_level*3)

    for current_square in range(0, square_count):
        move_to_next_point(current_side)
        draw_square(current_side)

def main():
    levels = 1
    first_square_side = 50
    outer_square_side = 3*first_square_side 

    draw_outer_square(outer_square_side)
    home_point = pos()

    for current_level in range(1, levels+1):
        draw_level(current_level, outer_square_side)
        setpos(home_point)

    exitonclick()

if __name__=='__main__':
    main()
