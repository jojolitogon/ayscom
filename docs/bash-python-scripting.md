**BASIC SCRIPTING WITH BASH AND PYTHON**

**Section 1: Introduction to Scripting**

**Topics:**

-   What is scripting?

-   Why automate repetitive data tasks?

-   Difference: scripting vs. full-fledged programming

-   When to use Bash vs. Python

**Slide Summary:**

-   Use Bash for: OS tasks, cron jobs, simple pipelines

-   Use Python for: data processing, logic-heavy tasks, APIs

**Activity:**

Group discussion: \"Which daily tasks could you automate with a
script?\"

**Section 2: Bash Scripting Basics**

**Topics:**

-   Writing and executing scripts (chmod +x, #!/bin/bash)

-   Variables, conditionals (if), loops (for, while)

-   File operations: cp, mv, mkdir, rm, find

-   Working with CSVs using cut, awk, grep

-   Scheduling with cron

**Code Example:**

#!/bin/bash

URL=\"https://example.com/data.csv\"

DATE=\$(date +%F)

FILENAME=\"sales\_\$DATE.csv\"

wget \$URL -O \$FILENAME

mkdir -p data/

mv \$FILENAME data/

echo \"File saved as data/\$FILENAME\"

**Mini Lab:**

-   Download a file

-   Rename it with today's date

-   Move it to a folder

**Section 3: Python Scripting for Data**

**Topics:**

-   File I/O and working with directories (os, glob)

-   Reading and writing CSV/JSON with pandas

-   Handling nulls, type conversions

-   Basic use of requests for API calls

-   Logging, error handling

**Code Example:**

import pandas as pd

import os

from glob import glob

all_files = glob(\"data/\*.csv\")

all_dfs = \[pd.read_csv(f) for f in all_files\]

df = pd.concat(all_dfs)

df.dropna(inplace=True)

df.to_csv(\"output/merged_clean.csv\", index=False)

**Mini Lab:**

-   Read all CSVs in a folder

-   Clean and normalize the data

-   Save as a merged file

**Section 4: Combining Bash + Python**

**Topics:**

-   Calling Python from Bash

-   Passing arguments to Python

-   Return codes and logging

**Bash Example:**

#!/bin/bash

FOLDER=\"data\"

python3 process_data.py \$FOLDER

**Python Example:**

\# process_data.py

import sys

folder = sys.argv\[1\]

print(f\"Processing folder: {folder}\")

**Activity:**

Write a script to detect new files in a folder and process them.

**Section 5: Best Practices for Scripting**

**Topics:**

-   Code organization and readability

-   Defensive scripting: set -e, trap, try/except

-   Using argparse for flexibility

-   Logging progress and errors

-   Git basics: init, commit, .gitignore

**Exercise:**

-   Improve an existing script with logging and error handling

**Section 6: Final Hands-On Project**

**Project Goal:**

Create an automated ETL-like pipeline

**Instructions:**

-   Bash script:

    -   Monitors a folder or runs daily

    -   Triggers the Python script

-   Python script:

    -   Cleans new data files

    -   Loads to SQLite/PostgreSQL

**Bonus:**

-   Optional: visualize the data with Grafana or Power BI

-   Package with README and clear structure

**Suggested Tools**

-   Bash in Ubuntu/macOS or Git Bash for Windows

-   Python 3.10+

-   pandas, requests, logging, argparse

-   SQLite/PostgreSQL

-   Git

**Learning Outcomes**

By the end of the course, students will:

-   Understand when and how to use scripting for automation

-   Write Bash scripts to orchestrate file and process tasks

-   Write Python scripts for data cleaning and transformation

-   Combine both in a mini ETL pipeline

-   Follow best practices for reusable and maintainable scripts

**What is Scripting?**

Scripting is the process of writing small programs---called
*scripts*---that automate tasks on a computer. Unlike full-scale
software applications, scripts are usually short, focused, and run line
by line without needing to be compiled.

Key traits of scripts:

-   Interpreted, not compiled (they run directly)

-   Great for automating repetitive tasks

-   Written in languages like **Bash**, **Python**, or **PowerShell**

*Think of a script as a digital assistant that follows your step-by-step
instructions.*

**Why Automate?**

Automation is about reducing manual effort and human error by letting
computers do the work for you.

**Reasons to automate:**

-   **Consistency**: The same task is done the same way every time

-   **Efficiency**: Tasks run faster, even while you sleep

-   **Accuracy**: Fewer mistakes compared to manual work

-   **Scalability**: Handle large amounts of data or tasks

*Instead of spending 20 minutes cleaning a file every morning, write a
script once---and save hours each week.*

**Differences Between Programming and Scripting**

  ------------------------------------------------------------------------
  **Feature**     **Programming**         **Scripting**
  --------------- ----------------------- --------------------------------
  Purpose         Build complex apps or   Automate tasks, manage systems
                  systems                 

  Language        Java, C++, Go           Python, Bash, JavaScript (Node),
  Examples                                PowerShell

  Compile vs      Compiled into binary    Interpreted line-by-line at
  Interpret       code                    runtime

  Use Case        Web apps, mobile apps,  File manipulation, automation,
                  games                   batch jobs
  ------------------------------------------------------------------------

*Programming is like building a car. Scripting is like driving it
efficiently from A to B.*

**When to Use Bash vs. Python**

  ------------------------------------------------------------------------
  **Task Type**             **Use Bash**    **Use Python**
  ------------------------- --------------- ------------------------------
  System-level tasks        Yes             Can do, but overkill sometimes

  File and folder           Fast and easy   More flexibility
  manipulation                              

  Working with CSV/JSON     Limited         Built-in libraries like
  data                                      pandas, json

  Calling APIs or complex   Difficult       Designed for this
  logic                                     

  Scheduling (cron jobs)    Perfect fit     Works, often called from Bash
  ------------------------------------------------------------------------

*Use Bash for quick glue scripts. Use Python when you need data
processing, error handling, or external APIs.*

**Running Commands and Writing Your First Script**

Bash is the default command-line shell in many Unix-based systems. You
can run individual commands---or group them in a .sh file to create a
script.

**Steps to create and run a Bash script:**

1.  Create a new file: nano myscript.sh

2.  Add this at the top: #!/bin/bash (shebang line)

3.  Write commands below it

4.  Make it executable: chmod +x myscript.sh

5.  Run it: ./myscript.sh

**Example script:**

#!/bin/bash

echo \"Hello, world!\"

*This is your first step to automation!*

**Variables, Conditionals, and Loops**

Bash scripts use variables to store and reuse values. They support basic
control structures like if, for, and while.

**Variables:**

name=\"Alice\"

echo \"Hello, \$name!\"

**Conditionals:**

if \[ \$name == \"Alice\" \]; then

echo \"Welcome!\"

else

echo \"Access denied.\"

fi

**Loops:**

for file in \*.csv; do

echo \"Processing \$file\"

done

*Use logic and repetition to automate smarter.*

**Working with Files and Directories**

Bash makes it easy to handle files and folders. Some common commands:

-   mkdir data/ → create a directory

-   mv file.csv data/ → move a file

-   rm old.txt → delete a file

-   find . -name \"\*.log\" → find all .log files

**Example:** Copy all .csv files into a backup folder:

mkdir -p backup

cp \*.csv backup/

*Combine commands to clean up and organize files quickly.*

**Reading and Writing CSVs with awk and cut**

While Bash isn't built for complex data processing, you can do a lot
with simple tools like awk, cut, and grep.

**cut** --- extract columns from a file:

cut -d\',\' -f1,3 sales.csv

**awk** --- pattern scanning and processing:

awk -F\',\' \'{print \$1, \$3}\' sales.csv

**grep** --- search for lines matching a pattern:

grep \"Shoes\" sales.csv

*Perfect for quick filtering or transforming CSVs before loading them.*

**Scheduling Scripts with cron**

Use cron to schedule your scripts to run automatically.

1.  Open the crontab: crontab -e

2.  Add a line like this:

0 6 \* \* \* /home/user/scripts/daily_etl.sh

This runs the script every day at 6:00 AM.

**Syntax:**

scss

CopiarEditar

┬ ┬ ┬ ┬ ┬

│ │ │ │ │

│ │ │ │ └─ Day of week (0--6)

│ │ │ └──── Month (1--12)

│ │ └────── Day (1--31)

│ └──────── Hour (0--23)

└────────── Minute (0--59)

*Cron is your personal task scheduler!*

**Bash + ETL: Automating File Downloads or Daily Jobs**

Bash is great for automating the first part of an ETL
process---**Extract**.

**Example script:**

#!/bin/bash

URL=\\\"https://example.com/data.csv\\\"

DATE=\$(date +%F)

FILENAME=\\\"sales\_\$DATE.csv\\\"

wget \$URL -O \$FILENAME

mkdir -p data/

mv \$FILENAME data/

echo \\\"Data saved as data/\$FILENAME\\\"

Use it with cron to automate daily downloads and move files into folders
for processing.

*This is real-world automation: download → store → ready for
transformation.*

**Mini Lab -- Bash: Automate a CSV Download**

**Goal:**

Create a Bash script that:

1.  Downloads a CSV file from a URL

2.  Renames it using today's date (e.g., sales_2025-07-20.csv)

3.  Moves it into a folder called data/

**Requirements:**

-   Internet connection

-   Basic Bash shell (Ubuntu, macOS, or Git Bash for Windows)

-   The wget or curl command

**Steps:**

1.  Create a new file named download_csv.sh

2.  Add a Bash shebang and comments

3.  Use variables to set the URL and the new filename

4.  Use the date command to generate today's date

5.  Create the data/ folder if it doesn\'t exist

6.  Move the downloaded file into that folder

**Example Script: download_csv.sh**

#!/bin/bash

\# Step 1: Set the URL of the CSV file

URL=\"https://people.sc.fsu.edu/\~jburkardt/data/csv/addresses.csv\"

\# Step 2: Get today's date in YYYY-MM-DD format

TODAY=\$(date +%F)

\# Step 3: Define the new filename with the date

FILENAME=\"download\_\$TODAY.csv\"

\# Step 4: Download the CSV file and rename it

wget -O \"\$FILENAME\" \"\$URL\"

\# Step 5: Create the target folder if it doesn\'t exist

mkdir -p data

\# Step 6: Move the file to the folder

mv \"\$FILENAME\" data/

\# Step 7: Confirmation message

echo \"File downloaded and saved as data/\$FILENAME\"

**Try It Out**

chmod +x download_csv.sh

./download_csv.sh

You should see:

File downloaded and saved as data/download_2025-07-20.csv

**Bonus Challenge:**

-   Add logging to a file called log.txt

-   Add error handling in case the download fails

if \[ \$? -ne 0 \]; then

echo \"Download failed!\" \>\> log.txt

exit 1

fi

**Mini Lab -- Bash Script Using curl**

**Goal:**

Same as before, but now using curl instead of wget to download the file.

**Example Script: download_csv_curl.sh**

#!/bin/bash

\# Step 1: Set the URL of the CSV file

URL=\"https://people.sc.fsu.edu/\~jburkardt/data/csv/addresses.csv\"

\# Step 2: Get today's date in YYYY-MM-DD format

TODAY=\$(date +%F)

\# Step 3: Define the new filename

FILENAME=\"download\_\$TODAY.csv\"

\# Step 4: Use curl to download the file

curl -o \"\$FILENAME\" \"\$URL\"

\# Step 5: Check if curl was successful

if \[ \$? -ne 0 \]; then

echo \"Download failed!\"

exit 1

fi

\# Step 6: Create the target folder if it doesn\'t exist

mkdir -p data

\# Step 7: Move the file to the folder

mv \"\$FILENAME\" data/

\# Step 8: Confirmation message

echo \"File downloaded and saved as data/\$FILENAME\"

**How to Run It**

chmod +x download_csv_curl.sh

./download_csv_curl.sh

Expected output:

File downloaded and saved as data/download_2025-07-20.csv

**Quick Comparison**

  -------------------------------------------------------------------------
  **Feature**   **wget**                  **curl**
  ------------- ------------------------- ---------------------------------
  Output        Saves file automatically  Needs -o to save to file

  Installed?    Often pre-installed       Always pre-installed on macOS

  Advanced?     Simpler syntax            More flexible and scriptable
  -------------------------------------------------------------------------

**Python: Variables, Functions, Loops**

**Variables**\
In Python, you don\'t need to declare the type:

name = \"Alice\"

price = 19.99

count = 3

**Functions**\
Functions help you organize and reuse code:

def greet(name):

return f\"Hello, {name}!\"

print(greet(\"Bob\"))

**Loops**\
For iterating over items:

python

CopiarEditar

for i in range(5):

print(i)

names = \[\"Ana\", \"John\", \"Mia\"\]

for name in names:

print(name)

*Use variables to store values, functions to group logic, and loops to
repeat actions.*

**2. Working with Files (open, os, glob)**

**open()** --- Read/write local files:

with open(\"data.txt\", \"r\") as f:

content = f.read()

print(content)

**os** --- Work with files and folders:

import os

os.mkdir(\"data\") \# Create folder

os.rename(\"file.txt\", \"old.txt\") \# Rename

**glob** --- Search for files using wildcards:

from glob import glob

files = glob(\"data/\*.csv\")

for file in files:

print(f\"Found file: {file}\")

*These tools let your script explore and manipulate your file system.*

**3. Data Manipulation Using pandas**

**pandas** is a powerful library for handling data tables (DataFrames).

import pandas as p

df = pd.read_csv(\"sales.csv\")

\# Preview data

print(df.head())

\# Clean and transform

df\[\"price\"\] = pd.to_numeric(df\[\"price\"\], errors=\"coerce\")

df\[\"product\"\] = df\[\"product\"\].str.strip().str.lower()

\# Filter rows

df = df\[df\[\"price\"\] \> 0\]

\# Add new column

df\[\"total\"\] = df\[\"price\"\] \* df\[\"quantity\"\]

*With pandas, you can clean, filter, and analyze datasets with just a
few lines.*

**4. Handling CSV/JSON Files**

**Reading and writing CSVs:**

\# Read CSV

df = pd.read_csv(\"data.csv\")

\# Write CSV

df.to_csv(\"clean_data.csv\", index=False)

**Reading and writing JSON:**

import json

\# Read JSON

with open(\"data.json\") as f:

data = json.load(f)

\# Write JSON

with open(\"output.json\", \"w\") as f:

json.dump(data, f, indent=2)

*CSV for tables, JSON for structured data like APIs.*

**5. APIs with requests**

Use the requests library to call REST APIs and handle responses.

python

CopiarEditar

import requests

response = requests.get(\"https://api.github.com/users/octocat\")

if response.status_code == 200:

data = response.json()

print(data\[\"login\"\], data\[\"public_repos\"\])

else:

print(\"Failed to fetch data:\", response.status_code)

**Optional -- POST request:**

response = requests.post(\"https://api.example.com/data\",
json={\"key\": \"value\"})

*APIs let your script interact with web services in real time.*

**6. Logging and Error Handling**

**Logging** --- Use logging instead of print() for production-ready
scripts.

import logging

logging.basicConfig(level=logging.INFO)

logging.info(\"Script started\")

logging.warning(\"Missing value encountered\")

**Error Handling with try/except:**

try:

price = float(\"19.99\")

except ValueError:

logging.error(\"Failed to convert price\")

**Combine both:**

try:

df = pd.read_csv(\"input.csv\")

except FileNotFoundError:

logging.error(\"File not found\")

exit(1)

*Logs and exceptions help you understand and debug your scripts safely.*

**Mini Lab -- Python: Clean and Merge CSV Files**

**Goal**

Create a Python script that:

1.  Reads all .csv files from a folder

2.  Cleans the data using pandas

3.  Merges them into a single cleaned output file

**Prerequisites**

-   A folder called data/ with at least 2--3 sample CSV files (e.g.,
    sales_jan.csv, sales_feb.csv, etc.)

-   Each file should have the same structure: product, price, quantity

Example content:

product,price,quantity

Shoes,59.99,3

Hat,NaN,2

backpack,29.90,1

**Step-by-Step Script**

\# clean_merge_csvs.py

import pandas as pd

import os

from glob import glob

\# Step 1: Define the input folder

input_folder = \"data\"

output_file = \"output/merged_cleaned.csv\"

\# Step 2: Create output folder if it doesn't exist

os.makedirs(\"output\", exist_ok=True)

\# Step 3: Find all CSV files in the folder

csv_files = glob(os.path.join(input_folder, \"\*.csv\"))

\# Step 4: Read and clean each file

cleaned_dfs = \[\]

for file in csv_files:

print(f\"Processing {file}\")

df = pd.read_csv(file)

\# Clean data: remove nulls

df = df.dropna()

\# Normalize column values

df\[\"product\"\] = df\[\"product\"\].str.strip().str.lower()

\# Convert price to float

df\[\"price\"\] = pd.to_numeric(df\[\"price\"\], errors=\"coerce\")

\# Re-clean in case price conversion created new nulls

df = df.dropna()

cleaned_dfs.append(df)

\# Step 5: Merge all cleaned data

merged_df = pd.concat(cleaned_dfs, ignore_index=True)

\# Step 6: Save final output

merged_df.to_csv(output_file, index=False)

print(f\"Merged file saved as: {output_file}\")

**How to Run It**

1.  Save the script as clean_merge_csvs.py

2.  Make sure you have the pandas library installed:

pip install pandas

3.  Run the script:

python3 clean_merge_csvs.py

**What This Teaches**

-   glob() for reading multiple files

-   pandas cleaning tools: dropna, str.strip(), str.lower(), to_numeric

-   os.makedirs() to ensure output folders exist

-   Data merging with pd.concat()

**Optional Challenges**

-   Add logging with logging.info()

-   Add command-line arguments using argparse

-   Automatically add a column for the file source (e.g.,
    df\[\"source\"\] = file)

**Combining Bash and Python**

Using Bash to control Python scripts is a powerful way to build
lightweight automation pipelines. Bash handles system-level
orchestration (scheduling, file checking), while Python performs the
logic-heavy data processing.

**Calling Python Scripts from Bash**

To call a Python script from a Bash script:

#!/bin/bash

echo \"Starting Python script\...\"

python3 process_data.py

echo \"Done.\"

This executes the Python file just like a regular command. Make sure the
Python script is executable and has a valid shebang (#!/usr/bin/env
python3) if you want to call it directly.

**2. Passing Arguments from Bash to Python**

You can send values from your Bash script into Python using command-line
arguments.

**Bash Script:**

#!/bin/bash

FOLDER=\"data\"

OUTPUT=\"output/cleaned.csv\"

python3 process_data.py \"\$FOLDER\" \"\$OUTPUT\"

**Python Script (process_data.py):**

import sys

import pandas as pd

import os

\# Receive arguments

input_folder = sys.argv\[1\]

output_file = sys.argv\[2\]

print(f\"Reading files from {input_folder}\...\")

print(f\"Saving cleaned data to {output_file}\...\")

\# (You can insert data cleaning logic here)

*This makes your Python scripts reusable for different inputs and
scenarios.*

**3. Creating a Folder-Watching Mini-Pipeline**

Let's say you want to check every minute whether new CSV files have been
added to a folder. If so, process them.

**Bash Script: watch_and_run.sh**

#!/bin/bash

INPUT_DIR=\"incoming\"

PROCESSED_DIR=\"processed\"

mkdir -p \"\$PROCESSED_DIR\"

\# Watch for new files every 60 seconds

while true; do

for file in \"\$INPUT_DIR\"/\*.csv; do

if \[ -f \"\$file\" \]; then

echo \"Processing \$file\...\"

python3 clean_and_save.py \"\$file\"

mv \"\$file\" \"\$PROCESSED_DIR\"/

fi

done

sleep 60

done

**Python Script: clean_and_save.py**

import sys

import pandas as pd

import os

file_path = sys.argv\[1\]

print(f\"Cleaning file: {file_path}\")

df = pd.read_csv(file_path)

df = df.dropna()

df\[\"product\"\] = df\[\"product\"\].str.strip().str.lower()

filename = os.path.basename(file_path)

output_path = f\"output/cleaned\_{filename}\"

os.makedirs(\"output\", exist_ok=True)

df.to_csv(output_path, index=False)

print(f\"Saved cleaned file to {output_path}\")

*This simulates a lightweight real-time ETL process: check → clean →
store.*

**4. Example: Automate an ETL-like Process**

**Goal**: Extract a CSV, transform it with Python, and load it into a
database or clean folder---all triggered by a Bash script.

**🔹 Bash: daily_etl.sh**

bash

CopiarEditar

#!/bin/bash

\# Step 1: Download data

DATE=\$(date +%F)

curl -o \"sales\_\$DATE.csv\" \"https://example.com/sales.csv\"

\# Step 2: Run transformation

python3 etl_transform.py \"sales\_\$DATE.csv\"

\# Step 3: Move to archive

mv \"sales\_\$DATE.csv\" archive/

**Python: etl_transform.py**

import sys

import pandas as pd

import os

input_file = sys.argv\[1\]

df = pd.read_csv(input_file)

df = df.dropna()

df\[\"product\"\] = df\[\"product\"\].str.lower().str.strip()

os.makedirs(\"cleaned\", exist_ok=True)

df.to_csv(f\"cleaned/cleaned\_{os.path.basename(input_file)}\",
index=False)

Run this script daily with cron, and you have a basic ETL pipeline in
production!

**What\'s Inside:**

-   etl_runner.sh -- Bash script that triggers the ETL pipeline.

-   etl_process.py -- Python script that cleans a CSV and loads it into
    a SQLite database.

-   incoming/products.csv -- Sample data file to simulate incoming
    files.

-   archive/ -- Folder where processed files are moved.

-   db/ -- SQLite database is saved here after running the Python
    script.

**How to Run:**

1.  **Unzip the folder** and navigate inside.

2.  **Make the Bash script executable**:

chmod +x etl_runner.sh

3.  **Run the pipeline**:

./etl_runner.sh

**Best Practices for Scripting**

Writing scripts isn't just about making things work---it's about making
them clear, safe, and maintainable. These practices will help your
scripts scale with your team and your data.

**1. Write Readable Scripts (Comments & Structure)**

**Why it matters:** Your future self---or your colleagues---should be
able to read your code easily.

**Best practices:**

-   Use clear, descriptive variable names

-   Break code into functions or logical blocks

-   Add comments explaining *why*, not just *what*

-   Group related steps together

**Example (Bash):**

\# Download today\'s sales report and move to the data folder

URL=\"https://example.com/sales.csv\"

curl -o daily_sales.csv \"\$URL\"

mv daily_sales.csv data/

**Example (Python):**

\# Clean product names and remove invalid prices

df\[\"product\"\] = df\[\"product\"\].str.strip().str.lower()

df\[\"price\"\] = pd.to_numeric(df\[\"price\"\], errors=\"coerce\")

df.dropna(subset=\[\"price\"\], inplace=True)

*Readable code saves debugging time and builds team trust.*

**2. Use set -e and trap in Bash**

**Why it matters:** Bash scripts should fail safely and visibly when
something goes wrong.

**Best practices:**

-   set -e → exits the script if any command fails

-   trap → define a cleanup or alert when errors happen

**Example:**

#!/bin/bash

set -e

trap \'echo \"Something went wrong. Exiting\...\"\' ERR

echo \"Starting ETL job\...\"

python3 etl_process.py

echo \"ETL completed.\"

*Fail early. Fail clearly. Don't let broken scripts run silently.*

**3. Use argparse and logging in Python**

**Why it matters:** Make your scripts flexible and debuggable.

**argparse** -- For command-line arguments:

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(\"\--input\", required=True)

args = parser.parse_args()

print(f\"Processing file: {args.input}\")

**logging** -- For consistent output (instead of print()):

import logging

logging.basicConfig(level=logging.INFO)

logging.info(\"Script started\")

*This makes your script reusable in pipelines, scheduled jobs, or with
multiple parameters.*

**4. Use Version Control (Git Basics)**

**Why it matters:** Track changes, collaborate, and roll back when
needed.

**Core Git commands:**

git init \# Start version control

git add script.py \# Stage changes

git commit -m \"Add initial ETL script\"

git log \# See history

**Extra tips:**

-   Use .gitignore to skip folders like \_\_pycache\_\_, \*.db, or
    output/

-   Write meaningful commit messages

-   Use branches for different versions or experiments

*If it's not in Git, it's not tracked.*

**5. When to Scale to Tools Like Airflow or Prefect**

**Scripting is great for:**

-   Simple ETL pipelines

-   One-time automation

-   Learning and prototyping

**But consider orchestration tools when you need:**

-   Scheduled, reliable execution (daily/hourly jobs)

-   Dependency handling (run this *after* that)

-   Monitoring, retries, notifications

-   Complex DAGs (directed acyclic graphs)

**Popular options:**

-   [Apache Airflow](https://airflow.apache.org/)

-   [Prefect](https://www.prefect.io/)

-   [Dagster](https://dagster.io/)

*Scripts are the seeds of automation. Workflow tools are the gardens.*

**Final Hands-On Project: Automated Sales Pipeline**

A guided challenge that combines everything students have
learned---Bash, Python, automation, and optional data visualization.

**Project Goal**

Build a **mini ETL pipeline** that:

1.  Detects new CSV files in a folder

2.  Processes and cleans them using Python (pandas)

3.  Loads the data into a database (SQLite)

4.  *(Optional)* Visualizes the results in Power BI or Grafana

**Deliverables**

Each student/team should deliver:

Folder structure:

bash

CopiarEditar

automated_sales_pipeline/

├── incoming/

├── archive/

├── db/

├── etl_runner.sh \# Bash script

├── etl_process.py \# Python script

├── sample_data.csv \# Test data

└── README.md \# Instructions

etl_runner.sh\
etl_process.py\
README.md with clear usage instructions

**Step-by-Step Instructions**

**1. Bash Script: etl_runner.sh**

This script:

-   Looks for new .csv files in incoming/

-   Calls the Python script for each file

-   Moves processed files to archive/

**Example:**

#!/bin/bash

INPUT_DIR=\"incoming\"

ARCHIVE_DIR=\"archive\"

mkdir -p \"\$INPUT_DIR\" \"\$ARCHIVE_DIR\"

for file in \"\$INPUT_DIR\"/\*.csv; do

if \[ -f \"\$file\" \]; then

echo \"Processing \$file\...\"

python3 etl_process.py \"\$file\"

mv \"\$file\" \"\$ARCHIVE_DIR\"/

echo \"Archived \$file\"

fi

done

**2. Python Script: etl_process.py**

This script:

-   Reads the CSV file

-   Cleans data using pandas

-   Loads it into a SQLite database

**Example:**

import sys

import os

import pandas as pd

import sqlite3

\# Input from Bash

file_path = sys.argv\[1\]

\# Read and clean the data

df = pd.read_csv(file_path)

df.dropna(inplace=True)

df\[\"product\"\] = df\[\"product\"\].str.strip().str.lower()

\# Load into SQLite

os.makedirs(\"db\", exist_ok=True)

conn = sqlite3.connect(\"db/sales.db\")

df.to_sql(\"sales\", conn, if_exists=\"append\", index=False)

conn.close()

print(f\"Loaded {len(df)} rows into the database.\")

**3. Optional Visualization**

**Option A: Power BI**

-   Connect to the sales.db SQLite database

-   Create charts: total sales, top products, etc.

**Option B: Grafana**

-   Set up Grafana + SQLite plugin or push to PostgreSQL

-   Build a dashboard using SQL queries

**📄 README.md Template**

markdown

CopiarEditar

\# Automated Sales Pipeline

This mini-project automates the ingestion and cleaning of daily sales
CSV files.

\## How it works

\- Place your \`.csv\` files in the \`incoming/\` folder

\- Run the pipeline using:

\`\`\`bash

./etl_runner.sh

-   Cleaned data will be loaded into db/sales.db

-   Original files will be moved to archive/

**Requirements**

-   Python 3.8+

-   pandas

-   SQLite (preinstalled)

yaml

CopiarEditar

\-\--

\## \*\*Learning Outcomes\*\*

Students will demonstrate their ability to:

\- Combine Bash and Python in a real-world automation task

\- Clean and prepare data for storage

\- Automate file workflows using scripting tools

\- Structure code and projects professionally
