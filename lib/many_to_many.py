class Book:
    all: list["Book"] = []

    def __init__(self, title: str):
        self.title = title
        Book.all.append(self)

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise Exception("title must be a non-empty string")
        self._title = value.strip()

    def contracts(self) -> list["Contract"]:
        return [c for c in Contract.all if c.book is self]

    def authors(self) -> list["Author"]:
        seen = set()
        result: list["Author"] = []
        for c in self.contracts():
            if c.author not in seen:
                seen.add(c.author)
                result.append(c.author)
        return result

    def __repr__(self) -> str:
        return f"Book(title={self.title!r})"


class Author:
    all: list["Author"] = []

    def __init__(self, name: str):
        self.name = name
        Author.all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise Exception("name must be a non-empty string")
        self._name = value.strip()

    def contracts(self) -> list["Contract"]:
        return [c for c in Contract.all if c.author is self]

    def books(self) -> list["Book"]:
        seen = set()
        result: list["Book"] = []
        for c in self.contracts():
            if c.book not in seen:
                seen.add(c.book)
                result.append(c.book)
        return result

    def sign_contract(self, book: "Book", date: str, royalties: int) -> "Contract":
        return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self) -> int:
        return sum(c.royalties for c in self.contracts())

    def __repr__(self) -> str:
        return f"Author(name={self.name!r})"


class Contract:
    all: list["Contract"] = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self) -> Author:
        return self._author

    @author.setter
    def author(self, value: Author) -> None:
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    @property
    def book(self) -> Book:
        return self._book

    @book.setter
    def book(self, value: Book) -> None:
        if not isinstance(value, Book):
            raise Exception("book must be a Book instance")
        self._book = value

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise Exception("date must be a non-empty string")
        self._date = value.strip()

    @property
    def royalties(self) -> int:
        return self._royalties

    @royalties.setter
    def royalties(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise Exception("royalties must be a non-negative int")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date: str) -> list["Contract"]:
        if not isinstance(date, str) or not date.strip():
            raise Exception("date must be a non-empty string")
        d = date.strip()
        return [c for c in cls.all if c.date == d]

    def __repr__(self) -> str:
        return (
            f"Contract(author={self.author.name!r}, "
            f"book={self.book.title!r}, date={self.date!r}, royalties={self.royalties})"
        )
