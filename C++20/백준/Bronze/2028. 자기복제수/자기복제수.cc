#include <iostream>

int main() {
    int T, N;
    std::cin >> T;
	for (int i = 0; i < T; i++)
	{
		std::cin >> N;
		int NN = N * N;
		bool isDupnum = true;
		while (N > 0) {
			if (N % 10 != NN % 10) {
				isDupnum = false;
				break;
			}
			N /= 10; NN /= 10;
		}

		if (isDupnum) {
			std::cout << "YES" << std::endl;
		}
		else {
			std::cout << "NO" << std::endl;
		}
	}
}