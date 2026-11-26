#include <iostream>

int main() {
    int N, L, D;
    std::cin >> N >> L >> D;

    int played = 0, time = 0, bellringTime = 0;
    while (played < N) {
        time += L;
        // 현재 시간을 넘을 때까지 전화벨 울림
        while (bellringTime < time) {
            bellringTime += D;
        }

        if (time + 5 > bellringTime) {
            break;
        }
        time += 5;
        ++played;
    }
    std::cout << bellringTime;
}