
class Book:
    def __init__(self, name, author):
        """
            Создание и подготовка к работе объекта "Книга"
            Аргументы:
            :param name: название книги
            :param author: автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        """
               Метод возвращает название книги
        """
        return f"'{self.name}' by {self.author}"

    def __repr__(self):
        """
                      Метод возвращает  валидную python строку,
                      по которой можно инициализировать точно такой же экземпляр
        """
        return f"Book('{self.name}', '{self.author}')"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        """
            Создание и подготовка к работе объекта "Бумажная книга"
            Аргументы:
            :param name: название книги
            :param author: автор книги
            :param pages: количество страниц в книге
        """
        super().__init__(name, author)
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = value

    def __str__(self):
        """
                       Метод возвращает название буиажной книги
        """
        return f"'{self.name}' by {self.author}, {self.pages} pages"

    def __repr__(self):
        """
                      Метод возвращает  валидную python строку,
                      по которой можно инициализировать точно такой же экземпляр
        """
        return f"PaperBook('{self.name}', '{self.author}', {self.pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        """
                  Создание и подготовка к работе объекта "Аудио книга"
                  Аргументы:
                  :param name: название книги
                  :param author: автор книги
                  :param duration: продолжительность
           """
        super().__init__(name, author)
        if not isinstance(duration, (int, float)) or duration <= 0:
            raise ValueError("Duration must be a positive number")
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Duration must be a positive number")
        self._duration = value

    def __str__(self):
        """
                       Метод возвращает название аудио книги
        """
        return f"'{self.name}' by {self.author}, {self.duration} hours"

    def __repr__(self):
        """
                      Метод возвращает  валидную python строку,
                      по которой можно инициализировать точно такой же экземпляр
        """
        return f"AudioBook('{self.name}', '{self.author}', {self.duration})"