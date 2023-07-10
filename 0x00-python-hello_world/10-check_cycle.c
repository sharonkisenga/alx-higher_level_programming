#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: listint_t
 * return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *pop;
	listint_t *check;

	if (list == NULL || list->next == NULL)
		return (0);
	pop = list;
	check = pop->next;
	while (pop != NULL && check->next != NULL && check->next->next != NULL)
	{
	if (pop == check)
	return (1);
	pop = pop->next;
	check = check->next->next;
	}
	return (0);
}

