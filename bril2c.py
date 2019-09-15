import json
import sys
import operator
json_str = sys.stdin.read()
#print(json_str)
obj = json.loads(json_str)
#print(obj)
def main_template(body):
    template = """#include<stdio.h>
    int main(){{
        {}
    }}
"""
    return template.format(body)


body = """
    return 0;
"""
main_function = obj['functions'][0]
instrs = main_function['instrs']
variables = set()

def const(instr):
    declr = ""
    if instr["dest"] not in variables:
        declr = "int"
        variables.add(instr["dest"])
    value = instr["value"]
    
    #print("!!!!"+str(instr["value"]))
    if instr["type"] == "bool":
        if instr["value"] == False:
            value = 0
        else:
            value = 1
    return "{} = {};".format(instr["dest"], value)

def br(instr):
    return """if({})
            goto {};
        else
            goto {};
""".format(instr["args"][0], instr["args"][1], instr["args"][2])

def jmp(instr):
    return "goto {};".format(instr["args"][0])



def bprint(instr):
    return 'printf("%d\\n", {});'.format(instr["args"][0])

def arith(instr):
    ops={"add":"+",
    "sub":"-",
    "mul":"*",
    "div":"/"
    }
    op = ops[instr["op"]]
    declr = ""
    if instr["dest"] not in variables:
        variables.add(instr["dest"])
    return "{} = {} {} {};".format(instr["dest"], instr["args"][0], op, instr["args"][1])

def compare(instr):
    ops = {"eq": "==",
          "lt": "<",
          "gt": ">",
          "le": "<=",
          "ge": ">="}
    op = ops[instr["op"]]
    if instr["dest"] not in variables:
        declr = "int"
        variables.add(instr["dest"])
    return "{} = {} {} {};".format(instr["dest"], instr["args"][0], op, instr["args"][1])

def nop(instr):
    return ""

def ret(instr):
    return "return 0;"

opcode = {
"const":const,
"br": br,
"jmp":jmp,
"print":bprint,
"add":arith,
"mul":arith,
"sub":arith,
"div":arith,
"eq":compare,
"lt":compare,
"gt":compare,
"le":compare,
"ge":compare,
"nop":nop,
"ret":ret
}

def label(instr):
    return "{}:;".format(instr["label"])

body = []
for i in instrs:
    #print(i)
    if "op" in i:
        code = opcode[i["op"]](i)
    elif "label" in i:
        code = label(i)
    body.append(code)

declr = ["int {};".format(v) for v in variables]
    

print(main_template("\n".join(declr+body)))
