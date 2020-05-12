class Date(object):

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        return f"{day}-{month}-{year}"

    @staticmethod
    def valid(date_string):
        day, month, year = map(int, date_string.split('-'))
        try:
            if not 1 <= day <= 31:
                return f'Error'
            elif not 1 <= month <= 12:
                return f'Error'
            elif not year < 2020:
                return f'Error'
        except ValueError:
            return False
        return f"{day}-{month}-{year}"


print(Date.valid('20-13-2019'))
print(Date.from_string('15-02-2017'))


