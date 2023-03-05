#include <iostream>

class myList	{
	public:
		int val;
		myList* next;

		myList(int val)	{
			this->val = val;
			next = NULL;
		}
};

myList	*find_intersection(myList *head1, myList *head2)	{
	myList *ptr1 = head1;
	myList *ptr2 = head2;
	if (ptr1 == NULL || ptr2 == NULL)
		return NULL;
	while (ptr1 != ptr2)	{
		if (ptr1 == NULL)
			ptr1 = head2;
		if (ptr2 == NULL)
			ptr2 = head1;
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	return ptr1;
}

void print_list(myList *lst)	{
	myList *curr = lst;
	if (!lst)
		return;
	std::cout << curr->val;
	while (curr->next)	{
		curr = curr->next;
		std::cout << " " << curr->val;
	}
	std::cout << std::endl;
}

//3 7 8 10
//99 1 8 10
int main(void)	{
	myList *A = new myList(3);
	A->next = new myList(7);
	A->next->next = new myList(8);
	A->next->next->next = new myList(10);

	myList *B = new myList(99);
	B->next = new myList(1);
	B->next->next = A->next->next;

	std::cout << "A: ";
	print_list(A);
	std::cout << "B: ";
	print_list(B);

	myList *res = find_intersection(A, B);
	std::cout << "intersection: " << res->val << std::endl;
}
