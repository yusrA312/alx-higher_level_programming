#include "monty.h"
/**
 * ro_tl - rotates the list left
 * @stack: pointer to the top of the stack
 * @line: the index of the current line
 *
 */
void ro_tl(stack_t **stack, __attribute__ ((unused))unsigned int line)
{
	stack_t *run;
	int temp1, temp2;

	if (*stack == NULL)
		return;
	run = *stack;
	while (run->next)
		run = run->next;
	while (run)
	{
		if (!run->next)
		{
			temp1 = run->n;
			run->n = (*stack)->n;
		}
		else
		{
			temp2 = run->n;
			run->n = temp1;
			temp1 = temp2;
		}
		run = run->prev;
	}
}
/**
 * ro_tr - rotates the list right
 * @stack: pointer to the top of the stack
 * @line: the index of the current line
 *
 */
void ro_tr(stack_t **stack, __attribute__ ((unused))unsigned int line)
{
	stack_t *run1, *run2;
	int temp1, temp2;

	if (*stack == NULL)
		return;

	run1 = *stack;
	run2 = *stack;
	while (run1->next)
		run1 = run1->next;
	while (run2)
	{
		if (run2->prev == NULL)
		{
			temp1 = run2->n;
			run2->n = run1->n;
		}
		else
		{
			temp2 = run2->n;
			run2->n = temp1;
			temp1 = temp2;
		}
		run2 = run2->next;

	}
}
