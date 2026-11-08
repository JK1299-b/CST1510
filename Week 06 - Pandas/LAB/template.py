"""
RECORD CHECK  -  my version
===========================

Name  :Jocelyn Kakorozya
Lane  :  AI      
Date  :02/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("Week 06 - Pandas/LAB/my_file.csv")   # replace with pd.read_csv("your_file.csv")

# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

percent = (df["value"] / df["limit"]) * 100
df["percent"] = percent

# Add a "status" column
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x > 100 else "WARNING" if x > 90 else "OK")


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.
#Threshhold: Print the DataFrame as-is, with the percent column.
print(df)

# Typical: Filter to show only rows that are NOT "OK"
not_ok_df = df[df["status"] != "OK"]
print("\nRows requiring attention:")
print(not_ok_df)

#Excellent: Group by "status" and print a count per group
status_counts = df.groupby("status").size()
print("\nCount per status:")
print(status_counts)

# Save the full DataFrame to a new CSV file
df.to_csv("Week 06 - Pandas/LAB/processed_records.csv", index=False)

# 2. Generate and save a bar chart of the counts per status
# Note: You may need to import matplotlib.pyplot as plt at the top if it isn't already
import matplotlib.pyplot as plt

status_counts.plot(kind="bar", title="Counts per Status")
plt.tight_layout()
plt.savefig("Week 06 - Pandas/LAB/status_chart.png")



# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
