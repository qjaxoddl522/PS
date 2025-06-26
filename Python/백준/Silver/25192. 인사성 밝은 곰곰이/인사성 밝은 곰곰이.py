import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	result = 0
	for _ in range(N):
		chat = input()
		if chat == "ENTER":
			greet = set()
		elif chat not in greet:
			greet.add(chat)
			result += 1
	print(result)

main()