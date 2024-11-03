import turtle

def main():
    print("Welcome to Pythagoras Tree rendering program")

    raw_depth = input("Enter how many iteration you'd like to run for tree rendering (number non less than zero and not bigger than 100) >>>   ")

    # validation
    if not raw_depth.isdigit():
        print("Cannot execute rendering, no valid number of iterations provided")
        return
    
    depth_level = int(raw_depth)
    if depth_level < 0 or depth_level > 100:
        print("Cannot execute rendering, number iterations should be not less than zero and no bigger than 100")
        return
    
    draw_tree(depth_level)


def draw_tree(depth_level):
    # prepare rendering
    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(500, 500)

    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)  
    t.penup()

    t.setposition(0, -100)
    t.pendown()
    t.hideturtle()
    t.setheading(90)

    # prepare parameters for tree
    branch_length = 50
    branch_reduction = 5
    angle = 25

    # draw pythagoras tree via recursion
    draw_tree_part(t, depth_level, branch_length, branch_reduction, angle)
    
    window.exitonclick()


def draw_tree_part(t: turtle.Turtle, depth_level, branch_length, branch_reduction, angle):
    if depth_level == 0:
        t.fd(0)
    else:
        branch_length = branch_length - branch_reduction
        t.forward(branch_length)
        t.left(angle)

        draw_tree_part(t, depth_level - 1, branch_length, branch_reduction, angle)
        t.right(angle * 2)

        draw_tree_part(t, depth_level - 1, branch_length, branch_reduction, angle)
        t.left(angle)
        t.backward(branch_length)


if __name__ == "__main__":
    main()