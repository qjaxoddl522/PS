#include <iostream>

int main() {
    int N;
    std::cin >> N;

	for (int _ = 0; _ < N; _++)
	{
		long long S;
		std::cin >> S;

		bool isSosu = true;
		for (int i = 2; i <= 1000000; i++)
		{
			if (S % i == 0) {
				isSosu = false;
				break;
			}
		}

		if (isSosu) {
			std::cout << "YES" << std::endl;
		}
		else {
			std::cout << "NO" << std::endl;
		}
	}
}