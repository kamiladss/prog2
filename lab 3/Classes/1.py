class First():
    """getString and printString"""
    def __init__(self):
        self.getSt = ""
          
    def getString(self):
        self.getSt = input()
    def printString(self):
        print(self.getSt.upper())
stroke = First() # connection with class
stroke.getString() 
stroke.printString()