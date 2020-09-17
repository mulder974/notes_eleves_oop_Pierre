import eleves
 
class Mark:
    id = 1

    def __init__(self,student_id:int,valeur:int):
        self.id = Mark.id
        self.id_eleve = student_id
        self.value = valeur

        for student in eleves.Student.student_list:
            if student.id == self.id_eleve:
                student.marks.append(self)

        Mark.id +=1 




