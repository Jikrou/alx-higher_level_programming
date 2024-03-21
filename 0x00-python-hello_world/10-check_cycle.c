#include "lists.h"
/**
* check_cycle - check if a linked list has a cylcle
* @list: pointer to the head of the linked list
* Return: 1 if a cycle has found, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	listint_t *cunx = list->next;

	if (list == NULL || list->next == NULL)
		return (0);

   	while (cunx != NULL && cunx->next != NULL)
		{
			if (curr == cunx)
				   return (1);

			curr = curr->next;
			cunx = cunx->next->next;
		}

	return (0);
}
