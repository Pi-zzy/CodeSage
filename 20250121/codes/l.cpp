#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
int dp[10000][10000];
int main() {
	int n;
	cin >> n;
	vector<int>a(n);
	vector<int>b(n + 1);
	b[0] = 0;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		b[i + 1] = b[i] + a[i];
	}
	int m = 1;
	for (int i = 2; i <= n; i++) {
		if (b[i] > b[m])m = i;
	}
	int h = 0;
	for (int i = 0; i < m; i++) {
		if (b[i] < b[h])h = i;
	}
	cout << b[m] - b[h];
}
