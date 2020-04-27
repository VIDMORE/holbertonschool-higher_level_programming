#include "lists.h"

/**
 * check_cycle - checks if there is a cycle
 * @list: list to examinate
 * Return: 1 if true, 0 if false
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *current;

	head = list;
	current = list;

	while (head)
	{
		while (head && current)
		{
			if (head == current->next)
				return (1);

			current = current->next;
		}
		head = head->next;
	}
	return (0);
}
