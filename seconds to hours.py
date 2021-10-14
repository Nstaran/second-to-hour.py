print("enter the second")
sum=int(input())
hour=int(sum/3600)
minutes=int(sum/60)
second=int(sum-int(minutes)*60)

print(str(hour)+':'+str(minutes)+':'+str(second)+':')