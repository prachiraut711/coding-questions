# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
# Answers within 10-5 of the actual value will be accepted as correct.
# Input: hour = 12, minutes = 30
# Output: 165
# Input: hour = 3, minutes = 30
# Output: 75
# Example 3:
# Input: hour = 3, minutes = 15
# Output: 7.5

def angleClock(hour, minutes):
    minute_angle = 6 * minutes
    hour_angle = 30 * hour + 0.5 * minutes

    angle = abs(hour_angle - minute_angle)
    final_angle = min(angle, 360 - angle)
    
    return final_angle

print(angleClock(hour = 12, minutes = 30))
print(angleClock(hour = 3, minutes = 30))
print(angleClock(hour = 3, minutes = 15))