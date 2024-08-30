<img src="https://github.com/Qcarvalhooliveira/holbertonschool-interview/blob/main/find_the_loop/image/Find-the-Loop.png" width="1000" height="400">

# **Find the Loop** :computer:

## **Description:** :speech_balloon:

* "Find the Loop" is a programming problem that focuses on detecting a cycle within a singly linked list. In this problem, the goal is to identify if a loop exists in the linked list, and if so, pinpoint the exact node where the loop begins. This is commonly solved using Floyd’s Cycle-Finding Algorithm, also known as the tortoise and hare algorithm, which employs two pointers moving at different speeds to traverse the list. If a loop is detected (when the pointers meet), the algorithm then resets one pointer to the head of the list and advances both pointers one step at a time until they meet again, which marks the start of the loop. 

## **Task** :books:

#### **0. Find the loop**

Write a function that finds the loop in a linked list.

* Prototype: listint_t *find_listint_loop(listint_t *head);
* Returns: The address of the node where the loop starts, or NULL if there is no loop
* You are not allowed to use malloc, free or arrays
* You can only declare a maximum of two variables in your function

Note: In order to compile the main file, you are provided with this static library. This library won’t be used during the correction; Its only purpose is for testing.

```
alexa@ubuntu:~/find_the_loop$ cat 0-main.c 
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *head2;
    listint_t *node;

    head2 = NULL;
    add_nodeint(&head2, 0);
    add_nodeint(&head2, 1);
    add_nodeint(&head2, 2);
    add_nodeint(&head2, 3);
    add_nodeint(&head2, 4);
    add_nodeint(&head2, 98);
    add_nodeint(&head2, 402);
    add_nodeint(&head2, 1024);
    print_listint_safe(head2);
    node = find_listint_loop(head2);
    if (node != NULL)
    {
        printf("Loop starts at [%p] %d\n", (void *)node, node->n);
    }
    free_listint_safe(&head2);
    head = NULL;
    node = add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    add_nodeint(&head, 4);
    add_nodeint(&head, 5);
    add_nodeint(&head, 6);
    node->next = add_nodeint(&head, 7);
    add_nodeint(&head, 98);
    add_nodeint(&head, 402);
    add_nodeint(&head, 1024);
    print_listint_safe(head);
    node = find_listint_loop(head);
    if (node != NULL)
    {
        printf("Loop starts at [%p] %d\n", (void *)node, node->n);
    }
    free_listint_safe(&head);
    return (0);
}
alexa@ubuntu:~/find_the_loop$ gcc -Wall -pedantic -Werror -Wextra 0-main.c 0-find_loop.c -L. -lloop -o main
alexa@ubuntu:~/find_the_loop$ ./main
[0x13700f0] 1024
[0x13700d0] 402
[0x13700b0] 98
[0x1370090] 4
[0x1370070] 3
[0x1370050] 2
[0x1370030] 1
[0x1370010] 0
[0x1370560] 1024
[0x1370540] 402
[0x1370010] 98
[0x1370030] 7
[0x1370050] 6
[0x1370070] 5
[0x1370090] 4
[0x13700b0] 3
[0x13700d0] 2
[0x13700f0] 1
[0x1370110] 0
-> [0x1370030] 7
Loop starts at [0x1370030] 7
alexa@ubuntu:~/find_the_loop$ 

If you want to use source file instead of the libloop.a library, please use this file lib.c

And compile it with this command: $ gcc -Wall -pedantic -Werror -Wextra 0-main.c 0-find_loop.c lib.c -o main
```

## **Author** :black_nib:

* **Queise Carvalho de Oliveira** - [Linkedin](https://www.linkedin.com/in/queise-carvalho-de-oliveira-50359749/)


## License :page_with_curl:
This project is licensed under the [MIT License](https://opensource.org/license/mit/).
