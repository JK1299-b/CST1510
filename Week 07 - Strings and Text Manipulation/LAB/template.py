"""
RECORD CHECK  -  my version
===========================

Name  : Jocelyn Kakorozya
Lane  :  AI 
Date  : 06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

def parse_line(raw_line: str) -> dict:
    """Cleans, normalizes casing, and parses a messy raw string into a structured dictionary."""
    # 1. Clean up overall spacing and standardise case
    cleaned_line = raw_line.strip().lower()
    
    # Example parsing logic: Assuming comma-separated values (e.g., " user123 ,  45.5 ")
    # Replace or adapt this split logic to match your specific messy data format
    parts = [part.strip() for part in cleaned_line.split(",") if part.strip()]
    
    parsed_data = {}
    if len(parts) >= 2:
        parsed_data["id"] = parts[0]
        try:
            parsed_data["value"] = float(parts[1])
        except ValueError:
            parsed_data["value"] = parts[1]
            
    return parsed_data


def status_of(data: dict) -> str:
    """Determines the operational status category based on the parsed data values."""
    # Example logic: checking a numerical limit to assign a status lane
    value = data.get("value", 0)
    
    if isinstance(value, (int, float)):
        if value > 100:
            return "OVER LIMIT"
        elif value > 80:
            return "WARNING"
        return "OK"

    return "FLAGGED"
    
    

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

import re
# 1. Create and save the "messy_records.txt" file with 5 varied AI survey records
with open("messy_records.txt", "w") as f:
    f.write("  Survey_2026 , rating=4 , age=23  \n")
    f.write("SURVEY_2026,rating=5,age=34\n")
    f.write("   survey_2026   ,   rating=2   ,   age=19   \n")
    f.write("Survey_2026, rating=1 ,age=45\n")
    f.write("  survey_2026,rating=3,  age=29\n")


# 2. Define the parser function to clean and structure the data
def parse_line(raw_line):
    """Parses a messy data science line into a clean structured dictionary."""
    # Clean up outer whitespace
    cleaned = raw_line.strip()
    
    # Extract the survey identifier (everything before the first comma)
    survey_id = cleaned.split(",")[0].strip().lower()
    
    # Use regular expressions to extract rating and age integers safely
    rating_match = re.search(r"rating=(\d+)", cleaned)
    age_match = re.search(r"age=(\d+)", cleaned)
    
    rating = int(rating_match.group(1)) if rating_match else 0
    age = int(age_match.group(1)) if age_match else 0
    
    # Mapping our fields dynamically to fit the status_of evaluation structure
    return {
        "hostname": f"{survey_id} (Age: {age})",  # Formats name output nicely
        "used": rating,                          # Mapped to 'used' for the status logic
        "total": 5                               # Out of a max rating scale of 5
    }


# 3. Define the status calculator function (scaled out of 100%)
def status_of(used, total, warning_at=90):
    """Return OVER LIMIT, WARNING or OK based on score percentage."""
    percent = (used / total) * 100
    if percent >= 100:
        return "EXCELLENT (MAX SCORE)"
    elif percent >= warning_at:
        return "GREAT"
    else:
        return "COMPLETED"


# 4. Main execution: Load the text file and print the outputs
with open("messy_records.txt") as f:
    for raw_line in f:
        if not raw_line.strip():
            continue
        record = parse_line(raw_line)
        print(record["hostname"], "-> Status:", status_of(record["used"], record["total"]))



# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

#for raw_record in raw_records:
import re

# Track execution statistics for the "Excellent" requirement
total_records = 0
flagged_count = 0

# Helper function to cleanly parse your AI/Data Science lane format
def parse_line(raw_line):
    cleaned = raw_line.strip()
    
    # Safely isolate the survey identifier
    survey_id = cleaned.split(",")[0].strip().lower()
    
    # Extract numerical fields using regular expressions
    rating_match = re.search(r"rating=(\d+)", cleaned)
    age_match = re.search(r"age=(\d+)", cleaned)
    
    rating = int(rating_match.group(1)) if rating_match else 0
    age = int(age_match.group(1)) if age_match else 0
    
    # Return structured dict matching your original logic fields
    return {
        "survey_id": survey_id,
        "used": rating,
        "total": 5,  # Assuming a standard survey rating system out of 5
        "age": age
    }

# Original threshold status evaluation function
def status_of(used, total, warning_at=90):
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

# PROCESS + OUTPUT: Read line by line from your saved text file
with open("messy_records.txt") as f:
    for raw_line in f:
        # Skip empty lines
        if not raw_line.strip():
            continue
            
        # 1. Parse and print the cleaned dictionary (Threshold)
        record = parse_line(raw_line)
        print(f"Cleaned Dict: {record}")
        
        # 2. Call status_of(...) and print alongside (Typical)
        status = status_of(record["used"], record["total"])
        print(f"Status      : {status}\n")
        
        # Update metrics for final summary
        total_records += 1
        if status in ["WARNING", "OVER LIMIT"]:
            flagged_count += 1

# 3. Print a one-line summary at the end (Excellent)
print("==================================================")
print(f"Summary: Processed {total_records} records, with {flagged_count} flagged.")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
