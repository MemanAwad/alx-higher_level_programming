#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - function to check if the linked list contaon a cycle
 * @list: the linked list
 *
 * Return: 1 if there is cycle 0 if it not
 */

int check_cycle(listint_t *list)
{
	listint_t *tu, *ha;

	if (list == NULL || list->next == NULL)
		return (0);

	tu = list->next;
	ha = list->next->next;

	while (tu && ha && ha->next)
	{
		if (tu == ha)
			return (1);

		tu = tu->next;
		ha = ha->next->next;
	}
	return (0);
}
