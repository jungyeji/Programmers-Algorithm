#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int red) {
    vector<int> answer;
    int all = brown+red;
    
    for(int x=3; x<all; x++){
        if(all%x==0){
            int y = all/x;
            if((x-2)*(y-2)==red){
                answer.push_back(y);
                answer.push_back(x);
                break;
            }
        }
    }
    
    return answer;
}
