from database.connection import get_db_connection
class Author:
    def __init__(self, id, name):
        self.id = id
        self.name =name

        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        
        if len(name.strip()) == 0:
            raise ValueError("Name must be a string")
        
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            if id is None:
                cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
                conn.commit()
                self._id = cursor.lastrowid
            else:
                cursor.execute('SELECT * FROM authors WHERE id = ?', (id,))
                if not cursor.fetchone():
                    raise ValueError(f"No author found with id {id}")
                self._id = id

            self._name = name
        except Exception as e:
            conn.rollback()
            raise ValueError(f"Error creating/retrieving author: {e}")
        finally:
            conn.close()
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        from models.article import Article
        conn = get_db_connection
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, title, content, author_id, magazine_id
            FROM articles
            WHERE author_id = ?
        ''', (self._id,))

        articles = [
            Article(
                id=row['id'],
                title=row['title'],
                content=row['content'],
                author_id=row['author_id'],
                magazine_id=row['magazine_id']
            ) for row in cursor.fetchall()
        ]

        conn.close()
        return articles
    
    def magazines(self):
        from models.magazine import Magazine
        conn = get_db_connection
        cursor = conn.cursor()

        cursor.execute('''
            SELECT DISTINCT m.id, m.name, m.category
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        ''', (self._id,))

        magazines = [
            Magazine(
                id=row['id'],
                name=row['name'],
                category=row['category']
            ) for row in cursor.fetchall()
        ]

        conn.close()
        return magazines




    def __repr__(self):
        return f'<Author {self.name}>'
