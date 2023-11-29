import math
from tkinter import *

win= Tk()
win.title("App giai toan hinh")
win.geometry('500x500')
win['bg'] = 'grey'




win.mainloop()

class ShapeCalculator:
    def __init__(self):
        self.shapes = ["Square", "Rectangle", "Circle", "Triangle", "Parallelogram", "Hexagon"]
        self.compound_shapes = ["Compound Shape"]
        self.three_d_shapes = ["Cube", "Sphere", "Cylinder", "Pyramid"]

    def calculate_area(self, shape, dimensions):
        if shape == 0:  # Square
            side = dimensions[0]
            return side * side
        elif shape == 1:  # Rectangle
            length, width = dimensions
            return length * width
        elif shape == 2:  # Circle
            radius = dimensions[0]
            return math.pi * radius * radius
        elif shape == 3:  # Triangle
            side1, side2, side3 = dimensions
            s = (side1 + side2 + side3) / 2
            return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        elif shape == 4:  # Parallelogram
            base, height = dimensions
            return base * height
        elif shape == 5:  # Hexagon
            side = dimensions[0]
            return 3 * math.sqrt(3) * (side ** 2)

    def calculate_perimeter(self, shape, dimensions):
        if shape == 0:  # Square
            side = dimensions[0]
            return 4 * side
        elif shape == 1:  # Rectangle
            length, width = dimensions
            return 2 * (length + width)
        elif shape == 2:  # Circle
            radius = dimensions[0]
            return 2 * math.pi * radius
        elif shape == 3:  # Triangle
            side1, side2, side3 = dimensions
            return side1 + side2 + side3
        elif shape == 4:  # Parallelogram
            base, side = dimensions
            return 2 * (base + side)
        elif shape == 5:  # Hexagon
            side = dimensions[0]
            return 6 * side

    def display_2d_shapes(self):
        print("2D Shapes:")
        for i, shape in enumerate(self.shapes):
            print(f"{i + 1}. {shape}")

    def display_compound_shapes(self):
        print("\nCompound Shapes:")
        for i, compound_shape in enumerate(self.compound_shapes):
            print(f"{i + 1}. {compound_shape}")

    def display_3d_shapes(self):
        print("\n3D Shapes:")
        for i, three_d_shape in enumerate(self.three_d_shapes):
            print(f"{i + 1}. {three_d_shape}")

    def get_dimensions_for_shape(self, shape):
        dimensions = []
        if shape == 0:  # Square
            side = float(input("Enter the side length: "))
            dimensions.append(side)
        elif shape == 1:  # Rectangle
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            dimensions.extend([length, width])
        elif shape == 2:  # Circle
            radius = float(input("Enter the radius: "))
            dimensions.append(radius)
        elif shape == 3:  # Triangle
            side1 = float(input("Enter the length of side 1: "))
            side2 = float(input("Enter the length of side 2: "))
            side3 = float(input("Enter the length of side 3: "))
            dimensions.extend([side1, side2, side3])
        elif shape == 4:  # Parallelogram
            base = float(input("Enter the base length: "))
            side = float(input("Enter the side length: "))
            dimensions.extend([base, side])
        elif shape == 5:  # Hexagon
            side = float(input("Enter the side length: "))
            dimensions.append(side)
        elif shape in [6, 7, 8, 9]:  # 3D shapes
            if shape == 6:  # Cube
                side = float(input("Enter the side length: "))
                dimensions.append(side)
            elif shape == 7:  # Sphere
                radius = float(input("Enter the radius: "))
                dimensions.append(radius)
            elif shape == 8:  # Cylinder
                radius = float(input("Enter the radius: "))
                height = float(input("Enter the height: "))
                dimensions.extend([radius, height])
            elif shape == 9:  # Pyramid
                base_length = float(input("Enter the base length: "))
                base_width = float(input("Enter the base width: "))
                height = float(input("Enter the height: "))
                dimensions.extend([base_length, base_width, height])
        return dimensions

    def build_compound_shape(self, shape1, dimensions1, shape2, dimensions2):
        area1 = self.calculate_area(shape1, dimensions1)
        area2 = self.calculate_area(shape2, dimensions2)
        perimeter1 = self.calculate_perimeter(shape1, dimensions1)
        perimeter2 = self.calculate_perimeter(shape2, dimensions2)

        total_area = area1 + area2
        total_perimeter = perimeter1 + perimeter2

        print("Compound Shape Area:", total_area)
        print("Compound Shape Perimeter:", total_perimeter)

    def build_three_d_shape(self, shape, dimensions):
        if shape == 0:  # Cube
            side = dimensions[0]
            surface_area = 6 * side * side
            volume = side ** 3
            print("Cube Surface Area:", surface_area)
            print("Cube Volume:", volume)
        elif shape == 1:  # Sphere
            radius = dimensions[0]
            surface_area = 4 * math.pi * radius * radius
            volume = (4 / 3) * math.pi * radius ** 3
            print("Sphere Surface Area:", surface_area)
            print("Sphere Volume:", volume)
        elif shape == 2:  # Cylinder
            radius, height = dimensions
            surface_area = 2 * math.pi * radius * (radius + height)
            volume = math.pi * radius ** 2 * height
            print(f"Cylinder Surface Area: {surface_area:.2f}")
            print(f"Cylinder Volume: {volume:.2f}")
        elif shape == 3:  # Pyramid
            base_length, base_width, height = dimensions
            surface_area = base_length * base_width + 0.5 * base_length * math.sqrt(
                (base_width / 2) ** 2 + height ** 2) + 0.5 * base_width * math.sqrt(
                (base_length / 2) ** 2 + height ** 2)
            volume = (1 / 3) * base_length * base_width * height
            print("Pyramid Surface Area:", surface_area)
            print("Pyramid Volume:", volume)

    def run(self):
        while True:
            print("\nWelcome to the Shape and Space App!")
            print("1. Work with 2D Shape")
            print("2. Work with Compound Shape")
            print("3. Work with 3D Shape")
            print("4. Exit")

            choice = input("Enter your choice (1, 2, 3, or 4): ")

            if choice == '4':
                print("Exiting the Shape and Space App. Goodbye!")
                break

            elif choice == '1':
                self.display_2d_shapes()
                selected_index = int(input("\nEnter the index of the shape you want to work with: ")) - 1

                if 0 <= selected_index < len(self.shapes):
                    dimensions = self.get_dimensions_for_shape(selected_index)
                    area = self.calculate_area(selected_index, dimensions)
                    perimeter = self.calculate_perimeter(selected_index, dimensions)

                    print(f"\nArea of the {self.shapes[selected_index]}: {area}")
                    print(f"Perimeter of the {self.shapes[selected_index]}: {perimeter}")
                else:
                    print("Invalid index selected. Please try again.")

            elif choice == '2':
                self.display_2d_shapes()
                selected_index1 = int(input("\nEnter the index of the first shape: ")) - 1

                if 0 <= selected_index1 < len(self.shapes):
                    selected_index2 = int(input("Enter the index of the second shape: ")) - 1

                    if 0 <= selected_index2 < len(self.shapes):
                        shape1 = self.shapes[selected_index1]
                        dimensions1 = self.get_dimensions_for_shape(selected_index1)

                        shape2 = self.shapes[selected_index2]
                        dimensions2 = self.get_dimensions_for_shape(selected_index2)

                        self.build_compound_shape(selected_index1, dimensions1, selected_index2, dimensions2)
                    else:
                        print("Invalid index for the second shape. Please try again.")
                else:
                    print("Invalid index for the first shape. Please try again.")


            elif choice == '3':

                self.display_3d_shapes()

                selected_index_3d = int(input("\nEnter the index of the 3D shape you want to work with: ")) - 1

                if 0 <= selected_index_3d < len(self.three_d_shapes):

                    dimensions_3d = self.get_dimensions_for_shape(
                        selected_index_3d + 6)

                    self.build_three_d_shape(selected_index_3d, dimensions_3d)

                else:

                    print("Invalid index selected for 3D shape. Please try again.")


            else:
                print("Invalid choice. Please enter a valid option (1, 2, 3, or 4).")


if __name__ == "__main__":
    shape_calculator = ShapeCalculator()
    shape_calculator.run()
