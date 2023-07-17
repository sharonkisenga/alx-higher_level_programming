#include "lists.h"
/**
 * pal - determine if list is palindrome
 * @start: position of list
 * @end: position of list
 * return: 1
 */
int pal(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (pal(start, end->next) == 1 && (*start)->n == end->n)
	{
		*start = (*start)->next;
		return(1);
	}
	return (0);
}
/**
 * is_palindrome - is a palindrome linked list a list
 * @haed: list to check
 * return: 1 
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	return (pal(head, *head));
}
