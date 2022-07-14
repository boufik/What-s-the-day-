'''
My only data is that in: 01 January of 1970 was Thursday
I have to predict the day of a given set of days/month/year = date
'''
daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysPerMonthInLeapYear = daysPerMonth.copy()
daysPerMonthInLeapYear[1] = 29
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# 1st Function
def isLeapYear(year):
    # Examples:
    # 2001 ---> no, 2004 ---> yes, 2060 ---> yes, 2300 ---> no, 2400 ---> yes
    if year % 4 != 0:
        # Like 2001 ---> False
        return False
    # The following cases conclude that: year can be divided exactly by 4 (year % 4 == 0)
    elif year % 4 == 0 and year % 100 != 0:
        # Like 2004 and 2060 ---> True
        return True
    # Now, we know for sure that our year can be divided by 4 and 100 ---> year % 4 == 0 and year % 100 == 0
    elif year % 100 == 0 and year % 400 != 0:
        # Like 2300 ---> False
        return False
    else:           # year % 400 == 0
        # Like 2400
        return True


# 2nd Function
def allDays(year):
    if isLeapYear(year) == True:
        return 366
    return 365

# 3rd Function
def partialDays(days, month, year):
    SUM = 0
    flag = isLeapYear(year)
    if flag == False:
        for i in range(month-1):
            SUM += daysPerMonth[i]
        return SUM + days
    else:
        for i in range(month-1):
            SUM += daysPerMonthInLeapYear[i]
        return SUM + days

# 4th Function
def countDays(days, month, year):
    SUM = 0
    for YEAR in range(1970, year):
        SUM += allDays(YEAR)
    SUM += partialDays(days, month, year)
    # This sum INCLUDES the 1st January of 1970 and I want to exclude it in order to find how many days
    # difference there are from 1 January
    return SUM - 1

# 5th Function - Find the final day
def giveDAY(number):
    return DAYS[(number + 3) % 7]
    # I added 3, beacuse my list of day begins with Monday (index = 0)
    # and I want to begin my process from Thursday (index = 3) cause of my data

# 6th Function - Checking the input
def checkInput(days, month, year):
    if year < 1970:
        print("We have data after: 1 January 1970")
        return False
    elif month < 0 or month > 12 or month != int(month):
        print("Each year has 12 months.")
        return False
    else:
        if days < 0:
            print("There are no negative days as we know")
            return False
        leap = isLeapYear(year)
        if leap == False:
            if days <= daysPerMonth[month-1]:
                return True
            print("This month has max days = " + str(daysPerMonth[month-1]) + ", but you gave me " + str(days))
            return False
        else:
            # We speak about a leap year
            if days <= daysPerMonthInLeapYear[month-1]:
                return True
            print("This month has max days = " + str(daysPerMonth[month-1]) + ", but you gave me " + str(days))
            return False


# 7th Function
def breakDATE(date):
    # There will be 2 spacebar-characters
    index1 = -1
    index2 = -1
    for i in range(len(date)):
        if date[i] == " ":
            index1 = i
            break
    for j in range(len(date)-1, -1, -1):
        if date[j] == " ":
            index2 = j
            break
    if index2 <= index1:
        print("There was a problem using function 'breakDATE'")
        return None
    # Now, we have to separate the infos coming from date
    days = date[0 : index1]
    MONTH = date[index1+1 : index2]
    MONTHFLAG = False
    month = -1000
    year = date[index2+1 :]
    for i in range(len(MONTHS)):
        if MONTH == MONTHS[i]:
            month = i + 1
            MONTHFLAG = True
            break
    if MONTHFLAG == False:
        print("There is no month named '" + str(MONTH) + "'")
    else:
        return int(days), month, int(year)



# MAIN FUNCTION
date = input("Give me a date: ")
days, month, year = breakDATE(date)
flag = checkInput(days, month, year)
if flag == True:
    print("---- Valid Date ----")
SUM = countDays(days, month, year)
print(str(SUM) + " days away from 1 January 1970")
print(str(date) + " ----> " + str(giveDAY(SUM)))