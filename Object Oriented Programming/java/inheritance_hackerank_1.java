import java.io.*;
import java.util.*;


class Arithmetic{
        int add(int x, int y){
                int z =  x+y;
                return z;
            }
    }
class Adder extends Arithmetic{
        
    }

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
       Adder a = new Adder();
       System.out.println("My superclass is: "+ a.getClass().getSuperclass().getName());  
       System.out.println(a.add(32,10)+" "+a.add(3,10)+" "+a.add(18,2)+"\n");     
    }
}