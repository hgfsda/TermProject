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
	{ NULL, NULL, 0, NULL } // 배열의 끝을 나타냅니다.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"getpw",            // 모듈 이름
	"get pw", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
