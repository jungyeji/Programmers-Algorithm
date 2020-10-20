#include <iostream>
#include <vector>
using namespace std;

int solution(vector<vector<int>> board)
{
    int answer = board[0][0];
    
    int row = board.size();
    int col = board[0].size();
    
    for(int i=1; i<row; i++){
        for(int j=1; j<col; j++){
            int num=0;
            if(board[i][j]!=0){
                num = min(board[i-1][j], board[i][j-1]);
                board[i][j] = min(num, board[i-1][j-1])+1;
                answer = max(answer, board[i][j]);
            }
        }
        
    }
    
    return answer*answer;
}
