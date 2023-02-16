#Get lenght and width of a rectangle using prompt
#Script that prompts the user to enter length and width of the rectangle and calculate its area and perimeter of this rectangle
#Store the user input as an integer in the "lenght" variable
length = int(input("What's the length of the rectangle?"))
#Store the user input as an integer in the "width" variable
width = int(input("What's the width of the rectangle?"))
#Calculating area and perimeter of a rectangle
area = length*width
perimeter = (2*(length + width))
print(area)
print(perimeter)