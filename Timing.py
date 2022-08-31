import math

class Timing:
    def hours(self, minutes):
        if(minutes < 60):
            return 0
        print(minutes)
        return self.hours_to_whole_number(minutes/60)
   
    def hours_to_whole_number(self, decimal_hours):
        return math.floor(decimal_hours)

    def print_time(self, minutes, pile_name):
        total_minutes = minutes
        hours = self.hours(total_minutes)
        minutes = minutes - (hours * 60)
        if(minutes < 0): minutes = total_minutes
        print(pile_name + ": " + str(hours) + "hr. " + str(minutes) + "min.")

    def minutes_total(self, hours, minutes):
        return hours * 60 + minutes