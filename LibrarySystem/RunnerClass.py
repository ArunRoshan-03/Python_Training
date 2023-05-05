from LibrarySystem.Library import Library


class RunnerClass:
    my_library = Library()

    my_library.add_book("To Kill a Mockingbird")
    my_library.add_book("1984")
    my_library.add_book("The Great Gatsby")

    my_library.remove_book("1984")

    my_library.add_member("John Smith")
    my_library.add_member("Jane Doe")

    my_library.return_book("To Kill a Mockingbird", "John Smith")

    my_library.lend_book("To Kill a Mockingbird", "John Smith")

    my_library.return_book("To Kill a Mockingbird", "John Smith")

    all_lending_records = my_library.get_lending_records()
