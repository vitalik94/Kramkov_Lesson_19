#ДЗ на четверг (Ivanov_Lesson_19.py)
# Класс Company:
# Создайте класс Company
class Company:

# Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста:
# 1:junior, 2:middle, 3:senior, 4:lead.
    levels = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}

# Создайте метод __init__(), внутри которого будут определены два protected свойства: 1) _index - передается параметром
# и 2) _level - принимает из словаря levels значение с ключом _index
    def __init__(self, index):
        self._index = index
        self._level = self.levels[self._index]

# Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def _level_up(self):
        self._index += 1
        self._level = self.levels[self._index]
        return self._index

# Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead(self):
        if self._level == self.levels[4]:
            return print(f'Программист достиг последней квалификации: {self._level}\n')
        else:
            return print(f'Программист не достиг последней квалификации: {self._level}\n')


# Класс Programmer:
# Создайте класс Programmer
class Programmer(Company):

# Создайте метод __init__(), внутри которого будут определены 3 динамических свойства:
# 1) name - передается параметром, является публичным, 2)age - возраст
# 3) level – уровень квалификации на основе словаря из Company
    def __init__(self, name, age, level):

        self.name = name
        self.age = age
        self.level = level
        super().__init__(self.level)

# Создайте метод work(), который заставляет программиста работать,
# что позволяет ему становиться более квалифицированным с помощью метода _level_up() родительского класса
    def work(self):
        self.level = self._level_up()

# Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
    def info(self):
        print(f'имя: {self.name} \nвозраст: {self.age} \nквалификация: {self.level}')

# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию (просто любой текст).
    @staticmethod
    def knowledge_base():
        print('Повышение уровня квалификации программиста\n')


# Вызовите справку по программированию
# Создайте объекты классов Company и Programmer
# Используя объект класса Programmer, повысьте свой уровень квалификации
# Дойдите до уровня lead

Programmer.knowledge_base()
programmer = Programmer('Vitalik', 28, 1)
company = Company(programmer.level)

programmer.info()
programmer.is_lead()
programmer.work()

programmer.info()
programmer.is_lead()
programmer.work()

programmer.info()
programmer.is_lead()
programmer.work()

programmer.info()
programmer.is_lead()






