#include <iostream>
#include <algorithm>
using namespace std;

long long int find_large(long long int arr[],int x)
{
	long long int max = arr[0];
	for(int i=1;i<x;i++)
	{
		if(arr[i]>max)
			max = arr[i];
	}
	return max;
}

int main(void)
{
	int x,y;
	cin>>x>>y;
	int i,j;
	long long int arr[x];
	long long int largest =0;
	long long int maxim = 0;
	long long int prev_largest=0;
	for(i=0;i<x;i++)
	{
		cin>>arr[i];
		if(arr[i]>largest){
			largest = arr[i];
		}
	}
	if(largest==0)
	{largest = find_large(arr,x);}

	for(j=1;j<=y;j++)
	{	
		if(prev_largest==largest){
			if((y-j)%2==0)
			{
				for(i=0;i<x;i++)
				{
					arr[i] = largest-arr[i];
				}
				break;
			}
			else break;
		}
		else{
		arr[0]=largest-arr[0];
		maxim = arr[0];
		for(i=1;i<x;i++)
		{
			arr[i] = largest-arr[i];
			if(maxim<arr[i])
			{
				maxim = arr[i];
			}
		}
			prev_largest = largest;
			largest = maxim;

		}
	}

	for(i=0;i<x;i++)
	{
		cout<<arr[i]<<" ";
	}

	return 0;
}