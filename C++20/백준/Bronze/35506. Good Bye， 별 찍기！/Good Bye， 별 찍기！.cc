#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int N;
	cin >> N;
	vector<vector<char>> board(N*2, vector<char>(N*4+2, ' '));
	int horLen = board[0].size(), verLen = board.size();

	// '/'드로우
	for (int i = 0; i < verLen; i++)
	{
		board[verLen - i - 1][i] = '*';
	}

	// '0'드로우
	// 0의 가로 시작 인덱스
	int st = N * 2 + 1;
	for (int i = 0; i < N; i++)
	{
		board[N - 1 - i][st + i] = '*'; // 좌상단
		board[N + i][st + i] = '*'; // 좌하단
		board[N + i][horLen - 1 - i] = '*'; //우하단
		board[N - 1 - i][horLen - 1 - i] = '*'; //우상단
	}

	for (int y = 0; y < verLen; y++)
	{
		for (int x = 0; x < horLen; x++)
		{
			cout << board[y][x];
		}
		cout << endl;
	}

	return 0;
}