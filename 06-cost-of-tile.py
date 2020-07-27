"""
Find Cost of Tile to Cover W x H Floor - 
Calculate the total cost of tile it would take 
to cover a floor plan of width and height, 
using a cost entered by the user.
"""

# takes in a cost of single tile, a width and height of the plan
def cost_of_tile(cost,width=100,height=100):
    # assume the size of a tile is 1 x 1
    total_cost = cost * width * height
    return total_cost,width,height


if __name__ == "__main__":
    cost = ''
    while isinstance(cost,float) == False:
        try:
            cost = float(input("Please enter the cost of a single tile. "))
        except:
            print("Please enter a valid number. ")
            continue
        if cost<=0:
            print("Please enter a positive value. ")
            cost=''
        else:
            pass
    total,width,height = cost_of_tile(cost)
    print(f"${cost} tile to cover {width}m x {height}m costs ${total}.")