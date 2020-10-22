#include <string>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    
    int index=0;
    sort(works.begin(), works.end(), greater<int>());
    
    for(int i=0; i<n; i++){
        if(works[index]>0){
            works[index]--;
        }
        
        if(index==works.size()-1){
            index=0;
        }else if(works[index] < works[index+1]){
            index++;
        }else{
            index=0;
        }
    }
    
    
    for(int i=0; i<works.size(); i++){
        answer = answer+works[i]*works[i];
    }

    return answer;
}
