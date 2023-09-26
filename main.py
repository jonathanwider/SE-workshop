from rectangle import  Rectangle
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    rect = Rectangle(2.0, 2.5)
    print(f"width {rect.width}")
    print(f"height {rect.height}")
    print(f"area {rect.area}")
    print(f"perimeter {rect.perimeter}")
    print("---")
    rect.width = 2.5
    print(f"width {rect.width}")
    print(f"height {rect.height}")
    print(f"area {rect.area}")
    print(f"perimeter {rect.perimeter}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
