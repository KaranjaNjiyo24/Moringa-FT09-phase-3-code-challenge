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

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('UPDATE magazines SET name = ? WHERE id = ?', (value, self._id))
            conn.commit()
            self._name = value
        except Exception as e:
            conn.rollback()
            raise ValueError(f"Error updating magazine name: {e}")
        finally:
            conn.close()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('UPDATE magazines SET category = ? WHERE id = ?', (value, self._id))
            conn.commit()
            self._category = value
        except Exception as e:
            conn.rollback()
            raise ValueError(f"Error updating magazine category: {e}")
        finally:
            conn.close()


    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, content, author_id, magazine_id 
            FROM articles 
            WHERE magazine_id = ?
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
    def con


    def __repr__(self):
        return f'<Magazine {self.name}>'
