int covertInfixToPostfix(char* expression) 
{ 
    int i, j;

    for (i = 0, j = -1; expression[i]; ++i) 
    { 
        if (checkIfOperand(expression[i])) 
            expression[++j] = expression[i]; 

        else if (expression[i] == '(') 
            push(expression[i]); 

        else if (expression[i] == ')') 
        { 
            while (!isEmpty() && peek() != '(') 
                expression[++j] = pop(); 
            if (!isEmpty() && peek() != '(') 
                return -1;
            else
                pop(); 
        }
        else
        { 
            while (!isEmpty() && precedence(expression[i]) <= precedence(peek())) 
                expression[++j] = pop(); 
            push(expression[i]); 
        } 

    } 

    while (!isEmpty()) 
        expression[++j] = pop(); 

    expression[++j] = '\0'; 
    printf( "%s", expression); 
} 

int main()
{
char expression[20];
    printf("Enter infix expression: ");
    scanf("%s", &expression);
    printf("\nPostfix expression: ");
    covertInfixToPostfix(expression); 
    return 0; 
}