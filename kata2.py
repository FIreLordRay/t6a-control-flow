# Warehouse Audit Calendar
# For days 1–30, apply these rules:
from itertools import cycle

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT
for day in range (1,31):
    if day % 3 == 0 and day % 5 == 0:
        print (f"Day {day}: Full Audit")
    elif day % 3 == 0:
        print (f"Day {day}: Cycle count")
    elif