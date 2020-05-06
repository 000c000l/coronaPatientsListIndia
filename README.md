# coronaPatientsListIndia
this repo contains the way to handle the list of present at "https://www.covid19india.org/demographics" via mysql way.


This program is written for Linux os and which has mysql-server installed.

Some assumptions:
   
      mysql user name is:  root.
      
      mysql password is:  password.
   

First run the initialSetup.sql on your mysql.

Python Libraries needed:
   
   selenium, mysql.connector and pandas.

To update the data run the following thing:
   
      python3 main.py --update

To run a mysql query:
  
      python3 main.py --query="mysql query"

To get the latitude and longitude of the locations of the query:
      
      
      python3 main.py --query="mysql query" --get_location
