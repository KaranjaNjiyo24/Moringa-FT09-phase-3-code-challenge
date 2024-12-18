class Magazine:
    def __init__(self, id, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters")
        
        
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
