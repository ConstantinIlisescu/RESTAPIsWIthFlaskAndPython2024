# special methods also called magic methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def __str__(self) -> str:
    #     return f"name:{self.name} | age: {self.age}"
    
    def __repr__(self) -> str:
        return f"<Person('{self.name}', {self.name})>"
        
# python calls these special methods in some casses
# when you call Person() under the hood python calls Person().__init__

bob = Person("Bob", 35)

print(bob) # by default if class does not contain __str__ will print <__main__.Person object at 0x000001AC9BDB5E50>
print(bob) # by having a custom __str__ method defuined, we print: name:Bob | age: 35
print(bob) # if there is no __str__ defined and you have __repr__ defined you get that as print output. __repr__ will print in debugger by defaut <Person('Bob', Bob)>