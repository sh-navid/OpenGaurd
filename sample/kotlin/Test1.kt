/*
    NOTICE: All of unformatting in this file is by design to test obfuscator
    so do not format this code
*/
// Start of empty lines



// End of empty lines
fun main() {
    val v1 = "our"        		 // This is comment1
    val v2 = "counter"// This is comment2
    println("This is $v1 "+v2)        // To use this vars


    var x=12
    x+=1



    var b=true/* To test variable detector */
    b=!b

    
    for (k in 10..15) {           
        print("\n$v1 $k "+x + "|$b")
    }
}