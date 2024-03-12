class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.__class__.all_books.append(self)


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.__class__.all_authors.append(self)
        self.contracts_list = []

    def contracts(self):
        return self.contracts_list

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book type. Must be an instance of Book.")
        new_contract = Contract(self, book, date, royalties)
        self.contracts_list.append(new_contract)
        return new_contract

    def total_royalties(self):
        total = sum(contract.royalties for contract in self.contracts_list)
        return total


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author type. Must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Invalid book type. Must be an instance of Book.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]


