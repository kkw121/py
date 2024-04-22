#include<stdio.h>
#define MAX 5

int stk[MAX], top=-1;

int main()
{
	int choice;
	clrscr();
	while(1)
	{
		printf("\n 1. PUSH");
		printf("\n 2. POP");
		printf("\n 3. VIEW");
		//printf("\n 4. Check Empty");
		//printf("\n 5. Check Full");
		printf("\n 6. Exit");
		printf("\n _____________________________");
		printf("\n Enter your choice : ");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1 : push(); break;
			case 2 : pop(); break;
			case 3 : view(); break;
			//case 4 : checkEmpty(); break;
			//case 5 : checkFull(); break;
			case 6 :
				printf("\n Press any key to exit...");
				getch();
			default :
				printf("\n Wrong Choice...!!!");
				exit();
		}
	}
}
push()
{
	int element;
	if(top == MAX-1)
	{
		printf("\n Stack is full. Element can not be added.");
	}
	else
	{
		printf("\n Enter a value : ");
		scanf("%d",&element);
		top++;
		stk[top] = element;
		printf("\n %d is added",element);
	}
}
pop()
{
	if(top == -1)
	{
		printf("\n Stack is empty.");
	}
	else
	{
		printf("%d is removed from stack",stk[top]);
		top--;
	}
}
view()
{
	int i;
	if(top == -1)
	{
		printf("\n Stack is empty.");
	}
	else
	{
		for(i = 0; i <= top; i++)
		{
			printf("\t%d",stk[i]);
		}
	}
}