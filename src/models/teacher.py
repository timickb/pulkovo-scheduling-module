class Teacher:
    def __init__(self, id, name, discipline, programs, priority, ability, workplan, changeplan):
        self.id = id
        self.name = name
        self.discipline = discipline
        self.programs = programs
        self.priority = priority
        self.ability = ability
        self.workplan = workplan
        self.changeplan = changeplan
    
    def __str__(self):
        return self.name