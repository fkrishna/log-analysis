import psycopg2

#######################
# DB SERVICES 
#######################
DBNAME = "news"
def db_connection():
    db = psycopg2.connect(database=DBNAME)
    return db.cursor()

def db_get_top_articles(limit):
    cursor = db_connection()
    query = """
        SELECT title, 
        COUNT(path) as nviews FROM articles
        JOIN log on log.path = CONCAT('/article/', articles.slug)
        GROUP BY title, path 
        ORDER BY nviews DESC LIMIT {}
    """.format(limit)
    cursor.execute(query)
    return cursor.fetchall()


#######################
# HELPER 
#######################
def separator(n = 45, sep = '-'):
    print(sep * n)

def format_num(num):
    return "{:,}".format(num)


#######################
# OUTPUT 
#######################
def output_top_articles():
    print("\n- Top 3 Most Popular Articles\n")
    for items in db_get_top_articles(3):
        print("Title: " + str(items[0]))
        print("Views: " + format_num(items[1]))
        separator()




def main():
    print("\n** LOGS ANALYSIS **")
    output_top_articles()

if __name__ == '__main__':
    main()
