
class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def student_has_name(self):
        return self.name

    def student_has_cohort(self):
        return self.student.cohort

    def student_can_update_name(self, name):
        return self.student.name

    def student_can_change_cohort(self, cohort):
        return self.student.cohort

    def talk(self):
        return "I can talk!" 

    def say_favourite_language(self):
        return f"I love {Python}"

    

    

