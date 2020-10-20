#include <string>
#include <vector>
#include <bitset>
#include <iostream> 
using namespace std;

int solution(int n) {
    int answer = 0;
    string bi_n = bitset<8>(n).to_string();
    int n_count = 0;
    for(int i=0; i<bi_n.size();i++){
        if(bi_n[i]=='1')
            n_count++;
    }
    answer = n+1;
    while(answer>n){
        string bi_an = bitset<8>(answer).to_string();
        int an_count=0;
        for(int i=0; i<bi_an.size(); i++){
            if(bi_an[i]=='1')
                an_count++;
        }
        if(n_count==an_count)
            break;
        
        answer++;
    }
    
    return answer;
}
