# Read an integer:
# a = int(input())
# Print a value:
# print(a)

hour1 = int(input())
minute1 = int(input())
seconds1 = int(input())

hour2 = int(input())
minute2 = int(input())
seconds2 = int(input())

result = (hour1*3600+minute1*60+seconds1)-(hour2*3600+minute2*60+seconds2)
print(result);

