class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        id (int): Идентификатор книги.
        name (str): Название книги.
        pages (int): Количество страниц в книге.
    """
    def __init__(self, id_, name, pages):
        """
        Инициализирует новый объект класса Book.

        Args:
            id_ (int): Идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строку в формате "Книга 'название_книги'".

        Returns:
            str: Строковое представление книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает валидную python строку для создания идентичного объекта Book.

        Returns:
            str: Строковое представление объекта Book, которое можно использовать для создания нового объекта.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод str

    print(list_books)  # проверяем метод repr


