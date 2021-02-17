# Areas of Rectangles
lengthRectangle1 = float(input("Enter the length of the first rectangle: "))
widthRectangle1 = float(input("Enter the width of the first rectangle: "))
areaRectangle1 = lengthRectangle1 * widthRectangle1
lengthRectangle2 = float(input("Enter the length of the second rectangle: "))
widthRectangle2 = float(input("Enter the width of the second rectangle: "))
areaRectangle2 = lengthRectangle2 * widthRectangle2
if areaRectangle1 > areaRectangle2:
    print("The first rectangle has the greater area.")
elif areaRectangle1 < areaRectangle2:
    print("The second rectangle has the greater area.")
else:
    print("Areas of both rectangles are the same.")
