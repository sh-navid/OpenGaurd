import sys
from src.file import File
from src.comment import KotlinComment,PythonComment,JsComment
from src.cleaner import KotlinCleaner,PythonCleaner,JsCleaner
from src.variable import KotlinVariable,PythonVariable,JsVariable
from src.security import Security

# ----------------------------------------------------------------------------

root=sys.path[0]

services=[
    {"ext":".kt", "lang":"kotlin", "engine":KotlinVariable, "actions":[
        KotlinComment.remove_linear,
        KotlinComment.remove_multiline,
        KotlinCleaner.remove_emptylines,
    ]},
    {"ext":".py", "lang":"python", "engine":PythonVariable, "actions":[
        PythonComment.remove_linear,
        PythonComment.remove_multiline,
        PythonCleaner.remove_emptylines,
]},
    {"ext":".js", "lang":"js", "engine":JsVariable, "actions":[
        JsComment.remove_linear,
        JsComment.remove_multiline,
        JsCleaner.remove_emptylines,
    ]},
]

for service in services:
    test_in=root+f"/sample/{service['lang']}/Test1{service['ext']}"
    test_out=root+f"/build/{service['lang']}/Test1{service['ext']}"

    # ----------------------------------------------------------------------------

    content=File.read(test_in)

    # ----------------------------------------------------------------------------

    for action in service["actions"]:
        content=action(content)

    # ----------------------------------------------------------------------------

    # FIXME: x[1]!='' and not x[1].startsWith("__") is a temprory fix for python language; remove this for other languages
    vars = [x[1] for x in service["engine"].find_variables(content) if x[1]!='' and not x[1].startswith("__")] 
    print(vars)

    # ----------------------------------------------------------------------------

    var_map=[service["engine"].generate_random_name(12) for _ in vars]
    print(var_map) 

    # ----------------------------------------------------------------------------
    # Untrusted code; this is just for test
    for i in range(0,len(vars)):
        content=content.replace(vars[i],var_map[i])

    # ----------------------------------------------------------------------------for i in range(0,len(vars)):
    #     content=content.replace(vars[i],var_map[i])
        
    # FIXME: this section is ended because its not going to work in python; fix it
    output=content # FIXME: its just a temprory fix; remove this line later
    # output=content+"\n/*\n * [HASH]\n"
    # output+=" * "+Security.Hash.md5(content)+"\n"
    # output+=" * "+Security.Hash.sha1(content)+"\n"
    # output+=" * "+Security.Hash.sha256(content)+"\n"
    # output+=" */"

    File.write(test_out,output)
    print(output)
