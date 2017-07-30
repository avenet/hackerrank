from datetime import date
from calendar import weekday

cases = int(raw_input())

def get_friday_13ths(initial, final):
    result = 0
    current = initial
    
    if initial.day < 13:
        current = date(initial.year, initial.month, 13)
    elif initial.day > 13:
        next_month = initial.month + 1
        current_year = initial.year
        
        if next_month == 13:
            current_year += 1
            next_month = 1
        
        current = date(current_year, next_month, 13)
    
    while current <= final:
        if weekday(current.year, current.month, current.day) == 4:
            result += 1
        
        month = current.month + 1
        year = current.year
        
        if month == 13:
            month = 1
            year += 1
            
        current = date(year, month, 13)
    
    return result

for case in xrange(cases):
    date_input = raw_input().split()
    initial_date = date(int(date_input[2]), int(date_input[1]), int(date_input[0]))
    final_date = date(int(date_input[5]), int(date_input[4]), int(date_input[3]))
    
    print get_friday_13ths(initial_date, final_date)
    