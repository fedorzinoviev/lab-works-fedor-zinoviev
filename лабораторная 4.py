from abc import ABC, abstractmethod
from typing import Union

class Clothing(ABC):
    """
    Базовый класс для одежды.
    Определяет основные атрибуты и методы, общие для всех предметов одежды.
    """

    def __init__(self, color: str, size: str):
        """
        Конструктор класса Clothing.

        Args:
            color: Цвет одежды.
            size: Размер одежды.
        """
        self.color = color
        self.size = size

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Clothing.
        """
        return f"Clothing(color='{self.color}', size='{self.size}')"

    def __repr__(self) -> str:
        """
        Возвращает представление объекта Clothing для отладки.
        """
        return f"Clothing(color='{self.color}', size='{self.size}')"

    @abstractmethod
    def get_material(self) -> str:
        """
        Абстрактный метод для получения материала одежды.
        Должен быть реализован в дочерних классах.
        """
        pass

    def describe(self) -> str:
        """
        Возвращает общее описание одежды.
        """
        return f"Это предмет одежды, цвет: {self.color}, размер: {self.size}."

    def wash(self, temperature: int) -> str:
        """
        Рекомендует режим стирки для одежды.
        """
        return f"Рекомендуется стирать при температуре не выше {temperature} градусов."

class TShirt(Clothing):
    """
    Класс, представляющий футболку.
    Наследуется от класса Clothing.
    """

    def __init__(self, color: str, size: str, sleeve_length: str):
        """
        Конструктор класса TShirt.
        Расширяет конструктор базового класса Clothing, добавляя атрибут длины рукава.

        Args:
            color: Цвет футболки.
            size: Размер футболки.
            sleeve_length: Длина рукава ("short", "long", "sleeveless").
        """
        super().__init__(color, size)
        self.sleeve_length = sleeve_length

    def __str__(self) -> str:
        """
        Перегружает строковое представление объекта TShirt.
        Добавляет информацию о длине рукава.
        """
        return f"TShirt(color='{self.color}', size='{self.size}', sleeve_length='{self.sleeve_length}')"

    def __repr__(self) -> str:
        """
        Перегружает представление объекта TShirt для отладки.
        Добавляет информацию о длине рукава.
        """
        return f"TShirt(color='{self.color}', size='{self.size}', sleeve_length='{self.sleeve_length}')"

        def get_material(self) -> str:
            """
            Возвращает материал футболки (по умолчанию - хлопок).
            """
            return "Cotton"

        def describe(self) -> str:
            """
            Перегружает метод describe базового класса.
            Добавляет информацию о длине рукава футболки.
            Причина перегрузки: необходимо добавить специфическую информацию о футболке.
            """
            return f"Это футболка, цвет: {self.color}, размер: {self.size}, длина рукава: {self.sleeve_length}."

        def wash(self, temperature: int = 30) -> str:
            """
            Перегружает метод wash базового класса.
            Устанавливает рекомендуемую температуру стирки для футболок (по умолчанию 30 градусов).
            Причина перегрузки: для футболок обычно рекомендуется более низкая температура стирки, чем для других видов одежды.
            """
            return f"Рекомендуется стирать при температуре не выше {temperature} градусов (деликатный режим)."

    class Jeans(Clothing):
        """
        Класс, представляющий джинсы.
        Наследуется от класса Clothing.
        """

        def __init__(self, color: str, size: str, style: str):
            """
            Конструктор класса Jeans.
            Расширяет конструктор базового класса Clothing, добавляя атрибут стиля.

            Args:
                color: Цвет джинсов.
                size: Размер джинсов.
                style: Стиль джинсов (например, "skinny", "straight", "bootcut").
            """
            super().__init__(color, size)
            self.style = style
            self._has_pockets = True  # Инкапсулированный атрибут наличия карманов

        def __str__(self) -> str:
            """
            Перегружает строковое представление объекта Jeans.
            Добавляет информацию о стиле.
            """
            return f"Jeans(color='{self.color}', size='{self.size}', style='{self.style}')"

        def __repr__(self) -> str:
            """
            Перегружает представление объекта Jeans для отладки.
            Добавляет информацию о стиле.
            """
            return f"Jeans(color='{self.color}', size='{self.size}', style='{self.style}')"

        def get_material(self) -> str:
            """
            Возвращает материал джинсов (по умолчанию - деним).
            """
            return "Denim"

        def describe(self) -> str:
            """
            Перегружает метод describe базового класса.
            Добавляет информацию о стиле джинсов.
            Причина перегрузки: необходимо добавить специфическую информацию о джинсах.
            """
            return f"Это джинсы, цвет: {self.color}, размер: {self.size}, стиль: {self.style}."

        def has_pockets(self) -> bool:
            """
            Возвращает информацию о наличии карманов.
            """
            return self._has_pockets

    # Пример использования:
    tshirt = TShirt(color="blue", size="M", sleeve_length="short")
    print(tshirt)
    print(tshirt.get_material())
    print(tshirt.wash())
    print(tshirt.describe())

    jeans = Jeans(color="black", size="L", style="skinny")
    print(jeans)
    print(jeans.get_material())
    print(jeans.has_pockets())
    print(jeans.describe())