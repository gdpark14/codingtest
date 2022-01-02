
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int arr[102][102];






int main()
{
	int count = 0;

	for (int i = 0; i < 102; i++) {
		for (int j = 0; j < 102; j++) {
			arr[i][j] = 0;
		}
	}

	int num;
	cin >> num;	
	for (int i = 0; i < num; i++) {
		int x, y;
		cin >> x >> y;

		for (int j = x; j < x + 10; j++) {
			for (int k = y; k < y + 10; k++) {
				if (arr[j][k] == 0) {
					arr[j][k] = 1;
				}
			}
		}
	}

	for (int i = 1; i < 101; i++) {
		for (int j = 1; j < 101; j++) {
				if (arr[i][j] == 1) {
					int temp = 0;
					if (arr[i - 1][j] == 0) {
						temp++;
					}
					if (arr[i + 1][j] == 0) {
						temp++;
					}
					if (arr[i][j - 1] == 0) {
						temp++;
					}
					if (arr[i][j + 1] == 0) {
						temp++;
					}

					if (temp == 2) {
						count += 2;
					}
					if (temp == 1) {
						count += 1;
					}
				}
			}
		}
	cout << count << endl;



}
