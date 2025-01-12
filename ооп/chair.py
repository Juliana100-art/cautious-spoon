# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Candy:
    def __init__(self, weight_candy: float, form_candy: str):
        if not isinstance(weight_candy, (int, float)):
            raise TypeError("Масса конфеты должна быть типа int или float")
        if weight_candy <= 0:
            raise ValueError("Масса конфеты должна быть положительным числом")
        self.weight_candy = weight_candy

        if not isinstance(form_candy, (str)):
            raise TypeError("Форма конфеты должна быть str")
        self.form_candy = form_candy

    def candy_exists(self) -> bool:
      def candy_foaming(self, caramel: float, water=None) -> None:

        if not isinstance(caramel, (int, float)):
            raise TypeError("Конфета с карамелью должна быть типа int или float")
        if water < 0:
            raise ValueError("Конфета с карамелью должна быть положительным числом")

    def melting_and_adding_extra_candy(self, extra_candy: float) -> None:
        if __name__ == "__main__":
            doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
