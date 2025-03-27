# pdf_scraper_script
### Description:
Python PDF scraping and processing script for converting tabular data in pdfs to extractable .csv files.

### Background: 
A local campaign in MA reached out in early 2025 and was looking for help summarizing and extracting ~350 contacts from a town government site. This site had a large database of voters and town government participants that the campaign wanted to compile and eventually use to do outreach, but the site only method of exporting was through a generic tabular pdf containg all the data in the database. A family friend volunteering for the campaign reached out to me looking for solution that would cut down the compilation time of this data from days to a few hours of developer time. This script is the result of my volunteer work for this local organization. Results from the script were ~330 of the ~350 contacts being compiled and being passed to the organization.

### Language and Libaries: 
Written in Python using pymupdf (for pdf reading and scraping) and pandas (for data manipulation and .csv file exports).

### High Level Code Overview: 
When the script is ran it will do the following in order: 
1. Conversion of the pdf page by page into tabular data and compiling it into a single "table".
2. Preliminary cleaning and labeling of the table data.
3. Hard cleaning of the table data column by column into specific human readable formatting.
4. Export specific columns of the table into a .csv with relevant contact info.

### Setup:
Cloning the repository and installing the environment (Windows):
- Install git and in the command line type `git clone https://github.com/j-crowley/pdf_scraper_script.git`
- Install Python and using pip in the command line type `py -m pip install pandas` and `py -m pip install pymupdf`
This will set up the files and the environment to run and use the code in your favorite IDE.

### Running / Executing Script (Windows): 
- Navigate to the project folder using `cd` in command line, or in your file explorer and open command line
- Type the command `py .\pdf_analysis_test.py`

### Known Issues: 
Originally the pdf this script reads off of contains pages of tables varying between 1 and 5 rows. Due to the way pymupdf reads and converts pdf tables into pandas dataframe objects or "program stored tables", some pages (usually ones with only 1-2 rows in the table) don't get read and captured by the script. This is what lead to the data loss of ~20 contacts (~6% of total contacts) for the compilation passed off to the organization, but was deemed acceptable due to time crunch and the "low" error rate. This issue could be fixed by experimenting with how pymupdf reads rows in a table via hardcoding row parameters into the pymupdf function call, or use other constraint parameters in the pymupdf function call.
