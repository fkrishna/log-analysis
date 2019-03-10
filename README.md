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
1. Download <a href="https://git-scm.com/downloads" target="_blank">Git</a>, <a href="https://www.virtualbox.org/wiki/Downloads" target="_blank">VirtualBox</a> and <a href="https://www.vagrantup.com/downloads.html" target="_blank">Vagrant</a>
2. Launch terminal to clone the project
```
https://github.com/fkrishna/log-analysis.git
```
```
cd log-analysis
```
3. Download the newsdata.sql file and place it at the root of the log analysis directory
4. Run these command to install the database and create the views
```
psql news -f newsdata.sql
psql news -f views.sql
```

# Run
```
python main.py
```