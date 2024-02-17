// package sample.java;

/*
    NOTICE: All of unformatting in this file is by design to test obfuscator
    so do not format this code
*/
// Start of empty lines



// End of empty lines

class Test1{
    public static void main(String[] argv){
        String v1 = "our";        		 // This is comment1
        final String v2 = "counter";// This is comment2
        System.out.println(String.format("This is %s ",v1)+v2);        // To use this vars


        int x=12;
        x+=1;



        boolean b=true;/* To test variable detector */
        b=!b;

        
        for (int k=10;k<15;k++ ) {           
            System.out.println(String.format("\n$v1 %d ",k)+x + String.format("|%b",b));
        }
    }
}