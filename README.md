# HTML-to-CSV-Python-Converter
Convert HTML Databases with python, yo can convert .csv to .sql archives too, just import in phpMyAdmin and get your tables and columns.

<h2>Instructions for running the script:</h2>

<h3>Run the HTML to CSV script:</h3>

Save and run convert_multiple_html_to_single_csv.py in a terminal:

python convert_multiple_html_to_single_csv.py

<h3>Run the CSV to SQL script:</h3>

Save and run convert_csv_to_sql.py in a terminal:

python convert_csv_to_sql.py

These scripts will process all the HTML files in the specified folder, combine the data into a single CSV file and then convert that CSV to a SQL file. Be sure to change the paths to the correct locations on your system.

Make sure the CSV file name_of_your_file.csv is in the specified location (C:\Downloads).

Save the convert_csv_to_sql_with_tables.py script in a folder of your choice.

Open a terminal and navigate to the folder where you saved the script.

Run the script:

python convert_csv_to_sql_with_tables.py

Import into phpMyAdmin:

Open phpMyAdmin.

Select the database where you want to import the table.

Go to the "Import" tab.

Select the SQL file name_of_your_file.sql and run it.
