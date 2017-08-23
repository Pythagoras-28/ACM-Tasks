#include<stdio.h>
int can_be_divided(int size){
  if (size==1)
    return 0;
  else{
    int cummulative_sum[size],count,temp;
    scanf("%d",cummulative_sum);
    for(count=1;count<size;count++){
      scanf("%d",&temp);
      cummulative_sum[count]=cummulative_sum[count-1]+temp;
    }
    if(cummulative_sum[size-1]%2!=0){
      return 0;
    }
    else{
      temp=cummulative_sum[size-1]/2;
      for(count=0;count<size;count++){
        if(cummulative_sum[count]==temp)
          return 1;
      }
      return 0;
    }
  }
}
int main (void){
  unsigned size;
  scanf("%u",&size);
  printf("%d\n",can_be_divided(size));
  return 0;
}
