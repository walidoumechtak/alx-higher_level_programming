#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - func that insert a node in sorted linkedlist
 * @head: the head of the linked list
 * @number: the value of n
 * Return: the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t	*new;
	listint_t	*temp;
	listint_t	*needed;
	int	index;

	if (!head || !*head)
		return (NULL);
	temp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	index = 0;
	while (temp != NULL)
	{
		if (number >= temp->n)
		{
			break;
		}
		index++;
		needed = temp;
		temp = temp->next;
	}
	needed->next = new;
	new->next = temp;
	return (new);
}
