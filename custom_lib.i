%module custom_lib

%{
#define SWIG_FILE_WITH_INIT
#include "custom_lib.h"
%}

int fact(int n);
int anagram(char *str1, char *str2);
