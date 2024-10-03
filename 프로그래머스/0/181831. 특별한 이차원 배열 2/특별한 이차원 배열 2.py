def solution(arr):
    n = len(arr)  # 이차원 배열의 크기 (행과 열의 수)

    # 이중 루프를 사용하여 대칭성 검사
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:  # 대칭성이 깨진 경우
                return 0  # 대칭이 아닐 때 0 반환

    return 1  # 모든 요소가 대칭인 경우 1 반환
