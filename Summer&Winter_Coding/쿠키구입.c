#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// cookie_len은 배열 cookie의 길이입니다.
int solution(int cookie[], size_t cookie_len) {
    int max_sum = 0;
    int i;
    for(i=0; i<cookie_len-1; i++){
        int l=i;
        int r=i+1;
        int l_sum = cookie[l];
        int r_sum = cookie[r];
        
        while(true){
            if(l_sum==r_sum && max_sum<r_sum){
                max_sum=r_sum;    
            }
            if(l_sum<=r_sum && l>0){
                l--;
                l_sum = l_sum+cookie[l];
            }
            else if(l_sum>=r_sum && r<(cookie_len-1)){
                r++;
                r_sum = r_sum+cookie[r];
            }
            else{
                break;
            }
            
        }
        
    }
    
    return max_sum;
}
