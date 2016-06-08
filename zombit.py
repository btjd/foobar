import itertools

def answer(intervals):
    # Sort and remove duplicates
    intervals.sort()
    shifts = [s for s,_ in itertools.groupby(intervals)]
    
    # Define and initialize variables that will be used
    # to calculate total amount of time
    start = shifts[0][0]
    finish = shifts[0][1]
    gaps = 0
    
    # Iterate over shifts and compare them to the initail shift.
    for item in shifts:
        ShiftStart = item[0]
        ShiftEnd = item[1]
        if ShiftStart > finish:
            gaps += ShifStart - finish
            finish = ShiftEnd
        elif ShiftEnd > finish and ShiftStart >= start:
            finish = ShiftEnd
        else:
            pass
    return (finish - start) - gaps