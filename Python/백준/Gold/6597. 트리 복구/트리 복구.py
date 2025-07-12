import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
	def dfs(preL, preR, inL, inR):
		if preL > preR:
			return
		
		root = preorder[preL]
		idx = position[root]
		left = idx - inL
		# 왼쪽, 오른쪽 재귀
		dfs(preL+1, preL+left, inL, idx-1)
		dfs(preL+left+1, preR, idx+1, inR)
		post.append(root)

	while True:
		try:
			preorder, inorder = map(list, input().split())
			position = {v: i for i, v in enumerate(inorder)}
			n = len(preorder)
			post = []
			dfs(0, n-1, 0, n-1)
			print(*post, sep='')
		except:
			break

main()