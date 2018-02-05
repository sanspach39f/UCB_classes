"""
This is just a dummy file - not really meant to be used
for other programs.
"""


#1)
"""
Write a simple Rectangle class. It should do the following:

Accepts length and width as parameters when creating a new instance
Has a perimeter method that returns the perimeter of the rectangle
Has an area method that returns the area of the rectangle
Don't worry about coordinates or negative values, etc.
"""
class Rectangle:
    @classmethod
    def tacobell(cls):
        print("fuck penis")
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2*(self.length+self.width)
    def area(self):
        return self.length*self.width

#2)
"""
Python provides several modules to allow you to easily extend 
some of the basic objects in the language. Among these modules 
are UserDict, UserList, and UserString. (Refer to the chart in 
Topic 10.3 to see what the methods you need to override look like. 
Also, since UserDict and UserList are part of the collection module, 
you can import them using from collections import UserDict and 
from collections import UserList.)

2. Using the UserList module, create a class called Ulist, and 
override the __add__, append, and extend methods so that duplicate 
values will not be added to the list by any of these operations.

"""    
from collections import UserList

class Ulist(UserList):
    def __init__(self,r=None):
        super().__init__(r)
        
    def __add__(self, other):
        """Overridden __add__ method - duplicates not allowed"""
        
        if other not in self:
            return super().__add__(other)
        else:
            return "Cannot add duplicate values"   
        
    def append(self, other):
        """Overridden append method - duplicates not allowed"""        
        if other not in self:
            super().append(other)
        else:
            return "Cannot add duplicate values"  
                
    def extend(self, other):
        """Overridden extend method - duplicates not allowed"""        
        if other not in self:
            super().extend([other])
        else:
            return "Cannot add duplicate values"         

    