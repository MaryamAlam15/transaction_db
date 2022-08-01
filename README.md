A small project to read data from Sqlite DB and do some transformation.
The project also demonstrates how db can be switched with a very little effort. 

### PreReq:
- Python 3.9

### Install required packages:
> pip install -r requirements.txt


### How to run:
To execute the tasks 1-4, run the following command:
>python etl.py

- This will generate the console outputs for task 1, 2 and 4.
- The output of task 3 is written in file ``combined_data.csv`` under *output/* folder.


### Notes:
- Regarding task 3, the original values in `revenue` column are not changed. 
Rather a new column `revenue_eur` is created to store revenue in eurs.
#### Task 5: 
If you wish to use any other DB, you only need to:
- Add the required package(s) in `requirements.txt`, and
- Add connection statement in `db_connection.py`.

**Example:**

To use Postgres, do the following steps:
1. Uncomment the package in `requirements.txt`.
2. Install the package by using the command mentioned above.
3. Uncomment the code in `db_connection.py`.
4. Ofcourse, comment out the code done for SQLite. :)
