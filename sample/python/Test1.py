"""
    NOTICE: All of unformatting in this file is by design to test obfuscator
    so do not format this code
"""
# Start of empty lines



# End of empty lines
if __name__=="__main__":
    # FIXME: v1 and v2 should obfuscate; fix it please
    v1 = "our"        		 # This is comment1
    v2 = "counter"# This is comment2
    print(f"This is {v1} "+v2)        # To use this vars


    x=12
    x+=1



    b=True
    ''' To test variable detector ''' # It seems that we cannot put this line in front of `b=True`
    b=not b

    # TODO: in next `testcase` check if owr variable name is `f` then f"|{b}" will obfuscate correctly or not
    for k in range(10,15):
        print(f"\n{v1} {k} "+str(x) + f"|{b}")