import java.util.Scanner;
import java.util.Arrays;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
 
 
 
 
public class Main  {
 
 public static void main(String[] args) throws NumberFormatException, IOException {
  // TODO Auto-generated method stub
  Scanner scanner = new Scanner(System.in);
  int testCases = scanner.nextInt();
  int playersCount = 11;
  
  int scores[] = new int [playersCount];
 
  
  for (int i=0;i<testCases;i++)
  {
   for(int j=0;j<playersCount;j++){
    
    scores[j] = scanner.nextInt();
  }
   
   Arrays.sort(scores);
   int K = scanner.nextInt();
   int Index = playersCount - K;
   int Value = scores[Index];
   int right = 0;
   int rightIndex = Index+1;
   
   while (rightIndex<playersCount && scores[rightIndex]==Value)
   { 
    right++;
    rightIndex++;
   }
   
   int left = 0;
   int leftIndex = Index-1;
   
   while (leftIndex>=0 && scores[leftIndex]==Value)
   {
    left++;
    leftIndex--;
   }
   
   int N = left+1+right; // to choose from N numbers
   int R = right+1 ;  // to choose R Numbers from N
   int Q = N-R;
   int deno =1;
   int num= 1;
   
   for (int j=0;j<R;j++){
     num *= N-j;
    
   }
   
   /*for (int j=1;j<=R;j++){
       num*=j;
    
    
   }
   */
   //System.out.println(num);
   for (int j = 0; j < R; j++) {
        num /= R - j;
      }
   //System.out.println(num);
   //System.out.println(deno);
   //int result = deno/num;
   System.out.println(num);
   
  } //end of outer for
 
 }
 
} 
