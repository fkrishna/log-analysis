import psycopg2

#######################
# DB SERVICES 
#######################

DBNAME = "news"

def db_connection():
    db = psycopg2.connect(database=DBNAME)
    return db.cursor()

# most articles that have been accessed the most
def db_get_popular_articles(limit):
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


# most popular article authors of all time
def db_get_popular_authors():
    cursor = db_connection()
    query = """
        SELECT name, 
        COUNT(*) as nviews
        FROM authors, articles, log
        WHERE authors.id = articles.author
        AND log.path = CONCAT('/article/', articles.slug)
        GROUP BY name
        ORDER BY nviews DESC
    """
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
def output_popular_articles():
    print("\n- Top 3 Most Popular Articles\n")
    for items in db_get_popular_articles(3):
        print("Title: " + str(items[0]))
        print("Views: " + format_num(items[1]))
        separator()


def output_popular_auhtors():
    print("\n- Most Popular Article Authors\n")
    for items in db_get_popular_authors():
        print("Author Name: " + str(items[0]))
        print("Views: " + format_num(items[1]))
        separator()




def main():
    print("\n** LOGS ANALYSIS **")
    output_popular_articles()
    output_popular_auhtors()

if __name__ == '__main__':
    main()
