#include<stdio.h>

struct node
{
	int data;
	struct node *next;
};
struct node *top = NULL;

int main()
{
	int choice;
	clrscr();
	while(1)
	{
		printf("\n1) Push \n2) Pop \n3) Display \n4) Count \n5) Distroy \n6) Exit");
		printf("\nEnter Your Choice : ");
		scanf("%d",&choice);

		switch(choice)
		{
			case 1: push(); break;
			case 2: pop(); break;
			case 3: display(); break;
			//case 4: count(); break;
			case 5: distroy(); break;
			case 6:
				printf("\nPress any key to exit...");
				getch();
				exit();
			default:
				printf("\nWrong Choice...");
		}
	}
	getch();
	return 0;
}

push()
{
	int ele;
	struct node *temp;

	printf("\nEnter a Value : ");
	scanf("%d",&ele);

	if(top == NULL)
	{
		top = (struct node *)malloc(sizeof(struct node));
		top->data = ele;
		top->next = NULL;
	}
	else
	{
		temp = (struct node *)malloc(sizeof(struct node));
		temp->data = ele;
		temp->next = top;
		top = temp;
	}
}
pop()
{
	struct node *temp;
	if(top == NULL)
	{
		printf("\nStack Underflow...");
	}
	else
	{
		temp = top;
		top = top->next;
		printf("%d is removed from stack",temp->data);
		free(temp);
	}
}
display()
{
	struct node *temp;
	if(top == NULL)
	{
		printf("\nStack Underflow...");
	}
	else
	{
		temp = top;
		printf("\nStack elements are  : ");
		while(temp != NULL)
		{
			printf("%d\t",temp->data);
			temp = temp->next;
		}
	}
}
destroy()
{
	struct node *temp;
	if(top == NULL)
	{
		printf("\nStack Underflow...");
	}
	else
	{
		temp=top;
		while(temp != NULL)
		{
			top = top->next;
			free(temp);
			temp = top;
		}
		printf("\n Stack destroyed");
	}
}