class LetterCount:
    string = input("Enter a string: ")
    letter_count = {}
    lis = [1, 5, 3, 8, 2]
    tup = ()

    def count_letter(self):
        for letter in self.string:
            if letter.isalpha():
                if letter.upper() in self.letter_count:
                    self.letter_count[letter.upper()] += 1
            else:
                self.letter_count[letter.upper()] = 1

        for letter in reversed(self.letter_count):
            print(f"{letter}: {self.letter_count[letter]}")

    def max_min_value(self):
        self.tup = (max(self.lis), min(self.lis))
        print(self.tup)

    def second_min_value(self):
        self.letter_count = sorted(self.lis)
        print(self.letter_count[3])


result = LetterCount()
result.second_min_value()
