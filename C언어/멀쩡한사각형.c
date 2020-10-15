#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long gcd(int a, int b){
    long tmp, n;
    if(a<b){
        tmp=a;
        a=b;
        b=tmp;
    }
    while(b!=0){
        n=a%b;
        a=b;
        b=n;
    }
    
    return a;
}

long long solution(int w, int h) {
    long long answer;
    long long W = w;
    long long H = h;
    long long gcd_num = gcd(w,h);
    
    answer = W*H - (w + h - gcd_num);
    
    return answer;
}
