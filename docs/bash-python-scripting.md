# BASIC SCRIPTING WITH BASH AND PYTHON
## INTRODUCTION TO SCRIPTING
### WHAT IS SCRIPTING
Scripting is the process of writing small programs—called scripts—that automate tasks on a computer. Unlike full-scale software applications, scripts are usually short, focused, and run line by line without needing to be compiled.<br><br>
Key traits of scripts:<br>
- Interpreted, not compiled (they run directly)
- Great for automating repetitive tasks
- Written in languages like Bash, Python, or PowerShell
### WHY AUTOMATE
Automation is about reducing manual effort and human error by letting computers do the work for you.<br><br>
**Reasons to automate:**
- **Consistency:** The same task is done the same way every time
- **Efficiency:** Tasks run faster, even while you sleep
- **Accuracy:** Fewer mistakes compared to manual work
- **Scalability:** Handle large amounts of data or tasks
### DIFFERENCES BETWEEN PROGRAMMING AND SCRIPTING
| **Feature**              | **Programming**                     | **Scripting**                               |
|---------------------------|-------------------------------------|---------------------------------------------|
| **Purpose**               | Build complex apps or systems       | Automate tasks, manage systems              |
| **Language Examples**     | Java, C++, Go                       | Python, Bash, JavaScript (Node), PowerShell |
| **Compile vs Interpret**  | Compiled into binary code           | Interpreted line-by-line at runtime         |
| **Use Case**              | Web apps, mobile apps, games        | File manipulation, automation, batch jobs   |
### WHEN TO USE BASH VS PYTHON
| **Task Type**                  | **Use Bash**                   | **Use Python**                         |
|--------------------------------|--------------------------------|----------------------------------------|
| **System-level tasks**          | Yes                            | Can do, but overkill sometimes         |
| **File and folder manipulation**| Fast and easy                   | More flexibility                       |
| **Working with CSV/JSON data**  | Limited                         | Built-in libraries like pandas, json   |
| **Calling APIs or complex logic**| Difficult                       | Designed for this                      |
| **Scheduling (cron jobs)**      | Perfect fit                     | Works, often called from Bash          |
## BASH SCRIPTING BASICS
Bash is the default command-line shell in many Unix-based systems. You can run individual commands—or group them in a .sh file to create a script.<br><br>
### STEPS TO CREATE AND RUN A BASH SCRIPT
1.	Create a new file: nano myscript.sh
2.	Add this at the top: #!/bin/bash (shebang line)
3.	Write commands below it
4.	Make it executable: chmod +x myscript.sh
5.	Run it: ./myscript.sh

**Example:**
```bash
#!/bin/bash
echo "Hello, world!"
```
### VARIABLES, CONDITIONALS AND LOOPS
Bash scripts use variables to store and reuse values. They support basic control structures like if, for, and while.<br>
**Variables:**
```bash
#!/bin/bash
name="Alice"
echo "Hello, $name!"
```
**Conditionals:**
```bash
#!/bin/bash
if [ $name == "Alice" ]; then
  echo "Welcome!"
else
  echo "Access denied."
fi
```
**Loops:**
```bash
#!/bin/bash
for file in *.csv; do
  echo "Processing $file"
done
```
### WORKING WITH FILES AND DIRECTORIES
Bash makes it easy to handle files and folders. Some common commands:<br>
- mkdir data/ → create a directory
- mv file.csv data/ → move a file
- rm old.txt → delete a file
- find . -name "*.log" → find all .log files

**Example:** Copy all .csv files into a backup folder:
```bash
#!/bin/bash
mkdir -p backup
cp *.csv backup/
```
### READING AND WRITING CSVs WITH awk AND cut
While Bash isn’t built for complex data processing, you can do a lot with simple tools like awk, cut, and grep.<br>
**cut —** extract columns from a file:
```bash
#!/bin/bash
cut -d',' -f1,3 sales.csv
```
**awk —** pattern scanning and processing:
```bash
#!/bin/bash
awk -F',' '{print $1, $3}' sales.csv
```
**grep —** search for lines matching a pattern:
```bash
#!/bin/bash
grep "Shoes" sales.csv
```
### SCHEDULING SCRIPTS WITH CRON
Use cron to schedule your scripts to run automatically.<br>
1.	Open the crontab: crontab -e
2.	Add a line like this:<br>
0 6 * * * /home/user/scripts/daily_etl.sh<br>
This runs the script every day at 6:00 AM.
```scss
┬ ┬ ┬ ┬ ┬
│ │ │ │ │
│ │ │ │ └─ Day of week (0–6)
│ │ │ └──── Month (1–12)
│ │ └────── Day (1–31)
│ └──────── Hour (0–23)
└────────── Minute (0–59)
```
### BASH + ETL: AUTOMATING FILE DOWNLOADS OR DAILY JOBS
Bash is great for automating the first part of an ETL process**—Extract**.<br>
**Example script:**
```bash
#!/bin/bash
URL=\"https://example.com/data.csv\"
DATE=$(date +%F)
FILENAME=\"sales_$DATE.csv\"

wget $URL -O $FILENAME
mkdir -p data/
mv $FILENAME data/
echo \"Data saved as data/$FILENAME\"
```
Use it with cron to automate daily downloads and move files into folders for processing.
### MINI LAB - BASH: AUTOMATE A CSV DOWNLOAD
**Goal:**<br>
Create a Bash script that:
1.	Downloads a CSV file from a URL
2.	Renames it using today’s date (e.g., sales_2025-07-20.csv)
3.	Moves it into a folder called data/

**Requirements:**
- Internet connection
- Basic Bash shell (Ubuntu, macOS, or Git Bash for Windows)
- The wget or curl command

**Steps:**
1.	Create a new file named download_csv.sh
2.	Add a Bash shebang and comments
3.	Use variables to set the URL and the new filename
4.	Use the date command to generate today’s date
5.	Create the data/ folder if it doesn't exist
6.	Move the downloaded file into that folder

**Example Script: download_csv.sh**
```bash
#!/bin/bash
# Step 1: Set the URL of the CSV file
URL="https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"

# Step 2: Get today’s date in YYYY-MM-DD format
TODAY=$(date +%F)

# Step 3: Define the new filename with the date
FILENAME="download_$TODAY.csv"

# Step 4: Download the CSV file and rename it
wget -O "$FILENAME" "$URL"

# Step 5: Create the target folder if it doesn't exist
mkdir -p data

# Step 6: Move the file to the folder
mv "$FILENAME" data/

# Step 7: Confirmation message
echo "File downloaded and saved as data/$FILENAME"
```
**Try It Out**
```bash
chmod +x download_csv.sh
./download_csv.sh
```
You should see:<br>
File downloaded and saved as data/download_2025-07-20.csv
### MINI LAB - BASH SCRIPT USING CURL
**Goal:**<br>
Same as before, but now using curl instead of wget to download the file.<br><br>
**Example Script: download_csv_curl.sh**
```bash
#!/bin/bash
# Step 1: Set the URL of the CSV file
URL="https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"

# Step 2: Get today’s date in YYYY-MM-DD format
TODAY=$(date +%F)

# Step 3: Define the new filename
FILENAME="download_$TODAY.csv"

# Step 4: Use curl to download the file
curl -o "$FILENAME" "$URL"

# Step 5: Check if curl was successful
if [ $? -ne 0 ]; then
  echo "Download failed!"
  exit 1
fi

# Step 6: Create the target folder if it doesn't exist
mkdir -p data

# Step 7: Move the file to the folder
mv "$FILENAME" data/

# Step 8: Confirmation message
echo "File downloaded and saved as data/$FILENAME"
```
**How to run it**
```bash
chmod +x download_csv_curl.sh
./download_csv_curl.sh
```
Expected output:<br>
File downloaded and saved as data/download_2025-07-20.csv<br><br>
**Quick Comparison**
| **Feature**     | **wget**              | **curl**                           |
|-----------------|-----------------------|------------------------------------|
| **Output**       | Saves file automatically | Needs `-o` to save to file          |
| **Installed?**   | Often pre-installed   | Always pre-installed on macOS      |
| **Advanced?**    | Simpler syntax        | More flexible and scriptable       |
## PYTHON SCRIPTING FOR DATA
### VARIABLES, FUNCTIONS, LOOPS
**VARIABLES**<br>
In Python, you don't need to declare the type:
```python
name = "Alice"
price = 19.99
count = 3
```
**FUNCTIONS**<br>
Functions help you organize and reuse code:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))
```
**LOOPS**<br>
For iterating over items:
```python
for i in range(5):
    print(i)

names = ["Ana", "John", "Mia"]
for name in names:
    print(name)
```
### WORKING WITH FILES (open, os, glob)
**open() —** Read/write local files:
```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```
**os —** Work with files and folders:
```python
import os
# Create folder
os.mkdir("data")
# Rename             
os.rename("file.txt", "old.txt")
```
**glob —** Search for files using wildcards:
```python
from glob import glob
files = glob("data/*.csv")
for file in files:
    print(f"Found file: {file}")
```
### DATA MANIPULATION USING PANDAS
**pandas** is a powerful library for handling data tables (DataFrames). With pandas, you can clean, filter, and analyze datasets with just a few lines.
```python
import pandas as p
df = pd.read_csv("sales.csv")

# Preview data
print(df.head())

# Clean and transform
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["product"] = df["product"].str.strip().str.lower()

# Filter rows
df = df[df["price"] > 0]

# Add new column
df["total"] = df["price"] * df["quantity"]
```
### HANDLING CSV/JSON FILES
CSV for tables, JSON for structured data like APIs.<br>
**Reading and writing CSVs:**
```python
# Read CSV
df = pd.read_csv("data.csv")

# Write CSV
df.to_csv("clean_data.csv", index=False)
```
**Reading and writing JSON:**
```python
import json
# Read JSON
with open("data.json") as f:
    data = json.load(f)
# Write JSON
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
```
### APIs WITH REQUESTS
Use the requests library to call REST APIs and handle responses. APIs let your script interact with web services in real time.
```python
import requests

response = requests.get("https://api.github.com/users/octocat")

if response.status_code == 200:
    data = response.json()
    print(data["login"], data["public_repos"])
else:
    print("Failed to fetch data:", response.status_code)
```
### LOGGING AND ERROR HANDLING
**Logging —** Use logging instead of print() for production-ready scripts. Logs and exceptions help you understand and debug your scripts safely.
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Script started")
logging.warning("Missing value encountered")

# Error Handling with try/except:
try:
    price = float("19.99")
except ValueError:
    logging.error("Failed to convert price")

# Combine both:
try:
    df = pd.read_csv("input.csv")
except FileNotFoundError:
    logging.error("File not found")
    exit(1)
```
### MINI-LAB - PYTHON: CLEAN AND MERGE CSV FILES
**Goal**<br><br>
Create a Python script that:
1.	Reads all .csv files from a folder
2.	Cleans the data using pandas
3.	Merges them into a single cleaned output file

**Prerequisites**
- A folder called data/ with at least 2–3 sample CSV files (e.g., sales_jan.csv, sales_feb.csv, etc.)
- Each file should have the same structure: product, price, quantity

Example content:
```csv
  product,price,quantity
  Shoes,59.99,3
  Hat,NaN,2
  backpack,29.90,1
```
## COMBINING BASH AND PYTHON
Using Bash to control Python scripts is a powerful way to build lightweight automation pipelines. Bash handles system-level orchestration (scheduling, file checking), while Python performs the logic-heavy data processing.<br>


