from multipledispatch import dispatch

# Method Overloading using multipledispatch
print("=== Method Overloading (multipledispatch) ===")

class Greeter:
    @dispatch()
    def greet(self):
        print("Hello!")

    @dispatch(str)
    def greet(self, name):
        print(f"Hello, {name}!")

    @dispatch(int)
    def greet(self, number):
        print(f"Hello, number {number}!")

g = Greeter()
g.greet()         
g.greet("Alice")  
g.greet(123)      

print("\n")


# --------------------------
#  Method Overriding
# --------------------------
print("=== Method Overriding ===")

class Parent:
    def speak(self):
        print("Parent speaking")

class Child(Parent):
    def speak(self):
        print("Child speaking (overrides Parent)")

p = Parent()
c = Child()
p.speak()
c.speak()

print("\n")


# --------------------------
#  Method Resolution Order (MRO)
# --------------------------
print("=== Method Resolution Order (MRO) ===")

class A:
    def who(self):
        print("I am A")

class B(A):
    def who(self):
        print("I am B")

class C(A):
    def who(self):
        print("I am C")

class D(B, C):
    pass

d = D()
d.who() 

print("MRO:", [cls.__name__ for cls in D.__mro__])

