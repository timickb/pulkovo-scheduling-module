class Classroom:
    def __init__(self, name, capacity, activity_type, configuration, priority, fitsto):
        self.name = name
        self.capacity = capacity
        self.activity_type = activity_type
        self.configuration = configuration
        self.priority = priority
        self.fitsto = fitsto
    
    def __str__(self):
        return self.name