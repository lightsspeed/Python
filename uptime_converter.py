'''
Scenario: You get uptime from a monitoring tool in minutes.

Task:

Convert minutes (e.g., 135) to hours and minutes

Print: "Uptime: 2 hours and 15 minutes"

Concepts: int, division, modulus, string formatting

'''

def convert_uptime(minutes: int) -> str:
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"Uptime: {hours} hours and {remaining_minutes} minutes"

# Test with 135 minutes
uptime_minutes = 135
print(convert_uptime(uptime_minutes))  # Output: Uptime: 2 hours and 15 minutes