class Date2025:
    year = 2025
    count = 0
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # Инициализирует дату
    def __init__(self, day, month):
        self.day = day
        self.month = month
        Date2025.count += 1

    # Печатает дату
    def __str__(self):
        print(str(self.day).zfill(2) + "-"
              + str(self.month).zfill(2) + "-"
              + str(self.year))

    # Сравнивает даты
    def compare_bool(obj1, obj2):
        print(obj1.day == obj2.day and obj1.month == obj2.month)

    # Сравнивает даты
    def compare_sign(self, obj2):
        if self.month < obj2.month:
            print("Первая дата больше второй")
            # Первая дата больше второй
        elif(self.month == obj2.month and self.day < obj2.day):
            print("Первая дата больше второй")
            # Первая дата больше второй
        elif(self.month > obj2.month):
            print("Вторая дата больше первой")
            # Вторая дата больше первой
        elif(self.month == obj2.month and self.day > obj2.day):
            print("Вторая дата больше первой")
            # Вторая дата больше первой
        elif(self.day == obj2.day and self.month == obj2.month):
            print("Даты равны")

    # Добавляет к дате 1 день
    def add_day(self):
        final_day = self.months[self.month]
        if self.month == 12 and self.day == final_day:
            raise TypeError("Дата выходит за пределы 2025 года")
        elif(self.day == final_day):
            self.month += 1
            self.day = 1
        else:
            self.day += 1

    def leap_year(self):
        if (self.year % 4 == 0):
            print("Год " + str(self.year) + " является високосным")
        else:
            print("Год " + str(self.year) + " не является високосным")