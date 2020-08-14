import xlrd

wb = xlrd.open_workbook('data/year_plan.xlsx')
sheet = wb.sheet_by_index(0)


startCol = 6
startRow = 5
currentRow = 5

groups = []

try:
    while sheet.cell(currentRow, startCol).value != "":
        groups.append(sheet.cell(currentRow, startCol).value)
        currentRow += 2
except IndexError:
    pass

print(groups)