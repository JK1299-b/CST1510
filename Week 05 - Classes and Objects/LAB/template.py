"""
RECORD CHECK  -  my version
===========================

Name  : Jocelyn Kakorozya
Lane  :  AI  
Date  :25th october 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class Record:
    # Excellent requirement: Class-level running total for over-limit records
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initialize the record with a label, numeric value, and threshold limit."""
        self.label = label
        self.value = value
        self.limit = limit
        
        # Check if this new record is immediately over limit during initialization
        if self.value > self.limit:
            Record.over_limit_count += 1

    def status(self):
        """Return the current threshold compliance status of the record."""
        # Typical requirement: Calculate status using self.value and self.limit
        if self.value > self.limit:
            return "OVER LIMIT"
        elif self.value >= (self.limit * 0.9):
            return "WARNING"
        else:
            return "OK"



# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

def load_records(path):
    """
    Excellent requirement: Reads label, value, limit lines from a file
    and returns a list of Record objects.
    """
    loaded_list = []
    try:
        with open(path, 'r') as file:
            for line in file:
                # Strip whitespace and skip empty lines
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                
                # Split line by commas: label, value, limit
                parts = cleaned_line.split(',')
                if len(parts) == 3:
                    label = parts[0].strip()
                    value = float(parts[1].strip())
                    limit = float(parts[2].strip())
                    
                    # Create the object and add it to our list
                    new_record = Record(label, value, limit)
                    loaded_list.append(new_record)
        return loaded_list
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return []
    
# Replace records = [] with the function call pointing to your data file
# Example usage assuming you create a 'data.txt' file in the same folder:
records = load_records("Week 05 - Classes and Objects/LAB/data.txt")


# Print out results to test the implementation
for r in records:
    print(f"Record {r.label}: Status = {r.status()} (Val: {r.value}, Lim: {r.limit})")

print(f"\nTotal Over-Limit Records Counted: {Record.over_limit_count}")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

over_limit_count = 0  # Running count of OVER LIMIT records


for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

     # Threshold requirement: print label, value, limit inside a border
    print(f"| Label: {record.label:<24} |")
    print(f"| Value: {record.value:<24} |")
    print(f"| Limit: {record.limit:<24} |")
    
    # Typical requirement: add the result of .status()
    print(f"| Status: {record.status():<23} |")
    print("=" * 34)
    
    # Excellent requirement: keep a running count of OVER LIMIT returns
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

# Excellent requirement: print that once, after the loop
print(f"\nTotal OVER LIMIT records found: {over_limit_count}")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
