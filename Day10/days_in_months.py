def is_leap(year):
    if not year % 4 == 0:
        return False
    else:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif not year % 100 == 0:
            return True
        else:
            return False


def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days = month_days[month - 1]
  leap = is_leap(year)
  if leap and month == 2:
    return days + 1
  else:
    return days


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
