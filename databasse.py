import psycopg2 as psql
class Database:
    @staticmethod
    async def connect(query,query_type):
        db=psql.connect(
            database="n_47",
            passwors="jasur",
            host="localhost",
            port=5432
        )
        cursor=db.cursor()
        data= ['insert','delete']
        cursor.execute(query,data)
        if query_type=='insert':
            return True
        elif query_type=='delete':
            db.commit()
            return True
        else:
            return cursor.fetchall()

