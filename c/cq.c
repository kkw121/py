#include<stdio.h>
#include<conio.h>
#define max 5

void enqueue();
void dequeue();
void display();

int queue[max], front=-1, rear=-1;

int main()
{
	int choice;
	clrscr();
	while(1)
	{
		printf("\n1.Insert \n2.Delete \n 3.Display \n 4.Exit");
		printf("\n _______________");
		printf("\n Enter Choice : ");
		scanf("%d", &choice);
		switch(choice)
		{
			case 1: enqueue(); break;
			case 2: dequeue(); break;
			case 3: display(); break;
			case 4:
				printf("\n Press any key to exit");
				getch();
				exit();
			default: printf("\n Invalid choice");
		}
	}
	getch();
	return 0;
}

void enqueue()
{
	int element;
	if((rear+1)%max == front)
	{
		printf("\n Queue is full.");
	}
	else
	{
		printf("\n Enter a Number : ");
		scanf("%d", &element);
		if(front == -1 && rear == -1)
		{
			front = rear = 0;
			queue[rear]=element;
		}
		else
		{
			rear=(rear+1)%max;
			queue[rear]=element;
		}
	}
}

void dequeue()
{
	if(front == -1 && rear == -1)
	{
		printf("\n Queue is empty");
	}
	else if(front==rear)
	{
		printf("\n %d is deleted.", queue[front]);
		front=rear=-1;
	}
	else
	{
		printf("\n %d is deleted", queue[front]);
		front=(front+1)%max;
	}
}

void display()
{
	int i;
	if(front == -1 && rear == -1)
	{
		printf("\n Queue is empty");
	}
	else
	{
		i=front;
		while(i!=rear)
		{
			printf("\t%d",queue[i]);
			i=(i+1)%max;
		}
		printf("\t%d",queue[rear]);
	}
}