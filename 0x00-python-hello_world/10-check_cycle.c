#include "lists.h"
/**
* check_cycle - checks if a list has a cycle
* @list: the input list to be checked
* Return: returns 1 if there is a cycle and 0 if no cycle is found
*/
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

while(slow != NULL && fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);

}

return (0);
}
