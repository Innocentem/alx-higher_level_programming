#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: pntr to head of the linked list.
 * @number: number to insert.
 *
 * Return: If fnctn fails - NULL.
 * Else - a pntr to  new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new, *tmp;

	if (*head == NULL)
		return (NULL);

	node = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	while (node && node->next->n < number)
		node = node->next;

	tmp = node->next;
	node->next = new;
	new->next = tmp;

	return (new);
}
