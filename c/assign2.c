

Q. No.  01:  Basic Stack Operations

Implement a stack using an array. Write functions for the following stack operations:
Push: Add an element to the top of the stack.
Pop: Remove and return the element from the top of the stack.
Peek: Return the element at the top of the stack without removing it.
isEmpty: Check if the stack is empty.
isFull: Check if the stack is full (if implemented using a fixed-size array).
Display: Show all elements in stack


#include<stdio.h>
#include<stdlib.h>

#define MAX_SIZE 5

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

void init(Stack *stack) {
    stack->top = -1;
}

int is_empty(Stack *stack) {
    return stack->top == -1;
}
int is_full(Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

void push(Stack *stack, int value) {
    if(is_full(stack)) {
        printf("Stack Overflow. Cannot push element onto full stack.\n");
        return;
    }
    stack->data[++stack->top] = value;
    printf("Pushed %d onto the stack.\n", value);
}

int pop(Stack *stack) {
    if(is_empty(stack)) {
        printf("Stack underflow. Cannot pop elemenet from empty stack.\n");
        return -1;
    }
    int value = stack->data[stack->top--];
    printf("Popped %d from the stack.\n",value);
    return value;
}

int peek(Stack *stack) {
    if(is_empty(stack)) {
        printf("Stack is empty. Cannot peek.\n");
        return -1;
    }
    return stack->data[stack->top];
}

void display(Stack *stack) {
    if(is_empty(stack)) {
        printf("Stack is empty.\n");
        return;
    }
    printf("Elemenets in the stack:\n");
    for(int i = stack->top; i >= 0; i--) {
        printf("%d\n",stack->data[i]);
    }
}

int main() {
    Stack stack;
    init(&stack);

    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);
    push(&stack, 4);
    push(&stack, 5);
    push(&stack, 6);

    display(&stack);

    printf("Peek: %d\n",peek(&stack));

    pop(&stack);
    pop(&stack);
    pop(&stack);
    pop(&stack);
    pop(&stack);
    pop(&stack);

    return 0;
}


Output :






Q. No. 02: Parenthesis Matching


Write a function to check if a given expression has balanced parentheses using a
stack. The expression can include parentheses, square brackets, and curly braces.


#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Node structure for the stack
struct Node {
    char data;
    struct Node* next;
};

// Function to create a new node
struct Node* newNode(char data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}

// Function to push a character onto the stack
void push(struct Node** top, char data) {
    struct Node* node = newNode(data);
    node->next = *top;
    *top = node;
}

// Function to pop a character from the stack
char pop(struct Node** top) {
    if (*top == NULL) {
        printf("Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    struct Node* temp = *top;
    char popped = temp->data;
    *top = (*top)->next;
    free(temp);
    return popped;
}

// Function to check if a given expression has balanced parentheses using a stack
bool isBalanced(char* expression) {
    struct Node* stack = NULL;
    char* p = expression;

    while (*p != '\0') {
        if (*p == '(' || *p == '[' || *p == '{') {
            push(&stack, *p);
        } else if (*p == ')' || *p == ']' || *p == '}') {
            if (stack == NULL) {
                return false;
            }
            char topChar = pop(&stack);
            if ((*p == ')' && topChar != '(') ||
                (*p == ']' && topChar != '[') ||
                (*p == '}' && topChar != '{')) {
                return false;
            }
        }
        p++;
    }
    return stack == NULL;
}

int main() {
    char expression1[] = "(){}[]";
    char expression2[] = "([{}]";
    char expression3[] = "({[}])";
    char expression4[] = "((()))";
    char expression5[] = "{[}]";

    printf("%s\n", isBalanced(expression1) ? "True" : "False");  // Output: True
    printf("%s\n", isBalanced(expression2) ? "True" : "False");  // Output: True
    printf("%s\n", isBalanced(expression3) ? "True" : "False");  // Output: False
    printf("%s\n", isBalanced(expression4) ? "True" : "False");  // Output: True
    printf("%s\n", isBalanced(expression5) ? "True" : "False");  // Output: False

    return 0;
}

Output :


Q. No. 03: Stack-based Calculator

Write a program to evaluate expressions in postfix notation using a stack. (Read
postfix expression, Read values of all variables)


#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

// Node structure for the stack
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}

// Function to push a value onto the stack
void push(struct Node** top, int data) {
    struct Node* node = newNode(data);
    node->next = *top;
    *top = node;
}

// Function to pop a value from the stack
int pop(struct Node** top) {
    if (*top == NULL) {
        printf("Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    struct Node* temp = *top;
    int popped = temp->data;
    *top = (*top)->next;
    free(temp);
    return popped;
}

// Function to evaluate a postfix expression
int evaluatePostfix(char* expression) {
    struct Node* stack = NULL;

    for (int i = 0; expression[i] != '\0'; i++) {
        if (isdigit(expression[i])) {
            push(&stack, expression[i] - '0');
        } else if (expression[i] == ' ') {
            continue;
        } else {
            int operand2 = pop(&stack);
            int operand1 = pop(&stack);
            switch (expression[i]) {
                case '+':
                    push(&stack, operand1 + operand2);
                    break;
                case '-':
                    push(&stack, operand1 - operand2);
                    break;
                case '*':
                    push(&stack, operand1 * operand2);
                    break;
                case '/':
                    push(&stack, operand1 / operand2);
                    break;
                default:
                    printf("Invalid operator\n");
                    exit(EXIT_FAILURE);
            }
        }
    }

    if (stack == NULL || stack->next != NULL) {
        printf("Invalid expression\n");
        exit(EXIT_FAILURE);
    }

    return pop(&stack);
}

int main() {
    char expression[100];

    printf("Enter postfix expression: ");
    fgets(expression, sizeof(expression), stdin);

    int result = evaluatePostfix(expression);
    printf("Result: %d\n", result);

    return 0;
}

Output :

Enter postfix expression: A B + C D + *
Stack underflow




Q. No. 04: Infix to Postfix Conversion

Write a function to convert an infix expression to postfix notation using a stack.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SIZE 100

typedef struct {
    char data[MAX_SIZE];
    int top;
} Stack;

void initialize(Stack *s) {
    s->top = -1;
}

int is_empty(Stack *s) {
    return s->top == -1;
}

int is_full(Stack *s) {
    return s->top == MAX_SIZE - 1;
}

void push(Stack *s, char value) {
    if (is_full(s)) {
        printf("Stack overflow\n");
        exit(EXIT_FAILURE);
    }
    s->data[++s->top] = value;
}

char pop(Stack *s) {
    if (is_empty(s)) {
        printf("Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    return s->data[s->top--];
}

int precedence(char op) {
    switch (op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        default:
            return 0;
    }
}

void infix_to_postfix(char *infix_expression, char *postfix_expression) {
    Stack s;
    initialize(&s);
    int j = 0;
    for (int i = 0; infix_expression[i] != '\0'; ++i) {
        char token = infix_expression[i];
        if (isalnum(token)) {
            postfix_expression[j++] = token;
        } else if (token == '(') {
            push(&s, token);
        } else if (token == ')') {
            while (!is_empty(&s) && s.data[s.top] != '(') {
                postfix_expression[j++] = pop(&s);
            }
            if (!is_empty(&s) && s.data[s.top] == '(') {
                pop(&s); // Discard '('
            } else {
                printf("Invalid infix expression\n");
                exit(EXIT_FAILURE);
            }
        } else { // Operator
            while (!is_empty(&s) && precedence(s.data[s.top]) >= precedence(token)) {
                postfix_expression[j++] = pop(&s);
            }
            push(&s, token);
        }
    }
    while (!is_empty(&s)) {
        if (s.data[s.top] == '(') {
            printf("Invalid infix expression\n");
            exit(EXIT_FAILURE);
        }
        postfix_expression[j++] = pop(&s);
    }
    postfix_expression[j] = '\0';
}

int main() {
    char infix_expression[MAX_SIZE];
    printf("Enter infix expression: ");
    fgets(infix_expression, sizeof(infix_expression), stdin);
    infix_expression[strcspn(infix_expression, "\n")] = '\0'; // Removing trailing newline
    char postfix_expression[MAX_SIZE];
    infix_to_postfix(infix_expression, postfix_expression);
    printf("Postfix expression: %s\n", postfix_expression);
    return 0;
}

Output:


Q. No. 05: Reverse a String using a Stack
Write a function to reverse a string using a stack.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

typedef struct {
    char data[MAX_SIZE];
    int top;
} Stack;

void initialize(Stack *s) {
    s->top = -1;
}

int is_empty(Stack *s) {
    return s->top == -1;
}

int is_full(Stack *s) {
    return s->top == MAX_SIZE - 1;
}

void push(Stack *s, char value) {
    if (is_full(s)) {
        printf("Stack overflow\n");
        exit(EXIT_FAILURE);
    }
    s->data[++s->top] = value;
}

char pop(Stack *s) {
    if (is_empty(s)) {
        printf("Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    return s->data[s->top--];
}

void reverse_string(char *str) {
    Stack s;
    initialize(&s);
    int length = strlen(str);
    
    // Push each character onto the stack
    for (int i = 0; i < length; ++i) {
        push(&s, str[i]);
    }

    // Pop each character from the stack and store them back in the string
    for (int i = 0; i < length; ++i) {
        str[i] = pop(&s);
    }
}

int main() {
    char str[MAX_SIZE];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0'; // Removing trailing newline
    reverse_string(str);
    printf("Reversed string: %s\n", str);
    return 0;
}

Output :














































