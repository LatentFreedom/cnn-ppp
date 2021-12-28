# CNN PPP Loan Scraper
Scrape the PPP loan table on **[www.cnn.com/projects/ppp-business-loans/loans](www.cnn.com/projects/ppp-business-loans/loans)**

## MYSQL
Run the commands within the `setup/setup_mysql.sh` shell script.

### Loans table template
```
mysql> describe loans;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | int unsigned | NO   | PRI | NULL    | auto_increment |
| name          | text         | NO   |     | NULL    |                |
| description   | text         | YES  |     | NULL    |                |
| type          | varchar(30)  | NO   |     | NULL    |                |
| sector        | varchar(40)  | NO   |     | NULL    |                |
| employees     | int unsigned | NO   |     | NULL    |                |
| date_approved | timestamp    | NO   |     | NULL    |                |
| loan_amount   | varchar(30)  | NO   |     | NULL    |                |
| lender        | varchar(30)  | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```

### Require `local_infile` true
```
mysql> SHOW GLOBAL VARIABLES LIKE 'local_infile';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| local_infile  | ON    |
+---------------+-------+
```