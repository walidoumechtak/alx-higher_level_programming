#include "lists.h"

/**
 * size_list - function that calculate the size of the linked list
 * @head: the head of the linked list
 * Return: the length of the linked list
 */

int	size_list(listint_t *head)
{
	int	i;

	i = 0;
	while (head != NULL)
	{
		i++;
		head = head->next;
	}
	return (i);
}

/**
 * is_palindrome - function that check if a linked list is palindrom
 * @head: the addr of the head
 * Return: 1 if it is pali or 0 if its not
 */

int is_palindrome(listint_t **head)
{
	listint_t	*half;
	listint_t	*new;
	int	len;
	int	i;

	half = NULL;
	if (head == NULL || *head == NULL)
		return (0);
	len = size_list(*head) / 2;
	//i = len - (len / 2) + 1;
	while (i < len)
	{

	}
	
	return (0);
}
