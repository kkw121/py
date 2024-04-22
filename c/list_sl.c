#include<stdio.h>
#include<conio.h>

struct node
{
	int data;
	struct node *next;
};
struct node *head;

int main()
{
	int choice;
	clrscr();
	while(1)
	{
		printf("\n ********** MENU **********");
		printf("\n 1. Create");
		printf("\n 2. Insert at Beginning");
		printf("\n 3. Insert after Specified Position");
		printf("\n 4. Insert at End");
		printf("\n 5. Delete From Beginning");
		printf("\n 6. Delete at Specified Position");
		printf("\n 7. Delete From End");
		printf("\n 8. Search");
		printf("\n 9. Display");
		printf("\n 10. Exit");
		printf("\n***************************");

		printf("\n Enter your choice : ");
		scanf("%d",&choice);

		switch(choice)
		{
			case 1: create(); break;
			case 2: insertAtBegin(); break;
			case 3: insertAfter(); break;
			case 4: insertAtEnd(); break;
			case 5: deleteFromBegin(); break;
			case 6: deleteRandom(); break;
			case 7: deleteEnd();
			case 8: search(); break;
			case 9: display(); break;
			case 10:
				printf("\n Press any key to exit.");
				getch();
				exit(0);
			default: printf("\n Invalid Choice.");
		}
	}
}

create()
{
	int ele;
	if(head != NULL)
	{
		printf("\n List is already created");
	}
	else
	{
		printf("\n Enter a Value : ");
		scanf("%d",&ele);
		head = (struct node *)malloc(sizeof(struct node));
		head->data = ele;
		head->next = NULL;
		printf("\n List is created");
	}
}

insertAtBegin()
{
	int ele;
	struct node *newNode;
	if(head == NULL)
	{
		printf("\n List is not created.");
	}
	else
	{
		printf("\n Enter a Value : ");
		scanf("%d",&ele);

		newNode = (struct node *)malloc(sizeof(struct node));
		newNode->data = ele;
		newNode->next = head;
		head = newNode;
		printf("\n Data added at the beginning.");
	}
}

insertAfter()
{
	int ele, position,i=1;
	struct node *newNode,*currentNode;
	if(head == NULL)
	{
		printf("\n List is not created.");
	}
	else
	{
		printf("\n Enter a Value : ");
		scanf("%d",&ele);

		printf("\n Enter Position : ");
		scanf("%d",&position);

		newNode = (struct node *)malloc(sizeof(struct node));
		newNode->data = ele;

		currentNode = head;
		while(i<position)
		{
			currentNode = currentNode->next;
			if(currentNode == NULL)
			{
				printf("\n Invalid Position.");
				return;
			}
			i++;
		}
		newNode->next = currentNode->next;
		currentNode->next = newNode;
		printf("\n Data addedd successfully.");
	}
}
insertAtEnd()
{
	int ele, i=1;
	struct node *newNode,*currentNode;
	if(head == NULL)
	{
		printf("\n List is not created.");
	}
	else
	{
		printf("\n Enter a Value : ");
		scanf("%d",&ele);

		newNode = (struct node *)malloc(sizeof(struct node));
		newNode->data = ele;
		newNode->next = NULL;

		currentNode = head;
		while(currentNode->next != NULL)
		{
			currentNode = currentNode->next;
		}
		currentNode->next = newNode;
		printf("\n Data addedd successfully.");
	}
}

deleteFromBegin()
{
	struct node *temp;
	if(head == NULL)
	{
		printf("\n List does not exists.");
	}
	else
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}
deleteRandom()
{
	int position,i=1;
	struct node *prevNode,*currentNode;
	if(head == NULL)
	{
		printf("\n List does not exists.");
	}
	else
	{
		printf("\n Enter Position : ");
		scanf("%d",&position);
		if(position == 1)
		{
			deleteFromBegin();
		}
		else
		{
			currentNode = head;
			while(i<position)
			{
				prevNode = currentNode;
				currentNode = currentNode->next;
				if(currentNode == NULL)
				{
					printf("\n Invalid Position.");
					return;
				}
				i++;
			}
			prevNode->next = currentNode->next;
			free(currentNode);
		}
	}
}

deleteEnd()
{
	struct node *prevNode,*currentNode;
	if(head == NULL)
	{
		printf("\n List does not exists.");
	}
	else
	{
		currentNode = head;
		if(currentNode->next == NULL)
		{
			deleteFromBegin();
			return;
		}
		while(currentNode->next != NULL)
		{
			prevNode = currentNode;
			currentNode = currentNode->next;
		}
		prevNode->next = NULL;
		free(currentNode);
	}
}
search()
{
	// TO DO;
}
display()
{
	struct node *temp;
	if(head == NULL)
	{
		printf("\n List does not exists");
	}
	else
	{
		temp = head;
		while(temp != NULL)
		{
			printf("\t%d",temp->data);
			temp = temp->next;
		}
	}
}