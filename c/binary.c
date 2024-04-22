#include<stdio.h>
main()
{
	int data[10];
	int i;
	int beg, mid, end;
	int key;
	clrscr();
	printf("\n Enter Data : ");
	for(i=0; i<10; i++)
	{
		scanf("%d",&data[i]);
	}
	printf("\n Enter a value to find : ");
	scanf("%d",&key);
	beg = 0;
	end = 9;
	mid = (beg + end) / 2;
	while(beg <= end)
	{
		if(data[mid] == key)
		{
			printf("\n %d is found at position #%d",key, mid);
			break;
		}
		else if(data[mid] < key)
		{
			beg = mid + 1;
		}
		else
		{
			end = mid - 1;
		}
		mid = (beg + end) / 2;
	}
	if(beg > end)
	{
		printf("\n %d is not found",key);
	}
	getch();
}