"""
RECORD CHECK  -  my version
===========================

Name  :Jocelyn korozya
Lane  :  AI 
Date  :10//10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def status_of(percent):
    """Return status based on percentage threshold."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate and return difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Format and print all report details enclosed inside a neat border."""
    print()
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Value      : {value:>15.2f}")
    print(f"  Limit      : {limit:>15.2f}")
    print(f"  Difference : {difference:>15.2f}")
    print(f"  Percentage : {percent:>14.2f}%")
    print(f"  Status     : {status:>15}")
    print("=" * 34)


# ====================================================================== MAIN CONTROL LOOP

# Counter tracking records that come back as OVER LIMIT
over_limit_count = 0

while True:
# ==================================================================== INPUT
# 2. Ask for your three values.
    label = input("\nEnter name/label (type 'quit' to stop): ").strip()
    
    # Check if the user wants to exit before collecting numeric inputs
    if label.lower() == "quit": 
        break
        
    value = float(input("Enter current value: "))
    limit = float(input("Enter threshold limit: "))



# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
difference, percent = check(value, limit)
status = status_of(percent)
    
    # Increment count if over limit
if status == "OVER LIMIT":
        over_limit_count += 1



# =================================================================== OUTPUT
# 4. Print the report.
def print_report(label, value, limit, difference, percent, status):"""Format and print all report details enclosed inside a neat border."""


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Value       : {value:>18.2f}")
print(f"  Limit       : {limit:>18.2f}")
print(f"  Difference  : {difference:>18.2f}")
print(f"  Percentage  : {percent:>17.2f}%")
print(f"  Status      : {status:>18}")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
