import math

def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height* width)/cover)
    # num_of_cans = math.ceil(num_of_cans)
    print(f"You'll need {num_of_cans} cans of paint")

test_h = int(input("Enter the height of the wall: "))
test_w = int(input("Enter the width of the wall: "))
coverage =5
paint_calc(height= test_h, width= test_w, cover= coverage)