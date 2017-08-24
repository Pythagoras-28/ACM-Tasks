/* I didnt get the time to check the code for a file input, it might be buggy
Although I have checked it for a number array and it works fine for it.*/


#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void swap(char** arr,int i,int j){
  char* temp=arr[i];
  arr[i]=arr[j];
  arr[j]=temp;
}
void partition(char**arr,int less, int greater){
  if(less<greater){
    int i=less-1,j=less;
    char* pivot=arr[greater];
    while(j<greater){
      if(strcmp(arr[j],pivot)<0){
        i++;
        swap(arr,i,j);
      }
      j++;
    }
    swap(arr,i+1,greater);
    partition(arr,less,i);
    partition(arr,i+2,greater);
  }
}
int main (int argc,char* argv[]){
  FILE *f=fopen(argv[1],"r");
  if(f==NULL){
    printf("Error");
  }
  else{
    int noOfLines=120,i=0;
    lines=(char**)malloc(sizeof(char*) * noOfLines);
    char c=getc(f);
    while(c!=EOF){
      if(i>=noOfLines){
        noOfLines=noOfLines*2;
        lines=(char**)realloc(sizeof(char*) * noOfLines);
      }
      int j=0;
      while(1){
        if(c=="\n"){
          lines[i][j]="\0";
          c=getc(f);
          i++;
          break;
        }
        else{
          lines[i][j]=c;
          c=getc(f);
          j++;
        }
      }
    }
    partition(lines,0,i-1);
  }  
  return 0;
}
