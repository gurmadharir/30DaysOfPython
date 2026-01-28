# =============================================================
# Day 14: Higher Order Functions
# ==============================================================
from datetime import datetime, date
from time import strptime

#1. Get the current day, month, year, hour, minute and timestamp
now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(day, month, year, hour, minute)
print("Timestamp:", timestamp)
#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

#3. Today is 28 January 2026. Change this time string to time.
date_string = "28 January, 2026"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

#4. Calculate the time difference between now and new year.
new_year = date(year=2027, month=1, day=1)
today = date(year=2026, month=1, day=28)
days_left = new_year - today
print("Days left:", days_left.days)

#5. Calculate the time difference between 1 January 1970 and now.
start = datetime(1970, 1, 1)

difference = now - start
print(difference)

#6. Think, what can you use the datetime module for? Examples:

# 1️⃣ Time series analysis
timestamp = datetime.now()
value = 120.5   # e.g. stock price

# 2️⃣ Timestamping activities in an application
log_time = datetime.now()
print(f"User logged in at {log_time}")

# 3️⃣ Adding posts on a blog
post_time = datetime(2026, 1, 26)   # example date

diff = now - post_time
days = diff.days

print(
    "Today" if days <= 0
    else "1 day ago" if days == 1
    else f"{days} days ago"
)
