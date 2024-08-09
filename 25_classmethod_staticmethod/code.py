# a method is a function that starts with def word and has self as first paramether (instance method)
class ClassTest:
    def instances_method(self):
        print(f"Called instance_method of {self}")
        
    @classmethod
    def class_method(cls): # convention to cal the param cls and will be the class itself
        print(f"Called instance_method of {cls}")
        
    @staticmethod
    def static_method():
        print("Called static_method")

# to call an instance method
test = ClassTest()
test.instances_method() # shorthand of ClassTest.instances_method(test)
        
# to call a class method you call the class itself not the instance
ClassTest.class_method() # under the hood this wil call ClassTest.class_method(ClassTest)

# to call a static method. Nothing will be passed to the method by default.
ClassTest.static_method()


##################################################################################################
# @classmethod could be used as factory

class Book:
    TYPES = ("hardcover","paperback") # variable and it become class properties that can be accesed like Book.TYPES
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weight {self.weight}g>"
    
    # use cls insted of Book in the return
    # @classmethod
    # def hardcover(cls, name, page_weight):
    #     return Book(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 100)
        
    
book = Book("Harry Potter", "hardcover", 1500)
print(book)

book_using_factory = book.hardcover("Harry Potter", 1300)
print(book_using_factory)

light_book_using_factory = book.paperback("Python 101", 600)
print(light_book_using_factory)