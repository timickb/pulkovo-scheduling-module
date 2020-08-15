import xlrd
import sys
from src.models.classroom import Classroom
from src.models.program import StudyProgram
from src.models.teacher import Teacher

class Parser:
    def __init__(self, config):
        self.config = config
    
    def __parse_teacher_priority(self, text):
        return 0
    
    def __parse_teacher_ability(self, text):
        return 0
    
    def __parse_teacher_workplan(self, text):
        return 0
    
    def __parse_teacher_changeplan(self, text):
        return 0

    def parse_teacher_params(self):
        filename = self.config['data_storage_path']

        wb = xlrd.open_workbook(filename + '/params.xlsx')
        sheet = wb.sheet_by_index(1)

        teachers = []

        current_row = 1
        while len(sheet.cell(current_row, 0).value) != 0:
            t_id = sheet.cell(current_row, 0).value
            t_name = sheet.cell(current_row, 1).value
            t_discipline = sheet.cell(current_row, 2).value.split(';') # list
            t_programs = sheet.cell(current_row, 3).value.split(';') # list
            t_priority = self.__parse_teacher_priority(sheet.cell(current_row, 4).value)
            t_ability = self.__parse_teacher_ability(sheet.cell(current_row, 5).value)
            t_workplan = self.__parse_teacher_workplan(sheet.cell(current_row, 4).value)
            t_changeplan = self.__parse_teacher_changeplan(sheet.cell(current_row, 4).value)    
            teachers.append(Teacher(t_id, t_name, t_discipline, t_programs, t_priority, t_ability, t_workplan, t_changeplan))
        
        return teachers
        

    def parse_classroom_params(self):
        filename = self.config['data_storage_path']

        wb = xlrd.open_workbook(filename + '/params.xlsx')
        sheet = wb.sheet_by_index(1)

        classrooms = []

        current_row = 1
        while len(sheet.cell(current_row, 0).value) != 0:
            cr_number = sheet.cell(current_row, 0).value
            cr_capacity = sheet.cell(current_row, 1).value
            cr_activity = sheet.cell(current_row, 2).value
            cr_configuration = sheet.cell(current_row, 3).value
            cr_priority = sheet.cell(current_row, 4).value
            cr_fitsto = sheet.cell(current_row, 5).value
            classrooms.append(Classroom(cr_number, cr_capacity, cr_activity, cr_configuration, cr_priority, cr_fitsto))
        
        return classrooms
        

    def parse_year_plan(self):
        filename = self.config['data_storage_path']

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