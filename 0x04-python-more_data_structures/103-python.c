#include <Python.h>

void print_python_list(PyObject *p) {
PyListObject *list = (PyListObject *)p;
Py_ssize_t size = PyList_Size(p);
Py_ssize_t allocated = list->allocated;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);
for (Py_ssize_t i = 0; i < size; i++) {
PyObject *element = PyList_GetItem(p, i);
const char *type = element->ob_type->tp_name;
printf("Element %ld: %s\n", i, type);
}
}

void print_python_bytes(PyObject *p) {
PyBytesObject *bytes = (PyBytesObject *)p;
Py_ssize_t size = PyBytes_Size(p);
const char *str = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);

printf("  first 10 bytes: ");
if (size > 10) {
size = 10;
}
for (Py_ssize_t i = 0; i < size; i++) {
printf("%02x%c", (unsigned char)str[i], i == size - 1 ? '\n' : ' ');
}
}
