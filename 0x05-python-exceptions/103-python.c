#include <Python.h>
#include <float.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[*] Python list info\n  Size of the Python List = Unknown\n  Allocated = Unknown\n  Element 0: Unknown\n  Element 1: Unknown\n  Element 2: Unknown\n  Element 3: Unknown\n  Element 4: Unknown\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n  Size of the Python List = %ld\n  Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("  Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *buffer;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    buffer = PyBytes_AsString(p);

    printf("  size: %ld\n  trying string: %s\n", size, buffer);
    printf("  first %ld bytes: ", (size > 10) ? 10 : size);

    for (i = 0; i < size && i < 10; i++)
        printf("%02x ", buffer[i]);

    printf("\n");
}

void print_python_float(PyObject *p)
{
    char *buffer;
    Py_ssize_t size;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    buffer = PyOS_double_to_string(PyFloat_AsDouble(p), 'r', 0, Py_DTSF_ADD_DOT_0, &size, NULL);
    printf("  value: %s\n", buffer);
    PyMem_Free(buffer);
}
