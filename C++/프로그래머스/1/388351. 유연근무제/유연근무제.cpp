#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int answer = 0;
    int n = schedules.size();
    
    // 시간 더하기
    auto add = [](int a, int b) {
        int result = a + b;
        if (result % 100 >= 60) {
            result += 40;
        }
        return result;
    };
    
    // 인덱스 상의 토요일 구하기
    int saturday = (7 + (6 - startday)) % 7;
    
    for (int i = 0; i < n; i++) {
        int score = 0; // 이번 직원이 늦지 않고 출근한 횟수
        int deadline = add(schedules[i], 10);
        
        for (int day = 0; day < 7; day++) {
            if (deadline >= timelogs[i][day] && day != saturday && day != (saturday+1)%7) {
                score += 1;
            }
        }
        // 늦은 적 없으면 상품
        if (score == 5)
            answer += 1;
    }
    return answer;
}