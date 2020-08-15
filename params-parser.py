import xlrd

wb = xlrd.open_workbook('data/params.xlsx')
prog_params = wb.sheet_by_index(0)
room_params = wb.sheet_by_index(1)
teacher_params = wb.sheet_by_index(2)

