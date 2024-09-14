def check_rectangles(x1, y1, w1, h1, x2, y2, w2, h2):
    half_w1, half_h1 = w1 / 2, h1 / 2
    half_w2, half_h2 = w2 / 2, h2 / 2

    if (x2 - half_w2 >= x1 - half_w1 and
        x2 + half_w2 <= x1 + half_w1 and
        y2 - half_h2 >= y1 - half_h1 and
        y2 + half_h2 <= y1 + half_h1):
        return "r2 is inside r1"

    elif (x2 + half_w2 > x1 - half_w1 and
          x2 - half_w2 < x1 + half_w1 and
          y2 + half_h2 > y1 - half_h1 and
          y2 - half_h2 < y1 + half_h1):
        return "r2 overlaps r1"
  
    else:
        return "r2 does not overlap r1"

print("Enter r1's data:")
x1 = float(input("Enter X-center coordinate: "))
y1 = float(input("Enter Y-center coordinate: "))
w1 = float(input("Enter width: "))
h1 = float(input("Enter height: "))

print("\nEnter r2's data:")
x2 = float(input("Enter X-center coordinate: "))
y2 = float(input("Enter Y-center coordinate: "))
w2 = float(input("Enter width: "))
h2 = float(input("Enter height: "))

result = check_rectangles(x1, y1, w1, h1, x2, y2, w2, h2)
print(result)
