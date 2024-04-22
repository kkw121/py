#include<stdio.h>
#include<conio.h>

int main()
{
	int matrix[20][20],rows,cols,i,j,nonzero=0,tupleRows,tupleMatrix[20][3];
	int x = 1;
	clrscr();

	printf("\n Enter no. of rows and columns of Matrix : ");
	scanf("%d%d",&rows,&cols);

	printf("\n Enter matrix elements : ");
	for(i=0;i<rows;i++)
	{
		for(j=0;j<cols;j++)
		{
			scanf("%d",&matrix[i][j]);
		}
	}
	printf("\n Matrix is : \n");
	for(i=0;i<rows;i++)
	{
		for(j=0;j<cols;j++)
		{
			printf("%5d",matrix[i][j]);
			if(matrix[i][j] != 0)
				nonzero++;
		}
		printf("\n");
	}
	if(((rows*cols)/2)>nonzero)
	{
		printf("\n Matrix is a Sparse Matrix");
		tupleRows = nonzero+1;
		tupleMatrix[0][0] = rows;
		tupleMatrix[0][1] = cols;
		tupleMatrix[0][2] = nonzero;
		for(i=0;i<rows;i++)
		{
			for(j=0;j<cols;j++)
			{
				if(matrix[i][j] != 0)
				{
					tupleMatrix[x][0]=i+1;
					tupleMatrix[x][1]=j+1;
					tupleMatrix[x][2]=matrix[i][j];
					x++;
				}
			}
		}

		printf("\n 3-Tuple Representation : \n");
		for(i=0;i<tupleRows;i++)
		{
			for(j=0;j<3;j++)
			{
				printf("\t%d",tupleMatrix[i][j]);
			}
			printf("\n");
		}
	}
	else
	{
		printf("\n Matrix is not sparse matrix");
	}
	getch();
	return 0;
}
