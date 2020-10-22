#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer;
    
    if(s<n){
        answer.push_back(-1);
    }
    else if(s%n==0){
            int tmp = s/n;
            for(int i=0; i<n; i++)
                answer.push_back(tmp);
            
    }else{
        int q = s/n;
        int r = s%n;
        for(int i=0; i<n; i++){
            if(i<n-r)
                answer.push_back(q);
            else
                answer.push_back(q+1);
        }
    }
    
    return answer;
}
