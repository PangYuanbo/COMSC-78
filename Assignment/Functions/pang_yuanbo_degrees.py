#Yuanbo Pang
#This program converts degrees, minutes, and seconds to decimal degrees.
def to_decimal(degrees, minutes, seconds):
    total_minutes = minutes + (seconds / 60)
    total_degrees = degrees + (total_minutes / 60)
    return total_degrees


degrees = int(input("Enter degrees: "))
minutes = int(input("Enter minutes: "))
seconds = float(input("Enter seconds: "))


decimal_degrees = to_decimal(degrees, abs(minutes), abs(seconds))
print(f"That is {decimal_degrees} decimal degrees.")
