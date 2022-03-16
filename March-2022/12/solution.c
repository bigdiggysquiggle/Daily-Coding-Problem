#include <unistd.h>

//March 12, 2022
//the following should be treated as a mockup of the algorithm
//designed to show an understanding of the question and how it
//would be implemented. As such I have not provided any test
//code for the time being. I intend to rewrite this code
//into a working example in C++ so I can implement this as a
//class with methods, as the wording of the challenge implies.
//However I felt personally that this was acceptable for the
//time being as a simple illustration of the concept the
//challenge was aimed towards testing my understanding of.

typedef struct s_node; {
	void	*val;
	size_t	x_or;
};	t_node

t_node	*make_node(void *val)
{
	t_node	new = malloc(sizeof(t_node));
	new->val = val;
	return new;
}

void	add_node(t_node *head, t_node *new)
{
	if (!head) //sanity check
		return ;
	size_t prev = (size_t)head;
	size_t tmp = 0;
	t_node *iter = (t_node *)head->x_or;
	if (!iter) //we only have a head so add the new node
	{
		head->x_or = (size_t)new;
		new->x_or = (size_t)head;
		return ;
	}
	while (prev != iter->x_or)
	{ //if prev == x_or we're at the end
		tmp = iter->x_or ^ prev; //get next
		prev = (size_t)iter; //advance prev
		iter = (t_node *)tmp; //advance iter
	}
	iter->x_or ^= (size_t)new;
	new->x_or = (size_t)iter;
}

t_node	*get(size_t i, t_node *head)
{
	if (!i) //we've been asked for the first item
		return head;
	if (!head) //the list doesn't exist
		return NULL;
//the above sanity checks could be performed in any order
//as in the event that i is 0 && head is NULL, I'm still
//returning NULL during the check to see if i > 0
	size_t count = 1; //we've already checked to see if the head has been requested
	size_t prev = (size_t)head;
	size_t tmp = 0;
	t_node *iter = (t_node *)head->x_or;
	while (count < i)
	{//when count == i, we've reached the node we want
		tmp = iter->x_or ^ prev;//get the address of next
		prev = (size_t)iter;//advance prev
		iter = (t_node *)tmp;//advance iter
		count++;
	}
	return iter;
}
