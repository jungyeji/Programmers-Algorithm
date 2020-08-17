#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    int len=participant.size();
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for(int i=0; i<len; i++){
        if(participant[i] != completion[i])
            return participant[i];
    }
    return participant[len-1];
}
