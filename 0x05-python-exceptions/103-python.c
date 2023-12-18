#include <Python.h>
#include <stdio.h>
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s = 0;
	PyObject *it;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		s = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < s)
		{
			it = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, it->ob_type->tp_name);
			if (PyBytes_Check(it))
				print_python_bytes(it);
			else if (PyFloat_Check(it))
				print_python_float(it);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double v = 0;
	char *sing = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	v = ((PyFloatObject *)p)->ob_fval;
	sing = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", sing);
}
/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t sz = 0, i = 0;
	char *sg = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sz = PyBytes_Size(p);
	printf("  size: %zd\n", sz);
	sg = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", sg);
	printf("  first %zd bytes:", sz < 10 ? sz + 1 : 10);
	while (i < sz + 1 && i < 10)
	{
		printf(" %02hhx", sg[i]);
		i++;
	}
	printf("\n");
}

