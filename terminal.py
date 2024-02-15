import sys
from src.file import File
from src.comment import Comment
from src.cleaner import Cleaner
from src.variable import Variable
from src.security import Security

# ----------------------------------------------------------------------------

root=sys.path[0]
test_in=root+"/sample/kotlin/Test1.kt"
test_out=root+"/build/kotlin/Test1.kt"

# ----------------------------------------------------------------------------

content=File.read(test_in)

# ----------------------------------------------------------------------------

actions=[
    Comment.remove_linear,
    Comment.remove_multiline,
    Cleaner.remove_emptylines,
]
for action in actions:
    content=action(content)

# ----------------------------------------------------------------------------

vars = [x[1] for x in Variable.find_variables(content)]
# print(vars)

# ----------------------------------------------------------------------------

var_map=[Variable.generate_random_name(24) for _ in vars]
# print(var_map) 

# ----------------------------------------------------------------------------
# Untrusted code; this is just for test
for i in range(0,len(vars)):
    content=content.replace(vars[i],var_map[i])

# ----------------------------------------------------------------------------
output=content+"\n/*\n * [HASH]\n"
output+=" * "+Security.Hash.md5(content)+"\n"
output+=" * "+Security.Hash.sha1(content)+"\n"
output+=" * "+Security.Hash.sha256(content)+"\n"
output+=" */"

File.write(test_out,output)
print(output)
