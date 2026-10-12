class parent_Class:
    num = 10

class child_Class(parent_Class):
    pass


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def details(self):
        return self.name

class B:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def details(self):
        return self.name

class C(A, B):
    def __init__(self, name, age):
        A.__init__(self, name, age)
    
    def get_details(self):
        return self.name


class Sub1:
    def first(self):
        print("This is the first function from Sub 1 class")

class Sub2(Sub1):
    def second(self):
        print("This is the second function from the Sub 2 class")

class Super(Sub2):
    def final(self):
        print("This is the final method from the super class")


class Parent:
    def fun1(self):
        print("This is the message from the fun1")

class Child1(Parent):
    def fun2(self):
        print("This is the message from the fun2")

class Child2(Parent):
    def fun3(self):
        print("This is the message from the fun3")


class ParentHybrid:
    def fun1(self):
        print("This is the message from the fun1")

class ChildHybrid(ParentHybrid):
    def fun2(self):
        print("This is the message from the fun2")

class Hybrid(ChildHybrid, ParentHybrid):
    def fun3(self):
        print("This is the message from the fun3")

if __name__ == "__main__":
    print("\n--- Task 1: Single Inheritance ---")
    obj_child = child_Class()
    print("Value of num:", obj_child.num)

    print("\n--- Task 2: Multiple Inheritance ---")
    obj_c = C("Sandhib", 25)
    print("Name from get_details():", obj_c.get_details())

    print("\n--- Task 3: Multilevel Inheritance ---")
    obj_super = Super()
    obj_super.first()
    obj_super.second()
    obj_super.final()

    print("\n--- Task 4: Hierarchical Inheritance ---")
    obj_child2 = Child2()
    obj_child2.fun1()

    print("\n--- Task 5: Hybrid Inheritance ---")
    obj_hybrid = Hybrid()
    obj_hybrid.fun1()
    obj_hybrid.fun2()
    obj_hybrid.fun3()
