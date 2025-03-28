# pdf_scraper_script
### Description:
Python PDF scraping and processing script for converting tabular data in pdfs to extractable .csv files. (Early 2025)

### Background: 
This script was a volunteer project for local MA campaign managed by a family friend. The organization needed helping compiling contact and outreach information from a PDF with embedded tabular data. Results of this project were ~330 of the ~350 contacts within seconds instead of days of tedious volunteer work.

### Language and Libaries: 
- Language: Python
- Libararies: Pandas, Pymupdf

### High Level Code Overview: 
When the script is ran it will do the following in order: 
1. Conversion of the pdf page by page into tabular data and compiling it into a single "table".
2. Preliminary cleaning and labeling of the table data.
3. Hard cleaning of the table data column by column into specific human readable formatting.
4. Export specific columns of the table into a .csv with relevant contact info.

### Setup:
Cloning the repository and installing the environment (Windows):
- Install git and type in the command line `git clone https://github.com/j-crowley/pdf_scraper_script.git`
- Install Python and type in the command line `py -m pip install pandas` and `py -m pip install pymupdf`

### Running / Executing Script (Windows): 
- Navigate to the project folder using `cd` in command line, or in your file explorer and open command line
- Type the command `py .\pdf_analysis_test.py`

### Known Issues: 
Pymupdf has issues "reading" tables with varying numbers of rows without specification from the user. This causes some rows to be clipped out of the dataset on pages with 1-2 row tables. This could be fixed with hardcoding function parameters specifying the height of each row, or using other constraint parameters for that function call.
