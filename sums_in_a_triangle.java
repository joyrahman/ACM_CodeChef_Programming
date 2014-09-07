import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
 
 
 
public class Main{
 
    public static void main(String[] args) throws Exception{
	new Main().solve(true);
	
    } //end of Main Method
 
    private void solve(boolean submit) throws Exception{
	
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	  
	/*
	if(submit)
	    {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    }
	*/    
	/*else 
	    {
		BufferedReader br = new BufferedReader(new FileInputStream('file/SUMTRIAN.in'));
	    }
	*/
	
 
	//BufferedReader br = new BufferedReader(new InputStreamReader(submit?System.in:new FileInputStream('SUMTRIAN.in')));
	//PrintWriter pw = new PrintWriter(System.out);
	int n = Integer.parseInt(br.readLine().trim());
	
	//run the program for n times
	for (int L=0;L<n;L++)
	{
	    int no_of_rows = Integer.parseInt(br.readLine().trim());
	    int [] [] triangle = new int [no_of_rows][no_of_rows];
	    //process Input
	    for (int i=0;i<no_of_rows;i++)
		{
		    String[] row = br.readLine().split(" ");
		    //fill-up the triangle with inputs
		    for(int j=0;j<=i;j++)
			{
			    triangle[i][j]= Integer.parseInt(row[j]);
			}
		}	
		//Apply the Calculation
		for(int i = no_of_rows-2;i>=0;i--)
			{
			    for(int j=0;j<=i;j++)
				{
				    triangle[i][j] += triangle[i+1][j]>triangle[i+1][j+1]?triangle[i+1][j]:triangle[i+1][j+1];
			//	    pw.write(triangle[i][j]);
				}
			}
 
		//print the result
		//pw.write(triangle[0][0]);
		System.out.println(triangle[0][0]);
 
		    
 
	} //end of outer for
 
 
	} //end of function
 
} 
