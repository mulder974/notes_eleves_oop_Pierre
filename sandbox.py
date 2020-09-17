from notes import Mark
from eleves import Student


Pierre = Student("Pierre")
Thibault = Student("Thibault")
Clement = Student("Clement")

for e in Student.student_list:
    print(e.name)


note1 = Mark(1,15)
note2 = Mark(1,12)
note3 = Mark(1,13)
note4 = Mark(1,17)

note5 = Mark(2,16)
note6 = Mark(2,15)
note7 = Mark(2,12)
note8 = Mark(2,3)
note9 = Mark(2,17)

for e in Pierre.marks:
    print(e.value)

Pierre.get_average()
Thibault.get_average()

