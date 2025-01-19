


class AbstractStructure(ABC):
    """
    Абстрактный класс, представляющий общую структуру.

    Атрибуты:
        material (str): Материал, из которого сделана структура.
        dimensions (Tuple[float, float]): Размеры структуры (ширина, высота) в метрах.
    """

    def __init__(self, material: str, dimensions: Tuple[float, float]):
        """
        Конструктор для создания объекта AbstractStructure.

        Args:
            material (str): Материал, из которого сделана структура.
            dimensions (Tuple[float, float]): Размеры структуры (ширина, высота) в метрах.
                Ширина и высота должны быть положительными.

        Raises:
            ValueError: Если ширина или высота не являются положительными числами.
        """
        if dimensions[0] <= 0 or dimensions[1] <= 0:
            raise ValueError("Размеры должны быть положительными числами.")
        self.material = material
        self.dimensions = dimensions

    def get_area(self) -> float:
        """
        Абстрактный метод для получения площади структуры.

        Returns:
            float: Площадь структуры в квадратных метрах.
        """
        ...

    def get_description(self) -> str:
        """
        Абстрактный метод для получения описания структуры.

        Returns:
            str: Описание структуры.
        """
        ...


class Door(AbstractStructure):
    """
    Класс, представляющий дверь.

    Атрибуты:
        material (str): Материал, из которого сделана дверь.
        dimensions (Tuple[float, float]): Размеры двери (ширина, высота) в метрах.
        is_open (bool): Открыта ли дверь.
    """

    def __init__(self, material: str, dimensions: Tuple[float, float], is_open: bool = False):
        """
        Конструктор для создания объекта Door.

        Args:
            material (str): Материал, из которого сделана дверь.
            dimensions (Tuple[float, float]): Размеры двери (ширина, высота) в метрах.
            is_open (bool): Открыта ли дверь. По умолчанию False.
        """
        super().__init__(material, dimensions)
        self.is_open = is_open

    def open(self) -> None:
        """
        Открывает дверь.

        Returns:
            None

        Examples:
            >>> door = Door("wood", (0.9, 2.1))
            >>> door.is_open
            False
            >>> door.open()
            >>> door.is_open
            True
        """
        self.is_open = True

    def close(self) -> None:
        """
        Закрывает дверь.

        Returns:
            None
        """
        self.is_open = False

    def get_area(self) -> float:
        """
        Возвращает площадь двери.

        Returns:
            float: Площадь двери в квадратных метрах.
        """
        return self.dimensions[0] * self.dimensions[1]

    def get_description(self) -> str:
        """
        Возвращает описание двери.

        Returns:
            str: Описание двери.
        """
        status = "открыта" if self.is_open else "закрыта"
        return f"Дверь из {self.material}, размером {self.dimensions[0]}x{self.dimensions[1]} м, {status}."


class Window(AbstractStructure):
    """
    Класс, представляющий окно.

    Атрибуты:
        material (str): Материал, из которого сделано окно.
        dimensions (Tuple[float, float]): Размеры окна (ширина, высота) в метрах.
        is_open (bool): Открыто ли окно.
    """

    def __init__(self, material: str, dimensions: Tuple[float, float], is_open: bool = False):
        """
        Конструктор для создания объекта Window.

        Args:
            material (str): Материал, из которого сделано окно.
            dimensions (Tuple[float, float]): Размеры окна (ширина, высота) в метрах.
            is_open (bool): Открыто ли окно. По умолчанию False.
        """
        super().__init__(material, dimensions)
        self.is_open = is_open

    def open(self) -> None:
        """
        Открывает окно.

        Returns:
            None
        """
        self.is_open = True

    def close(self) -> None:
        """
        Закрывает окно.

        Returns:
            None
        """
        self.is_open = False

    def get_area(self) -> float:
        """
        Возвращает площадь окна.

        Returns:
            float: Площадь окна в квадратных метрах.
        """
        return self.dimensions[0] * self.dimensions[1]

    def get_description(self) -> str:
        """
        Возвращает описание окна.

        Returns:
            str: Описание окна.
        """
        status = "открыто" if self.is_open else "закрыто"
        return f"Окно из {self.material}, размером {self.dimensions[0]}x{self.dimensions[1]} м, {status}."


class Wall(AbstractStructure):
    """
    Класс, представляющий стену.

    Атрибуты:
        material (str): Материал, из которого сделана стена.
        dimensions (Tuple[float, float]): Размеры стены (ширина, высота) в метрах.
        color (str): Цвет стены.
    """

    def __init__(self, material: str, dimensions: Tuple[float, float], color: str):
        """
        Конструктор для создания объекта Wall.

        Args:
            material (str): Материал, из которого сделана стена.
            dimensions (Tuple[float, float]): Размеры стены (ширина, высота) в метрах.
            color (str): Цвет стены.
        """
        super().__init__(material, dimensions)
        self.color = color

    def paint(self, new_color: str) -> None:
        """
        Перекрашивает стену в новый цвет.

        Args:
            new_color (str): Новый цвет стены.

        Returns:
            None
        """
        self.color = new_color

    def get_area(self) -> float:
        """
        Возвращает площадь стены.

        Returns:
            float: Площадь стены в квадратных метрах.
        """
        return self.dimensions[0] * self.dimensions[1]

    def get_description(self) -> str:
        """
        Возвращает описание стены.

        Returns:
            str: Описание стены.
        """
        return f"Стена из {self.material}, размером {self.dimensions[0]}x{self.dimensions[1]} м, цвет {self.color}."
