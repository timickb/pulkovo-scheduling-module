import xlrd
import sys

def parse_classroom_params(config):
    filename = config['data_storage_path']

    wb = xlrd.open_workbook(filename + '/params.xlsx')
    sheet = wb.sheet_by_index(1)

    classrooms = {}

    start_row = 1
    cols_amount = 6
    current_row = start_row
    while len(sheet.cell(current_row, 0).value) != 0:
        pass
    

def parse_year_plan(config):
    filename = config['data_storage_path']

    wb = xlrd.open_workbook(filename + '/year_plan.xlsx')
    sheet = wb.sheet_by_index(0)

    WEEKS_AMOUNT = 53

    start_col = 6
    start_row = 5
    current_row = start_row

    plan = {}

    try:
        while len(sheet.cell(current_row, start_col).value) != 0:
            try:
                group_name = sheet.cell(current_row, start_col).value
            except IndexError:
                break
            plan[group_name] = ['']*WEEKS_AMOUNT

            counter = 0
            for current_col in range(start_col + 2, start_col + WEEKS_AMOUNT, 2):
                plan[group_name][counter] = sheet.cell(current_row, current_col).value
                counter += 1
            current_row += 2
    except IndexError:
        pass

    return plan