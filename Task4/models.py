from abc import ABC, abstractmethod


class Student:
    def __init__(self, full_name, group_number, birth_date=""):
        self.__full_name = full_name
        self.__group_number = group_number
        self.__birth_date = birth_date

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def group_number(self):
        return self.__group_number

    @group_number.setter
    def group_number(self, value):
        self.__group_number = value

    @property
    def birth_date(self):
        return self.__birth_date


# 2. Абстрактний клас УСПІШНІСТЬ
class Performance(ABC):
    def __init__(self):
        self.subjects = []  # Список предметів
        self.scores = []  # Список балів

    def add_subject(self, subject, score):
        self.subjects.append(subject)
        self.scores.append(score)

    @abstractmethod
    def average_score(self):
        pass


# Реальна успішність (для розрахунків)
class RealPerformance(Performance):
    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)


# 3. Клас БАЖАНА_УСПІШНІСТЬ
class DesiredPerformance(Performance):
    def __init__(self, desired_avg_score):
        super().__init__()
        self.target_score = desired_avg_score

    def average_score(self):
        # Повертає бажаний бал, який встановив студент
        return self.target_score


# 4. Клас ДАНІ_СТУДЕНТА (Агрегатор)
class StudentData:
    def __init__(self, student: Student, real_perf: RealPerformance, desired_perf: DesiredPerformance):
        self.student = student
        self.real_perf = real_perf
        self.desired_perf = desired_perf