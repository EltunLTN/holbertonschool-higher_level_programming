# SQL - Introduction

This directory contains introductory SQL tasks from the Holberton Higher Level Programming curriculum. Scripts cover database and table management, basic queries, and aggregate functions using MySQL.

## Learning Objectives

- List and create databases and tables
- Insert, update, and query rows
- Use filtering, ordering, and grouping
- Compute aggregates (COUNT, AVG, MAX)
- Work with JOINs and character set configuration

## Files

- `0-list_databases.sql`: Lists all databases on the MySQL server
- `1-create_database_if_missing.sql`: Creates `db_7` if it does not exist
- `2-remove_database.sql`: Drops database `db_7` if it exists
- `3-list_tables.sql`: Lists all tables in `db_7`
- `4-first_table.sql`: Creates `first_table` if it does not exist
- `5-full_table.sql`: Shows the structure of `first_table`
- `6-list_values.sql`: Lists all rows in `first_table`
- `7-insert_value.sql`: Inserts a single row into `first_table`
- `8-count_89.sql`: Counts records with `id = 89`
- `9-full_creation.sql`: Creates `second_table` and inserts multiple rows
- `10-top_score.sql`: Lists top 3 scores from `second_table`
- `11-best_score.sql`: Lists rows with score ≥ 10
- `12-no_cheating.sql`: Updates Bob's score to 10
- `13-change_class.sql`: Removes rows with score ≤ 5
- `14-average.sql`: Computes average score
- `15-groups.sql`: Counts rows grouped by score
- `16-no_link.sql`: Lists rows from `first_table` and `second_table` with matching values
- `100-move_to_utf8.sql`: Converts database `hbtn_0d_tvshows` to UTF8
- `101-avg_temperatures.sql`: Average temperature by city
- `102-top_city.sql`: Top city names by average temperature
- `103-max_state.sql`: Maximum temperature value

## Requirements

- MySQL 5.7+ or 8.x
- Access to a MySQL server with appropriate privileges

## Usage

Run a SQL script against MySQL:

```bash
cat 0-list_databases.sql | mysql -hlocalhost -P3306 -uroot -p
```

Or from the MySQL client:

```sql
SOURCE 0-list_databases.sql;
```
