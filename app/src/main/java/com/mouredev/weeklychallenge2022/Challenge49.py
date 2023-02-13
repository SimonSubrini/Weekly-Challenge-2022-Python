import re

def handles(txt):
    handles={}
    char1=re.compile(r"@\w+")
    char2=re.compile(r"#\w+")
    char3=re.compile(r"(?:https?://|www\.)[\w.-]+\.[a-z]{2,}")
    
    handles['user']=re.findall(char1,txt)
    handles['hashtag']=re.findall(char2,txt)
    handles['web']=re.findall(char3,txt)
    return handles

# test

print(handles("En esta actividad de @mouredev, resolvemos #retos de #programacion desde https://retosdeprogramacion.com/semanales2022, que @braismoure aloja en www.github.com"))
