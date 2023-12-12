#include "monty.h"
/**
 *ro_tl- rotates the stack to the top
 *@head: stack head
 *@counter: line_number
 *Return: no return
 */
void ro_tl(stack_t **head,  __attribute__((unused)) unsigned int counter)
{
	stack_t *tmp = *head, *aux;

	if (*head == NULL || (*head)->next == NULL)
	{
		return;
	}
	aux = (*head)->next;
	aux->prev = NULL;
	while (tmp->next != NULL)
	{
		tmp = tmp->next;
	}
	tmp->next = *head;
	(*head)->next = NULL;
	(*head)->prev = tmp;
	(*head) = aux;
}
/**
 * ro_tr - rotates the list right
 * @head: pointer to the top of the stack
 * @counter: the index of the current line
 *
 */
void ro_tr(stack_t **head, __attribute__((unused)) unsigned int counter);
#include "monty.h"
/**
 *ro_tr- rotates the stack to the bottom
 *@head: stack head
 *@counter: line_number
 *Return: no return
 */
void ro_tr(stack_t **head, __attribute__((unused)) unsigned int counter)
{
	stack_t *copy;

	copy = *head;
	if (*head == NULL || (*head)->next == NULL)
	{
		return;
	}
	while (copy->next)
	{
		copy = copy->next;
	}
	copy->next = *head;
	copy->prev->next = NULL;
	copy->prev = NULL;
	(*head)->prev = copy;
	(*head) = copy;
}
