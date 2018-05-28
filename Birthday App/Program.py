import datetime


def print_header():
    print("------------------------------------------------------------------")
    print("                           BIRTHDAY APP")
    print("------------------------------------------------------------------")
    print()


def get_birthday_from_user():
    user_year = int(input("What year were you born [YYYY]? "))
    user_month = int(input("What month were you born [MM]? "))
    user_day = int(input("What day were you born [DD]? "))

    birthday = datetime.date(user_year, user_month, user_day)
    return birthday


def date_diff(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days

def print_birthday(days):
    if days < 0:
        print("You had your birthday {} days ago. ".format(-days))
    elif days > 0:
        print("Your birthday is in {} days! ".format(days))
    else:
        print("Happy Birthday!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = date_diff(bday, today)
    print_birthday(number_of_days)


main()
