# Imports
import pandas as pd
import pymupdf as pdf

def main():
    # Opening PDF with PyMUPDF for read access
    doc = pdf.open("Example File.pdf")
    data = []
    # Take each page in PDF and extract tabular data (using column positions) 
    # then append the resulting pandas dataframe to a list of dataframes
    for page in doc:
        tables = page.find_tables(vertical_lines=[20, 154, 270, 450, 590, 772]).tables[0].to_pandas()
        data.append(tables)

    # Merge all pandas dataframes into one dataframe
    dataframe = data[0]
    for i in range(1,len(data)):
        dataframe = pd.concat([dataframe, data[i]])

    # Filter out "Notes" column in dataframe and replace "\n" (or new lines) in all dataframe entries with spaces
    # Then change all dataframe entry object types to string for post-processing
    dataframe = dataframe[dataframe["Notes"] != "Notes"]
    for label in dataframe.columns:
        dataframe[label] = dataframe[label].str.replace("\n", " ")
        dataframe[label] = dataframe[label].astype("string")

    # Create an pandas dataframe to export certain data from the cumulative dataframe
    export_df = pd.DataFrame(columns=["First Name", "Last Name", "Email", "Home Phone", "Work Phone", "Mobile Phone"])
    # Use the ".apply()" pandas function to filter and strip information from the cumulative dataframe to the export dataframe
    # using custom "lambda" functions built on python's innate string functions
    export_df["First Name"] = dataframe["Name (ID)"].apply(strip_first_name)
    export_df["Last Name"] = dataframe["Name (ID)"].apply(strip_last_name)
    export_df["Email"] = dataframe["Contact"].apply(strip_email)
    export_df["Home Phone"] = dataframe["Contact"].apply(strip_home_phone)
    export_df["Work Phone"] = dataframe["Contact"].apply(strip_work_phone)
    export_df["Mobile Phone"] = dataframe["Contact"].apply(strip_mobile)
    # Print a snapshot export dataframe for verification and debugging
    print(export_df)
    # Export the export dataframe into a csv for use by client
    export_df.to_csv("person_listing.csv", index=False)

# "Lambda" Function: Strip the first name out of a string
# Input: string x
# Output: x if its pandas NA object, otherwise string slice 
def strip_first_name(x):
    if pd.isna(x): return x
    else: return x[x.find(",")+2 : x.find("(")-1]

# "Lambda" Function: Strip the last name out of a string
# Input: string x
# Output: x if its pandas NA object, otherwise string slice
def strip_last_name(x):
    if pd.isna(x): return x
    else: return x[0 : x.find(",")]

# "Lambda" Function: Strip the email out of a string
# Input: string x
# Output: x if its pandas NA object, otherwise string slice
def strip_email(x):
    if pd.isna(x): return x
    if x.find("Email: ") == -1: return ""
    else: return x[x.find("Email: ")+7 :]

# "Lambda" Function: Strip the home phone number out of a string
# Input: string x
# Output: x if its pandas NA object, otherwise string slice
def strip_home_phone(x):
    if pd.isna(x): return x
    else: return x[x.find("Home#: ")+7 : x.find("Work#:")]

# "Lambda" Function: Strip the work phone number out of a string
# Input: string x
# Output: x if its pandas NA object, otherwise string slice
def strip_work_phone(x):
    if pd.isna(x): return x
    else: return x[x.find("Work#: ")+7 : x.find("Mobile#")]

# "Lambda" Function: Strip the mobile number out of a string
# Input: string x
# Output: x if its pandas NA object, otherwise string slice
def strip_mobile(x):
    if pd.isna(x): return x
    else: return x[x.find("Mobile# ")+8 : x.find("Email:")]

main()