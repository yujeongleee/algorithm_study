import sys

text = sys.stdin.readline()
text = text[:-1]

arr = []
for _ in text:
    arr.append(_)

arr.sort(reverse=True)

for _ in arr:
    print(_, end='')
