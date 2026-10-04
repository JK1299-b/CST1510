"""
RECORD CHECK  -  my version
===========================

Name  :Jocelyn Bennet
Lane  :  AI
Date  :4th october 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Enter the label: ")
value = float(input("Enter the value: "))
limit = float(input("Enter the limit: "))     


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = limit - value   # replace with your calculation
percent = (value / limit * 100)        # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

status = "OK"

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print()
print("=" * 40)
print(f"RECORD CHECK - {label}")
print("=" * 40)
print(f"Value:       {value}")
print(f"Limit:       {limit}")
print(f"Difference:  {difference:.2f}")
print(f"Percentage:  {percent:.2f}%")
print(f"Status:      {status}")
print("=" * 40)

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
