class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
        
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconect(self):
        self.connected = False
        print('Disconected.')
        
## Use the class to create an instance of it     
# printer = Device("Printer", "USB")
# print(printer)
# printer.disconect()


## Create another clas that inherits from the parent class
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remain_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remain_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remain_pages -= pages
        
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconect()
printer.print(30)

## if you call printer.disconect() in Printer class:
#       python will check first the Printer class for disconect() method, 
#       if not present, will check the parent class, if not present will check the base object class, 
#       if not present, will return an error