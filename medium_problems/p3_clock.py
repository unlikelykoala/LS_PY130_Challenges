'''
notes:
    - clock independent of date
    - add/subtract minutes from time of a clock object
        - this creates a new clock, not mutating current clock
    - equality: two clocks with same time are equal
    - no built-in date or time functionality: only arithmetic operations

rules:
    - 
    
    - class Name:
        - constructor:
            - self._time set by at method
            self._hour
            self._minute

        - __add__(minutes):
            - add minutes
            - returns new clock
            - when it gets to 24 hours, it reverts back to 0
            - normalize time if over 59

        - __sub__(minutes):
            - subtracts minutes
            - returns new clock object
            - when isubtract below 0, it moves to 23 hours
            - normalize time if over 59

        - __eq__(self, other):
            - compares time of two clocks

        - __str__
            - returns string of time
        
        classmethod
        - at(hour, minutes=0):
            - returns clock object with time of the int 8 -> '8:00'

DS:
    - 

Alg:
    - normalize substracted minutes to a single day
    - figure out how many hours and minutes are left over
    - subtract hours from self._hour
    - subtrack minutes from self._minutes
        - if this causes self._minute to go below 00, self._hour should go down by 1 and self._minute should go back up to 0

'''
class Clock:
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

    def __init__(self, hour, minute):
        self._hour = hour
        self._minute = minute

    def __add__(self, minutes):
        hours, minutes = Clock._convert_minutes(minutes)

        added_minutes = self._minute + minutes
        additional_hour, final_minute = divmod(added_minutes, Clock.MINUTES_PER_HOUR)

        added_hours = additional_hour + hours + self._hour
        final_hour = added_hours % Clock.HOURS_PER_DAY

        return Clock.at(final_hour, final_minute)

    def __sub__(self, minutes):
        hours, minutes = Clock._convert_minutes(minutes)

        subtracted_minutes = self._minute - minutes
        additional_hour, final_minute = divmod(subtracted_minutes, Clock.MINUTES_PER_HOUR)

        subtracted_hours = self._hour + (Clock.HOURS_PER_DAY - hours + additional_hour) # adding additional_hour bc it's negative
        final_hour = subtracted_hours % Clock.HOURS_PER_DAY

        return Clock.at(final_hour, final_minute)

    def __eq__(self, other):
        return (
            self._hour == other._hour
            and self._minute == other._minute
        )
    
    def __ne__(self, other):
        return (
            self._hour != other._hour
            or self._minute != other._minute
        )

    def __str__(self):
        return f'{self._hour:02d}:{self._minute:02d}'

    @staticmethod
    def _convert_minutes(minutes):
        #normalize to one day
        minutes %= Clock.MINUTES_PER_DAY

        # conver to hours and minutes
        hours, minutes = divmod(minutes, Clock.MINUTES_PER_HOUR)
        return hours, minutes
    
    @classmethod
    def at(cls, hour, minute=0):
        return Clock(hour, minute)


if __name__ == '__main__':
    print(Clock.at(0, 30) - 40)
