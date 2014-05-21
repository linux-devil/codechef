#include <iostream>
#include <cstring>
#include <stack>
#include <cstdio>
#include <algorithm>
using namespace std;
#define maxn 1000000
char x[maxn];
int c[maxn];
int d[maxn];
int main(void)
{
  int n,i;
  scanf("%d",&n);

  for(i=0;i<n;i++)
    {

      //char x[1000000];
      scanf("%s",x);
      int len = strlen(x);
      int j;
      int flag = 0;
      if(x[0]=='>'){
        printf("%d\n",0);
        continue;
        }

      //int c[len];
      //int d[len];
      fill(c,c+len,-1);
      fill(d,d+len,-1);
      int maxx=0;
      int q,manu;
      stack<int> s;
      for(j=0;j<len;j++)
      {
          if(x[j]=='<')
            s.push(j);
          else{

            if(!s.empty())
            {
              d[j]=s.top();
              s.pop();
              c[j]=d[j];
              q = d[j]-1;
              if(q>0 && x[q]=='>' && c[q]!=-1)
                c[j]=c[q];
              manu = j-c[j]+1;
              if (s.empty()){
              if(maxx<manu)
                maxx = manu;}
            }
            else{
              printf("%d\n",maxx);flag=1;break;
            }
          }
      }
      if(flag==0){
        printf("%d\n",maxx);
      //else
        //printf("%d\n",0);
    }
  }
  return 0;
}
