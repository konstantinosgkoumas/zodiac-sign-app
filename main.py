import datetime
zodiac_signs = {
    "Aries": (datetime.date(1980, 3, 21), datetime.date(1980, 4, 19)),
    "Taurus": (datetime.date(1980, 4, 20), datetime.date(1980, 5, 20)),
    "Gemini": (datetime.date(1980, 5, 21), datetime.date(1980, 6, 20)),
    "Cancer": (datetime.date(1980, 6, 21), datetime.date(1980, 7, 22)),
    "Leo": (datetime.date(1980, 7, 23), datetime.date(1980, 8, 22)),
    "Virgo": (datetime.date(1980, 8, 23), datetime.date(1980, 9, 22)),
    "Libra": (datetime.date(1980, 9, 23), datetime.date(1980, 10, 22)),
    "Scorpio": (datetime.date(1980, 10, 23), datetime.date(1980, 11, 21)),
    "Sagittarius": (datetime.date(1980, 11, 22), datetime.date(1980, 12, 21)),
    "Capricorn": (datetime.date(1980, 12, 22), datetime.date(1981, 1, 19)),
    "Aquarius": (datetime.date(1981, 1, 20), datetime.date(1981, 2, 18)),
    "Pisces": (datetime.date(1981, 2, 19), datetime.date(1981, 3, 20)),
}
def get_zodiac_sign(date):
    for sign, date_range in zodiac_signs.items():
        if date_range[0] <= date <= date_range[1]:
            return sign
    return None
while True:
    try:
        user_date_str = input("Enter a date (YYYY-MM-DD): ")
        user_date = datetime.datetime.strptime(user_date_str, "%Y-%m-%d").date()
        break
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
zodiac_sign = get_zodiac_sign(user_date)

if zodiac_sign:
    print(f"Your zodiac sign is: {zodiac_sign}")
else:
    print("The provided date is not within the zodiac sign range.")