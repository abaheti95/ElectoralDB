# ElectoralDB
The aim of this project was to create a user friendly web tool to manage electoral data. It has different views for different users of the website with different permission. Django is used for the backend.

## Data Extraction
Currently we have populated the data tables which are having the authentic data available online. There are Five such tables which are:
* Parliament_Constituency
* Constituency
* District_Constituency
* Address
* Party Data

All the above data is crawled from the internet.

## Parser files' information:
* parliamentParser.py : Takes the parliament text file extracted as input and inserts them to the mysql database
* assemblyParser.py: Takes the assembly-district-parliament mapping and inserts them to constituecya as well as district_constituency table.
* addressParser.py: Parses the address file in format town,pin,state,district and inserts them to the sql tables
* partyParser.py: Parses the party list and stores them in the table.

## Crawlers' information:
* District_pin_crawler.py : Uses http://www.mapsofindia.com/pincode/india/ as the crawler target.
* PoliticalParties.py : Use Parties.txt extracted from pdf of election commision of india
* Parliamentary Constituency Data: crawled from Wikipedia
* Assembly parliament and district mapping for westbengal: Crawled from Wikipedia.

Link for 3) and 4) is “http://en.wikipedia.org/wiki/" and "http://en.wikipedia.org/wiki/

## Data Population
The scripts used for data population is given above. These scripts parse the files needed for the same.

## Tables and Queries
All the tables used for data population is given in tables_and_queries.txt file. We have tried to include as many queries as possible to be used by our backend. Note that in many cases we are retrieving all the row information from table as they will be manipulated using the backend Python.