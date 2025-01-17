#total seconds calculator
seconds=int(input())
minutes=int(input())
hours=int(input())
min_sec=(minutes*60)
hrs_sec=(hours*3600)
time_sec=(seconds+min_sec+hrs_sec)
print(time_sec,"seconds")