#include "custom_lib.h"
#include <stdio.h>
#include <curses.h>
#include <string.h>

int fact(int n) {
    if (n < 0){
        return 0;
    }
    if (n == 0) {
        return 1;
    }
    else {
        return n * fact(n-1);
    }
}

int anagram(char *str1, char *str2) {
    int length, i, j, found=0;
    length = strlen(str1);
    if(length == strlen(str2)){
        for(i=0; i<length; i++){
            found = 0;
            for(j=0; j<length; j++){
                if(str1[i] == str2[j]){
                    found = 1;
                    break;
                }
            }
        }
        if(found == 0)
            return 0;
        else
            return 1;
    }
    else
        return 0;
}