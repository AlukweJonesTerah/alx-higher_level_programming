#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_bytes - func 1
 * @bytes_object: args2
 */
void print_python_bytes(PyObject *bytes_object)
{
	long int size;
	int i = 0;
	char *byte_string = NULL;

	printf("[.] Bytes object info\n");
	if (!PyBytes_Check(bytes_object))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(bytes_object, &byte_string, &size);

	printf("  Size: %li\n", size);
	printf("  Byte string: %s\n", byte_string);
	if (size < 10)
		printf("  First %li bytes:", size + 1);
	else
		printf("  First 10 bytes:");
	while (i <= size && i < 10)
	{
		printf(" %02hhx", byte_string[i]);
		i++;
	}
	printf("\n");
}
/**
 * print_python_list - func 1
 * @python_list: args4
 */
void print_python_list(PyObject *python_list)
{
	long int size = PyList_Size(python_list);
	int i;
	PyListObject *list_object = (PyListObject *)python_list;
	const char *type_name;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list_object->allocated);
	for (i = 0; i < size; i++)
	{
		type_name = (list_object->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type_name);
		if (!strcmp(type_name, "bytes"))
			print_python_bytes(list_object->ob_item[i]);
	}
}
