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
            print("Первая дата больше второй")    # Первая дата больше второй
        elif(self.month == obj2.month and self.day < obj2.day):
            print("Первая дата больше второй")    # Первая дата больше второй
        elif(self.month > obj2.month):
            print("Вторая дата больше первой")    # Вторая дата больше первой
        elif(self.month == obj2.month and self.day > obj2.day):
            print("Вторая дата больше первой")    # Вторая дата больше первой
        elif(self.day == obj2.day and self.month == obj2.month):
            print("Даты равны")

    # Добавляет к дате 1 день
    def add_day(obj):
        final_day = obj.months[obj.month]
        if obj.month == 12 and obj.day == final_day:
            raise TypeError("Дата выходит за пределы 2025 года")
        elif(obj.day == final_day):
            obj.month += 1
            obj.day = 1
        else:
            obj.day += 1


dt1 = Date2025(15, 3)
dt3 = Date2025(7, 7)
# Date2025.init(dt1, 15, 3)
# Date2025.init(dt3, 7, 7)
Date2025.__str__(dt1)

dt2 = Date2025(31, 3)

# Date2025.init(dt2, 31, 3)
Date2025.__str__(dt2)
"""
print(dt2 is dt1)

print("1 объект день напрямую " + str(dt1.day))
print("2 объект день напрямую " + str(dt2.day))
"""
Date2025.compare_sign(dt1, dt2)

print("dt2 before increment:")
Date2025.__str__(dt2)

Date2025.add_day(dt2)
dt2.add_day()

print("dt2 after increment:")
Date2025.__str__(dt2)


print("print(dt2)")
print(dt2.__str__())

#print(object.__dict__)
#print(object.__str__)

