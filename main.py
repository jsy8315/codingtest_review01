# 이코테 복습해보면서 하나라도 코드 더 쳐보자

# round(실수형 데이터, 반올림하고자 하는 위치 -1)
print(round(123.456, 2))

# //은 몫을 구할때, %는 나머지를 구할때 사용
a = 7
b = 3
print(a//b)
print(a%b)

#리스트의 인덱싱: 뒤에서 첫 번째 원소 출력은 [-1]
a = [1,2,3,4,5,6,7,8,9]
print(a[-1])

#리스트 슬라이싱: 끝 인덱스는 -1
print(a[0:4])

# 리스트 컴프리헨션: 이건 직접 해봐야됨
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 ==1]
print(array)

#연습 : i for i in range(20) if i % 2 == 1
#연습 : i for i in range(20) if i % 2 == 1
#연습 : i for i in range(20) if i % 2 == 1
#연습 : i for i in range(20) if i % 2 == 1

# n*m 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] *m for _ in range(n)]
print(array)

# 언더바는? 단순 반복 출력시 사용
for _ in range(5):
  print("hello world")

# 정렬은 sort: 오름차순이 기본
a = [1,4,3]
a.append(2)
print(a)

a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 작은 따옴표와 큰 따옴표를 표현하는 하기: \
data = 'hello world'
print(data)
data = "Don't you know \"PYTHON\"?"
print(data)

# 이중for문: 구구단
#for i in range(2,10):
#  for j in range(1,10):
#    print(i, "x", j, "=", i*j)
#    print()

# 함수는 기본문부터 해보기
def add(a,b):
  return a+b
  
print(add(3,7))

# 입출력
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))
print(data)

# 문자열 입력받기는 늘 봐도 새로워
import sys
data = sys.stdin.readline().rstrip()
print(data)

# 유용한 f-string
answer = 10
print(f"축구의 신 메시의 등번호는 {answer}입니다.")

# itertools
# 순열 permutations
from itertools import permutations
data = ["A", "B", "C"]
result = list(permutation(data,3))
print(result)

# 조합 combinations
from itertools import combinations
result = list(combinations(data,3))
print(result)

# 중복 순열 product
from itertools import product
result = list(product(data, repeat=2))
print(result)

# 중복 조합 combinations_with_replacement
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,2))
print(result)