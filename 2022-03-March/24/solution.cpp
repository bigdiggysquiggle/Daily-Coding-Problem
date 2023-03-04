#include <deque>
#include <iostream>

void	maxSub(int arr[], int k, int len)	{
	int i = 0;
	std::deque<int> ind(0);
	for (i = 0; i < k; i++)	{
		while (!ind.empty() && arr[i] >= arr[ind.back()])
			ind.pop_back();
		ind.push_back(i);
	}
	std::cout << "[" << arr[ind.front()];
	for (; i < len; i++)	{
		while (!ind.empty() && (i-k+1) > ind.front())
			ind.pop_front();
		while (!ind.empty() && arr[i] >= arr[ind.front()])
			ind.pop_front();
		ind.push_back(i);
		std::cout << ", " << arr[ind.front()];
	}
	std::cout << "]" << std::endl;
}

int	main(void){
	int arr[] = {10, 5, 2, 7, 8, 7};
	maxSub(arr, 3, 6);
}
