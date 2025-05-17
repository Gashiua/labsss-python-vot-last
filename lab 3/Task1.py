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

    
    def display_info(self):
        print("Информация о студенте:")
        print(f"Имя: {self.name}")
        print(f"ID студента: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")

# Пример использования:
student1 = Student("Рамадан", "1032240722")
student1.add_grade(8)
student1.add_grade(11)  # неправильная оценка
student1.add_grade(4)
student1.display_info()