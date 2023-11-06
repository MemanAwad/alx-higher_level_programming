#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * pali - check if it is palindrome
 * @arr: pointer to the linked list
 * @index1: first index
 * @incesx2: second index
 *
 * Return: 1 or 0
 */
int pali(int *arr, int index1, int index2)
{
	if (index1 > index2)
		return (1);
	if (arr[index1] != arr[index2])
	{
		return (0);
	}
	return (pali(arr, index1 + 1, index2 -1));
}
/**
 * is_palindrome - function to check if the linked list is palindrome
 * head - the head of the list
 *
 * Retrun 1 if it is 0 otherrwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int i = 0;
	const listint_t *temp = *head;
	int *arr;

	if (!*head)
		return (1);
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	temp = *head;
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);
	for (i = 0; i <= (len - 1); i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	if (pali(arr, 0, len -1) == 1)
	{
		free(arr);
		return(1);
	}
	free(arr);
	return (0);
}
