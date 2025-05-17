class Student:
    # Создаем нового студента с именем, id и пустым списком оценок
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    # Метод для добавления оценки
    def add_grade(self, grade):
        # Проверяем, что оценка от 0 до 10
        if 0 <= grade <= 10:
            self.grades.append(grade)
            print(f"Оценка {grade} добавлена.")
        else:
            print("Ошибка: оценка должна быть от 0 до 10.")

    # Метод для подсчета среднего балла
    def get_average(self):
        if len(self.grades) == 0:
            return 0  # если оценок нет, возвращаем 0
        return sum(self.grades) / len(self.grades)

    # Метод для отображения информации о студенте
    def display_info(self):
        print("Информация о студенте:")
        print(f"Имя: {self.name}")
        print(f"ID студента: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")

    # Магический метод __str__ — возвращает строку при вызове str(student)
    def __str__(self):
        return f"Студент {self.name} (ID: {self.student_id})"

    # Магический метод __eq__ — сравнивает студентов по student_id
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    # Магический метод __len__ — возвращает количество оценок
    def __len__(self):
        return len(self.grades)

# Пример использования:
student1 = Student("Рамадан", "1032240722")
student2 = Student("Аня", "1056789012")
student3 = Student("Рамадан", "1032240722")  # такой же ID как у student1

print(student1)  # вызов __str__
print(student2)  # вызов __str__

print(student1 == student2)  # сравнение по ID (__eq__)
print(student1 == student3)  

student1.add_grade(8)
student1.add_grade(7)
print(f"Количество оценок у {student1.name}: {len(student1)}")  # вызов __len__