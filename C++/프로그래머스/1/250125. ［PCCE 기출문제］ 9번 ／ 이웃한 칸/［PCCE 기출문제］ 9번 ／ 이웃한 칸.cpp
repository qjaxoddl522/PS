#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<string>> board, int h, int w) {
    int answer = 0;
    int n = board.size();
    string myColor = board[h][w];
    if (h > 0 && board[h-1][w] == myColor) {
        answer++;
    }
    if (w > 0 && board[h][w-1] == myColor) {
        answer++;
    }
    if (h < n-1 && board[h+1][w] == myColor) {
        answer++;
    }
    if (w < n-1 && board[h][w+1] == myColor) {
        answer++;
    }
    return answer;
}