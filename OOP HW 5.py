class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_current_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        """You can estimate lecturer's lesson. Not for finished courses!"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                print(f'Отметка {grade} для лектора {lecturer.name} \n'
                      f'по курсу {course} от студента {self.name} зачтена.\n')
                return
            else:
                lecturer.grades[course] = [grade]
                print(f'Отметка {grade} для лектора {lecturer.name} \n'
                      f'по курсу {course} от студента {self.name} зачтена.\n')
                return
        else:
            return print('Оценка не зачтена, проверьте правильность курсов или лектора.')

    def hw_average_rate(self):
        """You can count an average score of all courses grades"""
        if len(self.grades) == 0:
            return 'У студента нет оценок.'
        else:
            total = 0
            list_len_sum = 0
            for rate_list in self.grades.values():
                list_len_sum += len(rate_list)
                for rate in rate_list:
                    total += rate
            return round(total / list_len_sum, 1)

    def __str__(self):
        """Print information about you other way!"""
        average_rate = self.hw_average_rate()
        fin_course_str = ', '.join(self.finished_courses)
        current_course_str = ', '.join(self.courses_in_progress)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average_rate}\n'
                f'Курсы в процессе обучения: {current_course_str}\n'
                f'Завершенные курсы: {fin_course_str}')

    def __lt__(self, other_student):
        """Check, who is better - you or other student?"""
        if isinstance(other_student, Student) and len(self.grades) > 0 and len(other_student.grades) > 0:
            return (f'Средняя оценка студента {self.name} = {self.hw_average_rate()}. \n'
                    f'Средняя оценка студента {other_student.name} {other_student.hw_average_rate()}\n'
                    f'Студент {self.name} лучше.')
        else:
            return 'У кого то из студентов нет оценок.'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        """You can estimate student's HW. Only for current courses!"""
        if isinstance(student, Student) and course in self.courses_attached\
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                print(f'Отметка {grade} для студента {student.name} \n'
                      f'по курсу {course} от ревьюера {self.name} зачтена.\n')
            else:
                student.grades[course] = [grade]
                print(f'Отметка {grade} для студента {student.name} \n'
                      f'по курсу {course} от ревьюера {self.name} зачтена.\n')
        else:
            print(f'Ошибка. {self.name} не является Ревьюером.')
            return


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lesson_average_rate(self):
        """You can count an average score of all courses grades"""
        if len(self.grades) == 0:
            return 'У лектора нет оценок.'
        else:
            total = 0
            list_len_sum = 0
            for rate_list in self.grades.values():
                list_len_sum += len(rate_list)
                for rate in rate_list:
                    total += rate
            return round(total / list_len_sum, 1)

    def __str__(self):
        """Print information about you other way!"""
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.lesson_average_rate()}')
        return res

    def __lt__(self, other_lecturer):
        """Check, who is better - you or other lecturer?"""
        if isinstance(other_lecturer, Lecturer) and len(self.grades) > 0 and len(other_lecturer.grades) > 0:
            return (f'Средняя оценка лектора {self.name} = {self.lesson_average_rate()}. \n'
                    f'Средняя оценка лектора {other_lecturer.name} {other_lecturer.lesson_average_rate()}\n'
                    f'Лектор {self.name} лучше.')
        else:
            return 'У кого то из лекторов нет оценок.'


class Reviewer(Mentor):
    def __str__(self):
        """Print information about you other way!"""
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}')
        return res


# STUDENTS

stepan_student = Student('Stepan', 'Tsiglevkin', 'male')
stepan_student.add_current_courses('python')
stepan_student.add_finished_courses('GIT')

ivan_student = Student('Ivan', 'Polevoy', 'male')
ivan_student.add_current_courses('python')
ivan_student.add_finished_courses('GIT')

# LECTURERS

nikolay = Lecturer('Nikolay', 'Brezhnev')
nikolay.courses_attached.append('python')
nikolay.courses_attached.append('english')

aleksey = Lecturer('Aleksey', 'Gagarin')
aleksey.courses_attached.append('GIT')

# REVIEWERS

lubov = Reviewer('Lubov', 'Gotman')
lubov.courses_attached.append('python')

aleksandr = Reviewer('Aleksandr', 'Great one')
aleksandr.courses_attached.append('GIT')


students_list = [stepan_student, ivan_student]
lecturers_list = [aleksey, nikolay]


def st_course_average(some_list, course):
    """You can see the average score of some course for students"""
    total_rate = []
    for person in some_list:
        if not isinstance(person, Student):
            return f'{person} не студент.'
        else:
            if course in person.grades:
                total_rate += person.grades[course]
    res = round(sum(total_rate) / len(total_rate), 2)
    print(f'Средняя оценка студентов по курсу {course} = {res}.')
    return


def lecturer_course_average(some_list, course):
    """You can see the average score of some course from lecturers"""
    total_rate = []
    for person in some_list:
        if not isinstance(person, Lecturer):
            print(f'{person} не лектор.')
            return
        else:
            if course in person.grades:
                total_rate += person.grades[course]
    res = round(sum(total_rate) / len(total_rate), 2)
    print(f'Средняя оценка лекторов по курсу {course} = {res}.')
    return


# Testing
# estimate each other. # Важно - чтобы уведомления не выводились - return без print.

# stepan_student.rate_lecturer(nikolay, 'python', 10)
# stepan_student.rate_lecturer(nikolay, 'python', 7)
#
# ivan_student.rate_lecturer(nikolay, 'python', 2)
# ivan_student.rate_lecturer(nikolay, 'python', 10)
#
# lubov.rate_hw(stepan_student, 'python', 5)
# lubov.rate_hw(stepan_student, 'python', 9)
# lubov.rate_hw(ivan_student, 'python', 9)
# lubov.rate_hw(ivan_student, 'python', 2)
#
# print()

# print(stepan_student, ivan_student, aleksey, nikolay, lubov, aleksandr, sep='\n\n')

# print(stepan_student < ivan_student)
# print(aleksey < nikolay)

# lecturer_course_average(lecturers_list, 'python')
# st_course_average(students_list, 'python')
