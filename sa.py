import abc
import math


class Shape(abc.ABC):

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Радиус не должен быть отрицательным")

        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def area_compare(self, other):

        if not isinstance(other, Circle):
            raise TypeError("Нужно сравнивать объекты Circle")

        if self.area() > other.area():
            return (
                f"Круг с радиусом {self.radius} больше "
                f"чем круг с радиусом {other.radius}"
            )

        elif self.area() < other.area():
            return (
                f"Круг с радиусом {self.radius} меньше "
                f"чем круг с радиусом {other.radius}"
            )

        else:
            return "Круги одинаковые"

    def __str__(self):
        return (
            f"Круг(радиус={self.radius}, "
            f"длина окружности={self.perimeter()}, "
            f"площадь={self.area()})"
        )


if __name__ == "__main__":

    def print_menu():
        print("Menu")
        print("1. Длина круга")
        print("2. Площадь круга")
        print("3. Сравнить площади кругов")
        print("0. Выход")

    while True:

        print_menu()

        choice = input("Выберите пункт: ")

        if choice == "1":

            try:
                radius = float(input("Radius: "))

                circle = Circle(radius)

                print(f"Длина окружности: {circle.perimeter()}")

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":

            try:
                radius = float(input("Radius: "))

                circle = Circle(radius)

                print(f"Площадь: {circle.area()}" )

            except ValueError as e:
                print("Ошибка: {e}")

        elif choice == "3":

            try:
                radius1 = float(
                    input("First circle Radius: ")
                )

                radius2 = float(
                    input("Second circle Radius: ")
                )

                circle1 = Circle(radius1)
                circle2 = Circle(radius2)

                print(
                    circle1.area_compare(circle2)
                )

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "0":

            print("Выход из программы")
            break

        else:
            print(f"Неверный пункт")
