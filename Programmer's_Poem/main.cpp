/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/


/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <iostream>
#include <cmath>
#include <vector>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <string>
using namespace std;
int main()
{  
    int ryhmes,lines;
    cin >>ryhmes>> lines;
    cin.ignore();
    
    string input;
  
    string line;
    vector<string> alphabet;
    vector<vector<string>>pos;
    pos.resize(lines);
   
    for (char letter = 'A'; letter <= 'Z'; ++letter) {
        if (letter == 'X') {
            continue; // Skip the letter 'X'
        }
        string letterString(1, letter); // Convert char to string
        alphabet.push_back(letterString);
    }


    vector<vector<string>> linesOfWords; // Vector of vectors to store words from each line

   // cout << "Enter lines of text (Ctrl+D or Ctrl+Z to end input):\n";

    // Read lines of text in a loop until EOF (Ctrl+D or Ctrl+Z)
    while (getline(cin, line)) {
        istringstream iss(line);
        string word;
        vector<string> wordsInLine; // Vector to store words from the current line

        // Tokenize the input line into words and store in the vector
        while (iss >> word) {
            wordsInLine.push_back(word);
        }

        // Clear the input stream to handle any remaining newline characters
        // Store the words of the current line in the vector of vectors
        linesOfWords.push_back(wordsInLine);
    }   
    
    vector<string>all_words;
    
    for(int i=ryhmes+1;i<ryhmes +lines+1;i++){
        
       
        string lastWord = linesOfWords[i][linesOfWords[i].size() - 1];
        all_words.push_back(lastWord);
        
        
        
    }
    vector<int>index;


    for(int j=0; j<ryhmes;j++){
        int count=0;
            for(int i=0;i<linesOfWords[j].size();i++){
                    
                    auto it = find(all_words.begin(), all_words.end(),linesOfWords[j][i] );
                    if(it != all_words.end()){
                        count++;
                    }
                    if (count==2){
                        
                        break;
                    }    
            }
            if(count==1){
                index.push_back(j);
            }
    }
    int warning;
    warning=0;
  
    int flag=0;
    int counter=0;
    for(int i=ryhmes+1;i<ryhmes +lines+1;i++){
        flag=0;
       // for(int j=0; j<linesOfWords[i].size();j++){
        //cout<<linesOfWords[i][j]<<endl;
            string lastWord = linesOfWords[i][linesOfWords[i].size() - 1];
        //}
        for(int j=0; j<ryhmes;j++){
            
            for(int k=0;k<index.size();k++){
               if(j==index[k]){
                   cout<<"X";
                   warning=1;
                   break;
                }
            }       
        
           auto it = find(linesOfWords[j].begin(), linesOfWords[j].end(), lastWord);
           if (it != linesOfWords[j].end()&& warning==0) {
                if (pos[j].size()==0){
                  pos[j].push_back(alphabet[counter]);
                  cout<<alphabet[counter];
                  counter++;
                    
                }else{
                   cout<<pos[j][0] ;
                }
                   flag=1;
                   break;
           }
           if(flag!=1 && warning==0)
           {
                for (char &c : lastWord) {
                    c = tolower(c);
                }
                auto it = find(linesOfWords[j].begin(), linesOfWords[j].end(), lastWord);
               if (it != linesOfWords[j].end()) {
                    if(pos[j].size()==0){
                      pos[j].push_back(alphabet[counter]);
                      cout<<alphabet[counter];
                      counter++;
                        
                    }else{
                       cout<<pos[j][0];
                    }
                       flag=1;
                       break;
                }
           }
        }
        if (flag==0 ){
            cout<<"X";
            
        }
        
    }
 
    return 0;
}



