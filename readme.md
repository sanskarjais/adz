The application is build on Django Framework and for the database it uses the default version of sqlite3.
The db population is done by pandas dataframe and name of individual banks is fetched from sql file, it can also be done throgh csv but it would have 
increased the computation because standalone creating about 120,000 entries took much time, if the conditions are also added then it would be an
hassle.

In order to run the application on a local machine create a python environmnet and install the requirements. And on the browser visit localhost
Only queries of branches and banks are there, you can fetch the details of all the banks by the bank_id and branches by ifsc code visit sample.txt for sample queries
