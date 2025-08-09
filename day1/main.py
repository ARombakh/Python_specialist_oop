from date import *

dt1 = Date2025(15, 3)
dt3 = Date2025(7, 7)
# Date2025.init(dt1, 15, 3)
# Date2025.init(dt3, 7, 7)
Date2025.__str__(dt1)

dt2 = Date2025(31, 3)
# Date2025.init(dt2, 31, 3)

Date2025.__str__(dt2)

Date2025.compare_sign(dt1, dt2)

print("dt2 before increment:")
Date2025.__str__(dt2)


print("Print dt2 using str before increment:")
dt2.__str__()

Date2025.add_day(dt2)
dt2.add_day()

print("dt2 after increment using:")
Date2025.__str__(dt2)

print("print(dt2)")
dt2.__str__()

dt2.leap_year()
#print(object.__dict__)
#print(object.__str__)
