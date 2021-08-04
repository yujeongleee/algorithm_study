# 백준 코드 2438번 : 별 찍기 문제
# https://www.acmicpc.net/problem/2438
print(2438)
a = input()
for _ in range(int(a)):
    print('*'* (_+1))


#백준코드 2439번 : 별 찍기 문제
# 주의 : print 괄호 안에 +를 쓰면 띄어쓰기 없고, ,로 연결하면 띄어쓰기 한칸 생김
# 조금 더 꼼꼼히 보기
print(2439)
a = int(input())
for _ in range(a):
    print("_"*(a-_-1)+'*'* (_+1))

# 5598
#백준 코드 5598번 : 카이사르 암호
# 알파벳을 숫자로 바꾸는 ord 함수 사용
# 다시 알파벳으로 바꿀 때는 chr 함수 사용
code = input()
new_code = ''
for alphabet in code:
    if alphabet == 'A':
        new_code += 'X'
    elif alphabet == 'B':
        new_code += 'Y'
    elif alphabet == 'C':
        new_code += 'Z'
    else:
        new_code += chr(ord(alphabet) - 3)
print(new_code)

# 2562
# 최댓값
# argmax를 쓸 수 없다니..!
# 기본 파이썬 내장 함수 max와 배열.index(값)을 사용했다.
# index는 0부터 시작하는 것을 잊지 말자!!
numbers = []
for _ in range(9):
    numbers.append(int(input()))
print(max(numbers))
print(numbers.index(max(numbers)) + 1)

# 1037 약수
# 처음엔 이게 뭔 말인가 했다..
# 약수들이 다 주어질 것이니까 가장 작은 것과 가장 큰 약수를 곱하면 된다는 말
# 정답이 28이면, 2, 7 <- 이렇게 입력하는 것이 아니라 2, 4, 7, 14 이렇게 입력하는 것 (대신 순서는 랜덤)
_ = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

print(numbers[0] * numbers[-1])

