#include "lists.h"

/**
 * check_cycle - function that checks for a loop in a linked list
 * @list: pointer to the first node
 * Return: 0 if theres no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = list;
	temp2 = list;

	while (temp2)
	{
		temp1 = temp1->next;
		temp2 = temp2->next->next;

		if (temp1 == temp2)
		{
			return (1);
		}

	}

	return (0);
}

