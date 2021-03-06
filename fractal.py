from turtle import *

def set_home_position():
    setpos(0,0)

def move_to_line_beggining():
    setx(0)

def move_to_upper_line(current_side):
    left(90)
    forward(current_side*2)
    left(270)

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

def move_to_next_square(current_level, current_side, current_square):
    if current_square == 1:
        forward(current_side)
        left(90)
        forward(current_side)
        left(270)
    else:
        forward(current_side*3)

def draw_square_line(current_level, current_side, current_line):
    for current_square in current_line: 
        move_to_next_square(current_level, current_side, current_square)
        draw_square(current_side)

def draw_level(current_level, outer_square_side):
    current_side = outer_square_side/(3**current_level)
    square_count = 9**(current_level-1)
    line_number = 3**(current_level-1)
    level_lines = ([range(1, (square_count//line_number)+1)
                   for line in range(1, line_number+1)] or
                   [(1,2)])

    for line_index, current_line in enumerate(level_lines):
        draw_square_line(current_level, current_side, current_line)
        move_to_line_beggining()
        move_to_upper_line(current_side)

def main():
    levels = 4
    outer_square_side = 300

    draw_outer_square(outer_square_side)
    home_point = pos()

    for current_level in range(1, levels+1):
        draw_level(current_level, outer_square_side)
        set_home_position()

    exitonclick()

if __name__=='__main__':
    # parse args : speed, outer square side

    speed(0)
    #speed("slowest")
    main()
