# Log Analysis
Udacity FSND Project

# About 
An internal reporting tool built in python that operate on a large database

## The reporting tool answer the following question:
* Most three popular articles.
* Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

# Database Table
* articles -> articles themselves
* authors -> information about the authors of articles
* log -> one entry for each time a user visit the website

# Installation
1. You will need to have <a href="https://git-scm.com/downloads">Git</a>, <a href="https://www.python.org/downloads/">Python</a> and <a href="http://initd.org/psycopg/">Psycopg</a> which is a PostgreSQL database adapter for the Python programming language installed on your environment
2. Launch terminal to clone the project
```
https://github.com/fkrishna/log-analysis.git
```
```
cd log-analysis
```
3. Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">newsdata.sql</a> file and place it at the root of the log analysis directory

# How To Run
```
python main.py
```

