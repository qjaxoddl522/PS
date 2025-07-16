#include <iostream>
#include <vector>
#include <cmath>

class Point {
public:
	long long x;
	long long y;
	Point(long long inx, long long iny) {
		x = inx;
		y = iny;
	}
	Point operator-(Point p2) {
		return Point(x - p2.x, y - p2.y);
	}
	long long cross(Point a, Point b) {
		return a.x * b.y - b.x * a.y;
	}
};

int main()
{
	long long N;
	long long areaSum = 0;
	int underPoint = 0; 
	std::cin >> N;
	std::vector<Point> points;
	for (long long i = 0; i < N; i++) {
		long long x, y;
		std::cin >> x >> y;
		points.push_back(Point(x, y));
	}
	for (int i = 1; i < N - 1; i++) {
		Point vec1 = points[i] - points[0];
		Point vec2 = points[i + 1] - points[0];
		areaSum += vec1.cross(vec1, vec2);
	}
	areaSum = std::abs(areaSum);
	if (areaSum & 1)
		underPoint = 5;
	else
		underPoint = 0;
	areaSum = areaSum >> 1;

	std::cout << areaSum << '.' << underPoint;
}
