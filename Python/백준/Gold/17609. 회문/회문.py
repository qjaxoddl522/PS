import sys
input = lambda: sys.stdin.readline().rstrip()

def is_palindrome(s, left, right):
	while left < right:
		if s[left] != s[right]:
			return False
		left += 1
		right -= 1
	return True

def main():
	for _ in range(int(input())):
		string = input()
		n = len(string)
		
		if is_palindrome(string, 0, n-1):
			print(0)
			continue
		
		left = 0
		right = n - 1
		
		while left < right:
			if string[left] != string[right]:
				# 왼쪽 문자를 제거한 경우
				if is_palindrome(string, left + 1, right):
					print(1)
					break
				# 오른쪽 문자를 제거한 경우
				elif is_palindrome(string, left, right - 1):
					print(1)
					break
				else:
					print(2)
					break
			left += 1
			right -= 1

main()