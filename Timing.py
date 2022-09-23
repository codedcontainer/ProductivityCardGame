import math

class Timing:
    "Pretty print time"
    def hours(self, minutes):
        "converts minutes into hours"
        if minutes < 60 :
            return 0
        return self.hours_to_whole_number(minutes/60)

    def hours_to_whole_number(self, decimal_hours):
        "converts decimal hours to whole number"
        return math.floor(decimal_hours)

    def print_time(self, minutes, pile_name):
        "print time in hours and minutes"
        total_minutes = minutes
        hours = self.hours(total_minutes)
        minutes = minutes - (hours * 60)
        if minutes < 0 :
            minutes = total_minutes
        print(pile_name + ": " + str(hours) + "hr. " + str(minutes) + "min.")

    def minutes_total(self, hours, minutes):
        "return the total number of minutes"
        return hours * 60 + minutes
