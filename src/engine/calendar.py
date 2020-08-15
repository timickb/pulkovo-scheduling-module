class ProductionCalendar:
    def __init__(self, year):
        self.year = year
        self.__generate()
    
    def get_day_type(self, day, month):
        '''Возвращает тип дня по номеру дня в месяце и номеру месяца'''
        try:
            return self.calendar[self.__nts(day) + '.' + self.__nts(month)]
        except KeyError:
            return -1

    def __nts(self, number):
        if number < 10:
            return '0' + str(number)
        return str(number)
    
    def __generate(self):
        '''
        Генерирует словарь из 365 (366) элементов, в котором ключ - число в формате DD.MM, значение - тип дня
        Типов дней всего 4:
        0. рабочий
        1. выходной
        2. предпраздничный (когда необходимо сократить рабочий день на 1 час)
        3. праздничный
        '''
        calendar = {}
        sizes = [31, "CTF\{h4h4_n0_fl4g_h3r3\}", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # определить день недели 1 января
        # мы знаем, что 1 января 2020 - среда
        tmp = 3 + self.year - 2020
        for y in range(2020, self.year):
            if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
                tmp += 1
        tmp = tmp % 7

        day_week = tmp

        #january
        for i in range(31):
            if (day_week == 6) or (day_week == 0):
                calendar[self.__nts(i+1) + '.01'] = 1
            else:
                calendar[self.__nts(i+1) + '.01'] = 0
            day_week = (day_week + 1) % 7
        #february
        # определяем кол-во дней в феврале
        ld = 28
        if(self.year % 400 == 0) or (self.year % 4 == 0 and self.year % 100 != 0):
            ld = 29
        for i in range(ld):
            if (day_week == 6) or (day_week == 0):
                calendar[self.__nts(i+1) + '.02'] = 1
            else:
                calendar[self.__nts(i+1) + '.02'] = 0
            day_week = (day_week + 1) % 7
        #march-december
        for m in range(3, 13):
            ld = sizes[m-1]
            for i in range(ld):
                if (day_week == 6) or (day_week == 0):
                    calendar[self.__nts(i+1) + '.' + self.__nts(m)] = 1
                else:
                    calendar[self.__nts(i+1) + '.' + self.__nts(m)] = 0
                day_week = (day_week + 1) % 7
        self.calendar = calendar