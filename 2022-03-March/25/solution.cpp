#include <vector>
#include <iostream>

using namespace std;

int findMin(vector<int> costs, int j, int K)	{
	int min = (j == 0 ? costs[1] : costs[0]);
	for (int i = 0; i < K; i++)
		if (i != j && costs[i] < min)
			min = costs[i];
	return min;
}

int minCost(vector<vector<int>> const&costs, int N, int K)	{
	vector<vector<int>> aux(N, vector<int>(K, 0));
	if (N == 0 || K == 0)
		return 0;
	for (int i = 0; i < K; i++)
		aux[0][i] = costs[0][i];
	for (int i = 1; i < N; i++)
		for (int j = 0; j < K; j++)
			aux[i][j] = costs[i][j] + findMin(aux[i-1], j, K);
	int min = aux[N-1][0];
	for (int i = 1; i < K; i++)
		if (min > aux[N-1][i])
			min = aux[N-1][i];
	return min;
}

int main(void)	{
	cout << "costs:" << endl << "0: 14 2 11" << endl << "1: 11 14 5" << endl << "2: 14 3 10" << endl << endl << "aux:" << endl;
	cout << "minimum possible cost: " << minCost({{14,2,11}, {11,14,5}, {14,3,10}}, 3, 3) << endl;
}
