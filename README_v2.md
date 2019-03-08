# Project repository contents
* **source_code.py** - The Python program that connects to the PostgreSQL database, executes the SQL queries and displays the results.
* **README.md** - This read me file.
* **new_logs_output.txt** - The text output of the `source_code.py`
* **views queries and tables.txt** contains create view commands and their tables
# How to run the program
#### Step one: prepare the software
* install [Vagrant](https://www.vagrantup.com/) last version
* install [Virtual Box](https://www.virtualbox.org/) box
* install python
* install Git bash
* open your terminal
*  bring the virtual machine online (with `vagrant up`), do so now. Then log into it with `vagrant ssh`.
* `cd` to your data directory that conatins the data in step two
* *make sure to have these too*: psycopg2 - PostgreSQL
#### Step two: prepare the data
* download the file *source_code.py*
* download the *newsdata.sql* file from udacity, this [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) should work with you if you are eligible to view udacity's courses.
#### Step three: load the data
To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.
#### step four: create views
* when you get a psql prompt like this `news=>` copy and paste each line of the folloing views:

1- `CREATE VIEW authcles as select articles.author, articles.title, articles.slug, articles.time, articles.id, authors.name from articles join authors on articles.author = authors.id;`

2- `CREATE VIEW bad_clicks as (SELECT date(time), COUNT(*) AS bad_c from log where status = '404 NOT FOUND' group by date(time) order by date(time));`

3- `CREATE VIEW all_clicks as (SELECT date(time), COUNT(*) AS all_c from log group by date(time) order by date(time));`

4- `CREATE VIEW clicksbg as (select * from all_clicks join bad_clicks using (date));`

5- `CREATE VIEW clicksbg_h as (select * from clicksbg where 1/(all_c/100) < (bad_c*100)/all_c);`

* I have attached a full guide for create views commands and their output tables, the file named `views queries and tables.txt`. feel free to check it if you need to.
#### step five: run the python file
* press `ctrl + D` and run this command `$python  python source_code.py`
* the terminal should now view the output of this code, like the output attached in the file `output.txt`
