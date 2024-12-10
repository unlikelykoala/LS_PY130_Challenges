'''
notes:
    - meetups happen monthly on same day of the week
        - eg, The first Monday of January 2021, The third Tuesday of December 2020, The teenth Wednesday of December 2020, The last Thursday of January 2021
    - meetup objects represent a meetup date
        - number 1-12 for month, and year, like 2021
        - determines the exact date of the meeting when prompted with relative date *(2nd wed if dece 2021)
    - descriptors: 'first', 'second', 'third', 'fourth', 'fifth', 'last', and 'teenth'
        - teenth: each month has 7 teenth days, so there is exactly 1 day of the week with teenth date for each month
    - day of week: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', and 'Sunday'

    - ignore case
    
rules:
    - use datetime module
    
    - class Meetup:
        - constructor: (self, year, month) (2013, 12)
            - initializes the year and month
        
        - day(day_of_week, descriptor): date(2013, 12, 10) == meetup.day('Tuesday', 'second')
            - returns date object with year, month, and day
            - return None if no match

DS:
    - 

Alg:
    - FIRST_THRU_FIFTH
        - iterate thru the days of the month 
            - create target = to dict value of FIRST T_ FIFTH
            - use a counter to keep incrementing the day from 1
            - create a counter object to keep track of how many times you've encountered the day of the week from 0
            - create date object for the first day of self's month (include the year!)

            - while True:
                - use try and except block to catch value error if you are out of the month
                    - return None
                - check if the current day matches day:
                    if so, increment counter
                    if counter matches the DESCRIPTOR, return current day
                - increment day counter
                
    - TEENTH
        - iterate thru the days of the month 
            - use a counter to keep incrementing the day from 1
            - create date object for the first day of self's month (include the year!)

            - while True:
                - check if the current day matches day AND is in TEENTH tuple:
                    - if so, return current day
                - increment day counter

    - LAST
        - iterate thru the days of the month FROM THE END
            - use a counter starting at 31
            - while True:
                - try except:
                    - create date object for the 31st of self's month (include the year!)
                    except:
                        - decrement date_coutner by 1
                    else:
                        - break

            - while True:
                - check if the current day matches day:
                    - if so, return current day
                - decrement day counter

'''
import datetime as dt


class Meetup:
    DAYS_OF_WEEK = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6,
    }
    TEENTHS = tuple(range(13, 20))
    FIRST_THRU_FIFTH = {
        'first': 1,
        'second': 2,
        'third': 3,
        'fourth': 4,
        'fifth': 5
    }
    
    def __init__(self, year, month):
        self._year = year
        self._month = month

    def day(self, day_of_week, descriptor):
        day_of_week = day_of_week.capitalize()
        descriptor = descriptor.casefold()

        if descriptor not in list(Meetup.FIRST_THRU_FIFTH.keys()) + ['teenth', 'last']:
            raise ValueError('invalid descriptor')
        
        if descriptor in self.__class__.FIRST_THRU_FIFTH:
            return self._first_thru_fifth_match(day_of_week, descriptor)
        
        if descriptor == 'teenth':
            return self._teenth_match(day_of_week)
        
        return self._last_match(day_of_week)

    def _first_thru_fifth_match(self, day_of_week, descriptor):
        target_nth = Meetup.FIRST_THRU_FIFTH[descriptor]
        date_counter = 1
        day_of_week_counter = 0

        while True:
            try:
                current_day =  dt.date(self._year, self._month, date_counter)

            except ValueError:
                return None
            
            else:
                if current_day.weekday() == Meetup.DAYS_OF_WEEK[day_of_week]:
                    day_of_week_counter += 1
                    if day_of_week_counter == target_nth:
                        return current_day

                date_counter += 1

    def _last_match(self, day_of_week):
        date_counter = 31

        while True:
            try:
                current_day = dt.date(self._year, self._month, date_counter)
            except ValueError:
                date_counter -= 1
            else:
                if current_day.weekday() == Meetup.DAYS_OF_WEEK[day_of_week]:
                    return current_day

                date_counter -= 1

    def _teenth_match(self, day_of_week):
        date_counter = 1

        while True:
            try:
                current_day =  dt.date(self._year, self._month, date_counter)

            except ValueError:
                return None
            
            else:
                if (
                    current_day.weekday() == Meetup.DAYS_OF_WEEK[day_of_week]
                    and current_day.day in Meetup.TEENTHS
                ):
                    return current_day

                date_counter += 1


if __name__ == '__main__':
    meetup = Meetup(2013, 12)
    print(meetup.day('wednesday', 'LAST'))
