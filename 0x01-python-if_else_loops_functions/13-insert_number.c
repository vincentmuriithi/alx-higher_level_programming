#include "lists.h"
/**
* insert_node - inserts a namba in a sorted singly list
* @head: input pointer
* @number: umber to be inserted
* Return: returns the list
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new = *head;
listint_t *node =  malloc(sizeof(listint_t));

if (node)
return (NULL);
node->n = number;
node->next = NULL;

if (new == NULL || (new->next == NULL && new->n >= number))
{
node->next = new;
*head = node;
return (node);
}
while (new && new->next != NULL && new->n <= number)
{
new = new->next;

}
new->next = node;
return (node);

}
