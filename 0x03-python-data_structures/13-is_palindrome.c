#include "lists.h"

/**
 * is_palindrome - is_palindrome
 * @head: head
 * Return: return
 */

int is_palindrome(listint_t **head)
{
	int counter = 0;
	dlistint_t *new, *copy;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	while ((*head))
	{
		add_dnodeint_end(&new, (*head)->n);
		(*head) = (*head)->next;
		counter++;
	}
	copy = new;

	while (copy->next)
		copy = copy->next;

	while (new)
	{
		if (copy->n == new->n)
		{
			copy = copy->prev;
			new = new->next;
		}
		else
			return (0);
	}
	return (1);
}

/**
 * add_dnodeint_end - function that adds a node at the end
 * @head: head of the list
 * @n: number of the instance
 * Return: new list
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new, *temp;

	temp = *head;

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (!*head)
	{
		new->prev = NULL;
		*head = new;
	}
	else
	{
		while (temp->next)
			temp = temp->next;

		new->prev = temp;
		temp->next = new;
	}

	return (new);
}
