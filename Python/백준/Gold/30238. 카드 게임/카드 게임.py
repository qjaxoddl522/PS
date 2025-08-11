import sys
input = lambda: sys.stdin.readline().rstrip()

"""
첫 번째 카드가 양수면 음수인 카드를 두 번째에서 전부 지움으로써 양수인 카드만 더할 수 있다.
음수면 두 번째 카드와의 합이 양수일 경우 두 카드 다 더한다.
합이 음수면 두 카드를 무시하고, 다음 카드부터는 음수를 전부 지울 수 있다.(앞의 카드를 삭제하면 되므로)
"""
def main():
	for _ in range(int(input())):
		n = int(input())
		A = list(map(int, input().split()))
		
		if A[0] > 0:
			print(sum([a if a > 0 else 0 for a in A]))
			continue

		if n >= 2:
			if A[0] + A[1] > 0:
				print(A[0] + A[1] + sum([a if a > 0 else 0 for a in A[2:]]))
			else:
				print(sum([a if a > 0 else 0 for a in A[2:]]))
			continue

		print(0)

main()