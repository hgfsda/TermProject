#include "python.h" 

static PyObject *

getpw(PyObject *self, PyObject *args)
{	
	const char* pw = "wwzgbronrxdcrnfs";

	return Py_BuildValue("s", pw);
}

static PyMethodDef SpamMethods[] = {
	{ "getpw", getpw, METH_VARARGS,
	"get pw" },
	{ NULL, NULL, 0, NULL } // �迭�� ���� ��Ÿ���ϴ�.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"getpw",            // ��� �̸�
	"get pw", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
