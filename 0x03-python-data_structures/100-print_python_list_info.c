#include <Python.h>
/**
 * print_python_list_info - print basic info 
 * @p: object list
 */
void print_python_list_info(PyObject *p)
{
	int size, allo, l;
	PyObject *objet;
	size = Py_SIZE(p);
	allo = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allo);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		object = Py_List_Get_Item(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
