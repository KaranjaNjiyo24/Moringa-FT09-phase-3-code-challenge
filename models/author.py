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
    
    


    def __repr__(self):
        return f'<Author {self.name}>'
