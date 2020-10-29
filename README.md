# Text Search Service using Regex

## This project is built using the following technologies:
- Flask for Web Hosting
- Regex for Pattern Search and Replace (re module)
- Pandas for parsing csv and excels
- textract module for reading pdfs (https://textract.readthedocs.io/en/stable/index.html)

#### Note: This service purges off any uploaded content/document post page refresh. It does not save or cache any uploaded content. 

#### Modules used:
 - regex -> re
 - currency -> currency-symbols
 
 
 ### Run this project by the following commands:
 
 1. Download this repo
 2. Get into the folder using cd TextSearchEngine
 3. run python text_finder.py
 4. Upload a file of your choice. Currently, the app supports only pdf documents. Will enchance it further to accept other docs too.
 5. Select the type of data that you want to search - Date/Currency/Whole Numbers/Fractions/Time
 6. Click Submit
 7. Scroll down the page to find the matched content.
