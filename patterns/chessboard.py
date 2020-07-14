"""class Solution {
  public static void Met(int N, String start) {
      /* write your solution here */
      char p=start.charAt(0);
      for (int i=0;i<N;i++){
          for(int j=0;j<N;j++){
              if(p=='W')
               {   System.out.print(p);
              p='B';}
          else
           {   System.out.print(p);
          p='W';}}
      if(N%2==0){
          if(p=='W')
              p='B';
          else
              p='W';}
      System.out.println();
  }
}
}"""

for _ in range(int(input())):
    n=int(input())
    for i in range(1,n+1):
        if i%2==0:
            p='B'
            for j in range(n):
                print(p,end="")
                if p=='W':
                    p='B'
                else:
                    p='W'
            print()
                
        else:
            p='W'
            for j in range(n):
                print(p,end="")
                if p=='W':
                    p='B'
                else:
                    p='W'

            print()


