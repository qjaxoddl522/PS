import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	N = int(input())
	text = input()
	for i in range(N-1):
		latest = text[i+1]
		idx = [i+1]
		for j in range(i+2, N):
			if latest < text[j]:
				latest = text[j]
				idx = [j]
			elif latest == text[j]:
				idx.append(j)

		if latest > text[i]:
			result = []
			for j in idx:
				newText = text[:i] + text[i:j+1][::-1] + text[j+1:]
				result.append(newText)
			print(sorted(result)[-1])
			break
	else:
		print(text)

main()