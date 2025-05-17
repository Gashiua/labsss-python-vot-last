# Создаем класс Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Класс Teacher, который наследует от Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # вызываем конструктор базового класса
        self.subject = subject
        self.students = [] 
    # Метод для добавления студента
    def add_student(self, student):
        self.students.append(student)
        print(f"Студент {student.name} добавлен.")

    # Метод для удаления студента по имени
    def remove_student(self, student_name):
        for s in self.students:
            if s.name == student_name:
                self.students.remove(s)
                print(f"Студент {student_name} удален.")
                return
        print(f"Студент с именем {student_name} не найден.")

    # Метод для вывода всех студентов
    def list_students(self):
        print("Список студентов:")
        for s in self.students:
            print(f"- {s.name}")

# Создаем класс Student 
class Student:
    def __init__(self, name):
        self.name = name

# Пример использования:
teacher1 = Teacher("Юлия", 35, "Русский язык и культура речи")
student1 = Student("Рамадан")
student2 = Student("Андрей")

teacher1.add_student(student1)
teacher1.add_student(student2)

teacher1.list_students()

teacher1.remove_student("Рамадан")
teacher1.list_students()