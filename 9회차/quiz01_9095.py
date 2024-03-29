# 1, 2, 3 더하기
# 
# 문제
# - 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
#   1+1+1+1
#   1+1+2
#   1+2+1
#   2+1+1
#   2+2
#   1+3
#   3+1
# - 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# 입력
# -첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
# 출력
# - 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
def solution():
    n = 10                                               # 정수 n은 0<n<11이므로 10까지 구한 다음 해당 값만 리스트에 추출
    dp = [0]*(n+1)    
    for i in range(1,n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        if i<=3 :                                       # 1,2,3 일때는 본인의 숫자도 추가 될 수 있기 때문에 1개씩 추가          
            dp[i] += 1
    return dp

t = int(input())
result = solution()
for _ in range(t):
    num = int(input())
    print(result[num])