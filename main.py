from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import arrow

def main():
    print("Дата и время: ",arrow.now().format("YYYY-MM-DD HH:mm:ss"),"\n")
    r = Rectangle("синего", 5, 5)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()