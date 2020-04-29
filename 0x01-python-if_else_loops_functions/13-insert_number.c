#include "lists.h"

/**
 * insert_node - Inserts an integer in a determinated node
 * @head: head of the list
 * @number: number to add
 * Return: List
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temporal = *head;
	unsigned int i = 0, flag = 0;

	while (temporal)
	{
		if (temporal->n < number && temporal->next->n > number)
		{
			i++;
			flag = 1;
			break;
		}

		i++;
		temporal = temporal->next;
	}
	if (flag == 1)
		return (insert_nodeint_at_index(head, i, number));

	return (*head);
}

/**
 * insert_nodeint_at_index - inset a node in the given head
 * @head: head of the list
 * @idx: index
 * @n: number to set
 * Return: return the new node
 */

listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	unsigned int i = 0;
	listint_t *new, *temporal;

	temporal = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;

	if (idx == 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (temporal != NULL && i < (idx - 1))
	{
		temporal = temporal->next;
		i++;
	}

	if (temporal == NULL)
	{
		return (NULL);
	}

	new->next = temporal->next;
	temporal->next = new;

	return (new);
}
