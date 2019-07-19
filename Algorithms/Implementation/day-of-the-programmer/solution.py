def dayOfProgrammer(year):
    if year == 1918: return "26.09.1918"
    return "12.09.{0}".format(year) if (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))) or (year < 1918 and year % 4 == 0) else "13.09.{0}".format(year)
