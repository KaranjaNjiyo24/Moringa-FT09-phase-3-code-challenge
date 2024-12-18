class Author:
    def __init__(self, id, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        
        if len(name.strip()) == 0:
            raise ValueError("Name must be a string")
        
        
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
