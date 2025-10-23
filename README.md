# BASIC SCRIPTING
## INSTRUCTIONS
```bash
# clone
```
### BASH EXERCISES
```bash
# Create the file
nano bash-exercises/bash-exercise-1.sh

# ... Write your script ...

# Grant execution permission
chmod +x bash-exercises/bash-exercise-1.sh
# Run the script
./bash-exercises/bash-exercise-1.sh
```
### PYTHON EXERCISES
```bash
# Go to folder
cd basic-scripting
mkdir python-exercises
cd python-exercises

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install pandas requests

# Save dependencies
pip freeze > requirements.txt

# Run the script
python main.py
```