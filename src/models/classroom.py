class Classroom:
    def __init__(self, name, capacity, configuration, priority, fitsto):
        self.name = name
        self.capacity = capacity
        self.configuration = configuration
        self.priority = priority
        self.fitsto = fitsto
    
    def __str__(self):
        return self.name