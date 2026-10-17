"""
RECORD CHECK  -  my version
===========================

Name  : Jocelyn Kakorozya
Lane  :  AI
Date  : 17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """Calculate calculations and determine the threshold warning status."""
    difference = value - limit
    percent = (value / limit) * 100
    
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
        
    return difference, percent, status


def print_report(label, difference, percent, status):
    """Format and print a single structured record line to the terminal."""
    print(f"[{label}] Status: {status:<10} | Diff: {difference:>6.1f} | {percent:>5.1f}%")

def load_records(path):
    """Read label,value,limit from a file and return a list of record dicts."""
    records_list = []
    try:
        with open(path, "r") as f:
            for line in f:
                if not line.strip():  # skip empty lines
                    continue
                label, value_str, limit_str = line.strip().split(",")
                records_list.append({
                    "label": label,
                    "value": float(value_str),
                    "limit": float(limit_str)
                })
    except FileNotFoundError:
        print(f"Error: The data file '{path}' was not found.")
        print("Falling back to empty dataset to prevent a crash.")
        
    return records_list

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

# Change this path to match your text file's filename
DATA_FILE = "records.txt" 
OUTPUT_FILE = "report_output.txt"

records = load_records(DATA_FILE)


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

if records:
    over_limit_count = 0
    
    # Open the output file to write results simultaneously (Excellent tier)
    with open(OUTPUT_FILE, "w") as out_f:
        for record in records:
            # 1. Unpack values from dict and compute logic
            lbl = record["label"]
            diff, pct, stat = check_record(record["value"], record["limit"])
            
            # 2. Print report to the terminal
            print_report(lbl, diff, pct, stat)
            
            # 3. Save line to external file 
            out_f.write(f"{lbl},{stat}\n")
            
            # 4. Increment counter if over limit
            if stat == "OVER LIMIT":
                over_limit_count += 1
                
        # Print the final total running counter summary block
        print("-" * 55)
        print(f"Summary: {over_limit_count} of {len(records)} records were OVER LIMIT.")
else:
    print("No records loaded. Execution stopped safely.")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
