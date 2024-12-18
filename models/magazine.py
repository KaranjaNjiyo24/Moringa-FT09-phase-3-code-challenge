from database.connection import get_db_connection
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
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            if id is None:
                cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
                conn.commit()
                self._id = cursor.lastrowid
            else:
                cursor.execute('SELECT * FROM magazines WHERE id = ?', (id,))
                if not cursor.fetchone():
                    raise ValueError(f"No magazine found with id {id}")
                self._id = id
            
            self._name = name
            self._category = category
        except Exception as e:
            conn.rollback()
            raise ValueError(f"Error creating/retrieving magazine: {e}")
        finally:
            conn.close()

        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
