
import numpy as np

class Triangle:
    def __init__(self):
        pass

    def area_base_height(self):
        """Calculate area using base and height."""
        base = float(input("Enter the base value: "))
        height = float(input("Enter the height value: "))
        area = 0.5 * base * height
        return area

    def area_sides(self, a, b, c):
        """Calculate area using all three sides (Heron's formula)."""
        s = (a + b + c) / 2
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        return area # if we use print we can obtain the result but it will also print none because the method is not returning anything

    def area_included_angle(self, a, b, angle_deg):
        """Calculate area using two sides and the included angle (in degrees)."""
        area = 0.5 * a * b * np.sin(np.radians(angle_deg))
        return area # if we use print we can obtain the result but it will also print none because the method is not returning anything

# Call all methods using object 
if __name__ == "__main__":
    tri = Triangle()  # create object

    # Method 1: base and height
    area1 = tri.area_base_height()
    print(f"Area using base and height: {area1:.2f}")

    # Method 2: three sides
    area2 = tri.area_sides(5, 6, 7)
    print(f"Area using 3 sides (5, 6, 7): {area2:.2f}")

    # Method 3: two sides and included angle
    area3 = tri.area_included_angle(6, 7, 45)
    print(f"Area using sides 6, 7 and angle 45°: {area3:.2f}")