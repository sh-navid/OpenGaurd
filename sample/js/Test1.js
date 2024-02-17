/*
    NOTICE: All of unformatting in this file is by design to test obfuscator
    so do not format this code
*/
// Start of empty lines



// End of empty lines
const main = () => {
  const v1 = "our"                 // This is comment1
  let v2 = "counter"; // This is comment2
  console.log(`This is ${v1} ` + v2);         // To use this vars


  var x = 12
  x += 1



  var b = true /* To test variable detector */
  b = !b;


  // FIXME: if you have `let k`?
  for (k = 10; k <= 15; k++) {
    console.log(`\n${v1} ${k} ` + x + `|${b}`);
  }
};


main()
