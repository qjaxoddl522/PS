#include <iostream>



int main() {
    int n;
	std::cin >> n;

	std::cin.ignore();
	for (int i = 0; i < n; i++)
	{
		char name[26];
		std::cin.getline(name, 26);
		char* ptName = name;

		int g = 0, b = 0;
		while (*ptName != '\0') {
			if (*ptName == 'g' || *ptName == 'G') {
				++g;
			}
			else if (*ptName == 'b' || *ptName == 'B') {
				++b;
			}
			++ptName;
		}

		if (g > b) {
			std::cout << name << " is GOOD";
		}
		else if (g < b) {
			std::cout << name << " is A BADDY";
		}
		else {
			std::cout << name << " is NEUTRAL";
		}
		std::cout << std::endl;
	}
}