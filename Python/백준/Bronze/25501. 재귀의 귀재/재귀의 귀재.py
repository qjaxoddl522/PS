import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	for _ in range(int(input())):
		string = input()
		n = len(string)
		isPalin = True
		recursion = 1
		for i in range(n//2):
			if string[i] != string[n-i-1]:
				isPalin = False
				break
			recursion += 1
		print(1 if isPalin else 0, recursion)

main()