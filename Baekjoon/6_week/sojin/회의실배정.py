import sys
input = sys.stdin.readline

n = int(input())

time = []
for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

last=0
cnt=0

for start, end in time:
    if start >= last:
        cnt+=1
        last=end

print(cnt)