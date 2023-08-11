class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = sum_rating / len_rating
        return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не наш студент")
            return
        return self.av_rating() < other.av_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = sum_rating / len_rating
        return average_rating

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не наш лектор")
            return
        return self.av_rating() < other.av_rating()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


student1 = Student('Иван', 'Иванов', 'М')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['1С']

student2 = Student('Петр', 'Петров', 'М')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['1С']

lecturer1 = Lecturer('Lecturer', 'Lecturer1')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Lecturer', 'Lecturer2')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Reviewer', 'Reviewer1')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Reviewer', 'Reviewer2')
reviewer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 7)

student1.rate_lw(lecturer1, 'Python', 10)
student1.rate_lw(lecturer1, 'Python', 9)
student1.rate_lw(lecturer1, 'Python', 8)

student2.rate_lw(lecturer2, 'Python', 9)
student2.rate_lw(lecturer2, 'Python', 8)
student2.rate_lw(lecturer2, 'Python', 7)

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]
reviewer_list = [reviewer1, reviewer2]

import gc

print("Эксперты, проверяющие домашние задания")
for obj in gc.get_objects():
    if isinstance(obj, Reviewer):
        print(obj)

print("Лекторы")
for obj in gc.get_objects():
    if isinstance(obj, Lecturer):
        print(obj)

print("Студенты")
for obj in gc.get_objects():
    if isinstance(obj, Student):
        print(obj)

print(student1 < student2)

print(lecturer1 > lecturer2)