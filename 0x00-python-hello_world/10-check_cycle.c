/*
 * File: 10-check_cycle.c
 * Auth: Mwebaze Innocent
 */

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If  no cycle - 0.
 *         If there's a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}
