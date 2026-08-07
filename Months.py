

import calendar

# Print a header
print("Months of the Year:")

# Loop through month numbers from 1 to 12
for month_index in range(1, 13):
    # Get the full name of the month
    month_name = calendar.month_name[month_index]
    print(month_name)