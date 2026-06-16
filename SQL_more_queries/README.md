# SQL - More Queries

This directory contains advanced SQL tasks from the Holberton Higher Level Programming curriculum. Scripts cover user privileges, JOINs, subqueries, and TV show database queries.

## Learning Objectives

- Grant and manage MySQL user privileges
- Query data across multiple tables with JOINs
- Use subqueries for filtering and aggregation
- Work with genre and rating tables in a TV shows database

## Files

- `0-privileges.sql`: Lists privileges of the current MySQL user
- `1-create_user.sql`: Creates user `user_0d_1` with password
- `2-create_read_user.sql`: Creates read-only user `user_0d_2`
- `3-force_name.sql`: Lists users with `user_0d_` prefix
- `4-never_empty.sql`: Creates `id_not_null` table with NOT NULL constraint
- `5-unique_id.sql`: Creates `unique_id` table with UNIQUE constraint
- `6-states.sql`: Creates `states` table
- `7-cities.sql`: Creates `cities` table with foreign key to `states`
- `8-cities_of_california_subquery.sql`: Lists California cities using a subquery
- `9-cities_by_state_join.sql`: Lists cities with state names using JOIN
- `10-genre_id_by_show.sql`: Lists show title and genre for Comedy
- `11-genre_id_all_shows.sql`: Lists all shows with genre (or NULL)
- `12-no_genre.sql`: Lists shows without a genre
- `13-count_shows_by_genre.sql`: Counts shows per genre
- `14-my_genres.sql`: Lists genres linked to the show Dexter
- `15-comedy_only.sql`: Lists Comedy titles aired after 2004
- `16-shows_by_genre.sql`: Lists all shows linked to any genre
- `100-not_my_genres.sql`: Lists genres not used by Dexter
- `101-not_a_comedy.sql`: Lists shows that are not Comedy
- `102-rating_shows.sql`: Lists show title and rating
- `103-rating_genres.sql`: Lists genre and average rating

## Requirements

- MySQL 5.7+ or 8.x
- Access to a MySQL server with appropriate privileges
- TV shows database (`hbtn_0d_tvshows`) for genre/rating tasks

## Usage

Run a SQL script against MySQL:

```bash
cat 9-cities_by_state_join.sql | mysql -hlocalhost -P3306 -uroot -p
```

Or from the MySQL client:

```sql
SOURCE 9-cities_by_state_join.sql;
```
