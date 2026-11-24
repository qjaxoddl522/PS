#include <iostream>

int main()
{
	int n, k;
	while (std::cin >> n >> k) {
		int chicken = n;
		while (n >= k) {
			chicken += n / k;
			n = n % k + n / k;
		}
		std::cout << chicken << std::endl;
	}

	return 0;
}