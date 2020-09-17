class Student:

    student_list=[]

    id = 1 
    def __init__(self, name:str):
        
        self.id = Student.id
        self.name = name
        self.marks = []
        Student.student_list.append(self)
        Student.id += 1

    def get_average(self):
        sum=0
        print(f"les notes de {self.name} sont :")
        for mark in self.marks:
            print(mark.value)
            sum += mark.value
        print("Sa moyenne est donc de :", sum / len(self.marks))
        
