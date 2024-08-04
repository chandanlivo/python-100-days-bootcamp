#Modifying a global variable
enemies = 1
def myfunc():
    global enemies
    enemies += 1
    print(enemies)
myfunc()
print(enemies)