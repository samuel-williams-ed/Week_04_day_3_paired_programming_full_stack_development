from db.run_sql import run_sql

from models.author import Author

def save(author):
    sql = "INSERT INTO authors (name, age, fav_motto ) VALUES (%s, %s, %s) RETURNING *"
    values = [author.name, author.age, author.fav_motto]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select(author_id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [int(author_id)]
    full_results = run_sql(sql, values)

    result = full_results[0]
    if result is not None:
        author = Author(result['id'], result['name'], result['age'], result['fav_motto'])
        
    return author
