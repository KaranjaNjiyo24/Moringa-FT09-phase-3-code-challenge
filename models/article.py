from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        
        conn = get_db_connection
        cursor = conn.cursor

        try:
            if id is None:
                cursor.execute('''
                    INSERT INTO articles (title, content, author_id, magazine_id)
                    VALUES (?,?,?,?)
                    ''', (title, content, author_id, magazine_id))
                conn.commit()
                self._id = cursor.lastrowid
            else:
                cursor.execute('SELECT * FROM articles WHERE id= ?', (id,))
                if not cursor.fetchone():
                    raise ValueError(f"No article found with id {id}")
                self._id =id

            self._title = title
            self._content = content
            self._author_id = author_id
            self._magazine_id = magazine_id
        except Exception as e:
            conn.rollback()
            raise ValueError(f"Error creating/retrieving article: {e}")
        finally:
            conn.close()
    

    def __repr__(self):
        return f'<Article {self.title}>'
