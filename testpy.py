#initializing class
class Book:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author

    def get_details(self):
        return f"Title: {self.__title}, Author: {self.__author}"

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author 
#subclasses
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return super().get_details()

class PrintedBook(Book):
    def __init__(self, title, author, weight):
        super().__init__(title, author)
        self.__weight = weight
    
    def get_details(self):
         return f"{super().get_details()}, Weight: {self.__weight}g"

#Creating objects
ebook1 = Ebook("Digital Fortress", "Dan Brown", 2)
printed1 = PrintedBook("1984", "George Orwell", 300)

print(ebook1.get_details())
print(printed1.get_details())

#Activity 2

class Cheetahs:
    def speed(self):
        return "120 mph"
class leopards:
    def speed(self):
        return "36 mph"

for animals in [Cheetahs(), leopards()]:
    print(animals)
