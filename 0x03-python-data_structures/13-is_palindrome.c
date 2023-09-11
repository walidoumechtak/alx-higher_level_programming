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
 * reverse_list - reverse the linked list
 * @head: the head of linked list
 */

void	reverse_list(listint_t **head, )
{

}

/**
 * is_palindrome - function that check if a linked list is palindrom
 * @head: the addr of the head
 * Return: 1 if it is pali or 0 if its not
 */

int is_palindrome(listint_t **head)
{
	listint_t	*half;
	listint_t	*temp;
	int	len;
	int	half_len;
	int	i;

	half = NULL;
	temp = *head;
	if (head == NULL || *head == NULL)
		return (0);
	len = size_list(*head);
	half_len = len / 2;
	i = 0;
	while (i++ < half_len)
		temp = temp->next;
	if (len % 2 != 0)
		temp = temp->next;
	while (temp != NULL)
	{
		add_nodeint_end(&half, temp->n);
		temp = temp->next;
	}
	reverse_list(&half);
	free_listint(half);
	return (0);
}
