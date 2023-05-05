class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.lending_records = []

    def add_book(self, book):
        print()
        self.books.append(book)
        print(f"Book was added successfully '{book}'")

    def remove_book(self, book):
        print()
        self.books.remove(book)
        print(f"Book was remove successfully '{book}' in library")
        print(f"Total Book available '{self.books}' in library")

    def add_member(self, member):
        print()
        self.members.append(member)
        print(f"Libray member was added successfully '{member}'")

    def remove_member(self, member):
        print()
        self.members.remove(member)
        print(f"Libray member was removed successfully '{member}'")

    def lend_book(self, book, member):
        lending_record = {'book': book, 'member': member}
        self.lending_records.append(lending_record)

    def return_book(self, book, member):
        print()
        for record in self.lending_records:
            if record['book'] == book:
                print(f"the book'{record}' was returned by '{member}'")
                return record

    def get_lending_records(self):
        print()
        print(f"Lending books records list : '{self.lending_records}'")
        return self.lending_records
