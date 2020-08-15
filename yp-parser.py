import xlrd

class Workshop:
    def __init__(self, title, start_date, end_date, classroom):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.classroom = classroom

def parse_workshops(text):
    result = []
    return result


wb = xlrd.open_workbook('data/year_plan.xlsx')
sheet = wb.sheet_by_index(0)

WEEKS_AMOUNT = 53

start_col = 6
start_row = 5
current_row = start_row

groups = {}

try:
    while len(sheet.cell(current_row, start_col).value) != 0:
        try:
            group_name = sheet.cell(current_row, start_col).value
        except IndexError:
            break
        groups[group_name] = ['']*WEEKS_AMOUNT

        counter = 0
        for current_col in range(start_col + 2, start_col + WEEKS_AMOUNT, 2):
            groups[group_name][counter] = sheet.cell(current_row, current_col).value
            counter += 1
        current_row += 2
except IndexError:
    pass

print(groups)