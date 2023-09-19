#include "lists.h"
/**
 * insert_node - insert a number
 * @head: linked list
 * @number: insert the number
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
	node = node->next;
	node->next = new;
	return(new);
}
