class Student:
    def __init__(self, rollNumber, Name, marks1, marks2):
        self.Name = Name
        self.rollNumber = rollNumber
        self.marks1 = marks1
        self.marks2 = marks2

    def accept(self, rollNumber, Name, marks1, marks2):
        object = Student( rollNumber, Name, marks1, marks2)
        list.append(object)

    def display(self, object):
        print("Roll Number: ", object.rollNumber)
        print("Name: ", object.Name)
        print("Marks1: ", object.marks1)
        print("Marks2: ", object.marks2)

    def search(self, roll):
        for i in range(list.__len__()):

            if list[i].rollNumber == roll:
                return i
        return -1

    # Delete Function
    def delete(self, rn):
        i = self.search(rn)
        del list[i]

    # Update Function
    def update(self, rn, No):
        i = self.search(rn)
        rollNumber = No
        list[i].rollNumber = rollNumber


list = []
rollNumber = 0
obj = Student(0,'',0,0)
while (True):
    print("\nOperations used, ")
    print("1.Accept Student details\n2.Display Student Details\n"
          + "3.Search Details of a Student\n4.Delete Details of Student"
          + "\n5.Update Student Details\n6.Exit")
    ch = int(input("Enter the Choices: "))
    if ch == 1:
        Name = input("Enter the Name: ")
        rollNumber += 1
        marks1 = int(input("enter the marks1: "))
        marks2 = int(input("Enter the marks2: "))
        obj.accept(rollNumber,Name,marks1,marks2)
    elif ch == 2:
        print("\nList of Students\n")
        for i in range(list.__len__()):
            obj.display(list[i])
    elif ch==3 :
        roll=int(input("enter Roll number of Student to be Searched: "))
        s=obj.search(roll)
        if s != -1 :
            obj.display(list[s])
    elif ch==4:
        roll=int(input("enter Roll number of Student to be Deleted: "))
        obj.delete(roll)
    elif ch == 5 :
        oroll = int(input("enter Old Roll number of Student to be Updated: "))
        nroll = int(input("enter New Roll number of Student to be Searched: "))
        obj.update(oroll,nroll)
    elif ch==6 :
        print("Thank You !!")
        exit()



