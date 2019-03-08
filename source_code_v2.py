#! /usr/bin/env python3

# helper code for formatting output with python:
#  https://pynative.com/python-postgresql-select-data-from-table/
# helper method for dividing columns without getting 0:
#  https://stackoverflow.com/questions/3996779/how-to-divide-two-columns/3996808
# helper codes for cast, to_char, rount functions where used from:
#  multiple online sources like: postgresql.org and w3schools.com

import psycopg2
try:
    connection = psycopg2.connect(database="news")
    cursor = connection.cursor()
# 1. What are the most popular three articles of all time?
    articles_query = """
                        SELECT articles.title, count(*) AS views
                        FROM articles JOIN log
                        ON log.path = concat('/article/',articles.slug)
                        GROUP BY title
                        ORDER BY views DESC LIMIT 3;
                        """
    cursor.execute(articles_query)
    articles_result = cursor.fetchall()
    print "       pop articles"
    for row in articles_result:
        print '* "', row[0], '"', "__", row[1], "views"
# 2. Who are the most popular article authors of all time?
# check view number 1 to understand the following:
    authors_query = """
                       SELECT authcles.name, count(*) AS views
                       FROM authcles JOIN log
                       ON log.path = concat('/article/',authcles.slug)
                       GROUP BY name
                       ORDER BY views DESC
                       """
    cursor.execute(authors_query)
    authors_result = cursor.fetchall()
    print " "
    print "       pop authors"
    for row in authors_result:
        print '* ', row[0], "__", row[1], "views"

# 3. On which days did more than 1% of requests lead to errors?
# check views number 2, 3, 4, 5 to understand the following:
    errors_query = """
                      SELECT to_char(date, 'Mon DD, YYYY'),
                      round((CAST(bad_c AS DECIMAL) / all_c)*100, 1)
                      FROM clicksbg_h;
                      """
    cursor.execute(errors_query)
    errors_result = cursor.fetchall()
    print " "
    print "      errors"
    for row in errors_result:
        print '* ', row[0], "__", row[1], " errors"
# to print error msg as suggested:
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data: ", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("connection is closed")