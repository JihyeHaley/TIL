def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n), 0, -1):
        answer.append(n[i-1])
    return answer

print(solution(12345))