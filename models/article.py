class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        
        
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'
