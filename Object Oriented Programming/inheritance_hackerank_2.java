import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        MyBook b = new MyBook();
        Scanner input = new Scanner(System.in);
        String title = input.nextLine();
        b.setTitle(title);
        System.out.println("The title is: "+ b.getTitle()+"\n");
        
    }
}

abstract class Book{
    String title;
    //abstract void setTitle(String s);
    String getTitle(){
        return title;
    }
}

class MyBook extends Book {
    void setTitle(String s){
       title = s; 
    }
}