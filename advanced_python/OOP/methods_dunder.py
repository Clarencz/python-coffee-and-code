# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __del__(self):
#         print("object has being deleted")

# p = Person("meke",34)
# print(p.name)

class vector:  
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        return(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"x:{self.x} y:{self.y}"
    
    def __call__(self):
        print("hello i was called")
    
    # def __len__(self):
    #     return 10
v1 = vector(10,20)
v2 = vector(23,45)
v3 = v1 + v2
# print(v3.x)
# print(v3.y)
# print(v3)

# print(len(v3))
v3()
