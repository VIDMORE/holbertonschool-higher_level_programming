#include "lists.h"

/**
 * is_palindrome - is_palindrome
 * @head: head
 * Return: return
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);

	return (equal(head, *head));
}

/**
 * is_palindrome - is_palindrome
 * @head: head
 * Return: return
 */

int equal(listint_t **first, listint_t *last)
{
	if (!last)
		return (1);

	if (equal(first, last->next))
	{
		
		if ((*first)->n == last->n)
		{
			*first = (*first)->next;
			return (1);
		}
	}

	return (0);
}