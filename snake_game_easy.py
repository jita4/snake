def fruit_delete(coord, fruit_del):
    l=len(coord)-1
    x4=coord[l][0]
    y4=coord[l][1]
    if fruit_del[0][0]==x4:
        if fruit_del[0][1]==y4:
            fruit_del.pop(0)
    return fruit_del    

def movement(coordin, direct, fruit):
    c=len(coordin)-1
    x=coordin[c][0]
    y=coordin[c][1]
    if direct=='e':
        x1=x
        y1=y+1
        if y1>10:
            coordin=[(0,0)]
        else:
            for i in range(1):
                coordin.append((x1,y1))
    if direct=='s':
        x1=x+1
        y1=y
        if x1>10:
            coordin=[(0,0)]
        else:
            for i in range(1):
                coordin.append((x1,y1))
    if direct=='n':
        x1=x-1
        y1=y
        if x1<0:
            coordin=[(0,0)]
        else:
            for i in range(1):
                coordin.append((x1,y1))
    if direct=='w':
        x1=x
        y1=y-1
        if y1<0:
            coordin=[(0,0)]
        else:
            for i in range(1):
                coordin.append((x1,y1))
    x_last=coordin[0][0]
    y_last=coordin[0][1]
    if fruit[0][0]==x1:
        if fruit[0][1]==y1:
            coordin.insert(x_last,y_last)
    coordin.pop(0)
    return coordin

def put_coordinate(x2,y2,list_in):
    if x2>=0 & y2>=0:
        list_in[x2][y2]='x'
    return list_in
    
def fruit_put(x3,y3,list_all):
    if x3>=0 & y3>=0:
        if list_all[x3][y3]=='_':
            list_all[x3][y3]='O'
        
    return list_all


def map_draw(coordinates):
    list_map=[]
    for i in range(10):
        row = []
        for j in range(10):            
                row.append('_')    
        list_map.append(row)
    k=0
    list_new=[]
    for k in range(len(coordinates)):
        x=coordinates[k][0]
        y=coordinates[k][1]
        list_new=put_coordinate(x,y,list_map)
    return list_new

def build(list_look):    
    for item in list_look:
        print(" ".join(map(str, item)))
         
    
fruits=[(0,3),(1,4),(1,0),(3,4),(1,1),(5,5),(6,6)]
move_again=[(0,0),(0,1),(0,2)]
list_start=fruit_put(fruits[0][0],fruits[0][1],map_draw(move_again))
build(list_start)
ask=''
while ask!='end':
    ask=input('Direction? e=east, s=south, w=west, n=north, end=Stop Game')
    while True:
        if ask=='end':
            break
        if ask=='e' or ask=='s' or ask=='w' or ask=='n':
            break
        else:
            print('Your direction is wrong!!!Try again!')
            ask=input('Direction? e=east, s=south, w=west, n=north, end=Stop Game')
    
    if ask=='end':
                  break
    len1=len(move_again)
    f1=move_again[len1-1][0]
    h1=move_again[len1-1][1]
    g1=move_again[len1-2][0]
    v1=move_again[len1-2][1]
    move_ok=movement(move_again, ask, fruits)
    len2=len(move_ok)
    f2=move_ok[len2-1][0]
    h2=move_ok[len2-1][1]
    g2=move_ok[len2-2][0]
    v2=move_ok[len2-2][1]
    if f1==g2 and h1==v2 and g1==f2 and v1==h2:
        print("NO! You cant move back")
        break
        
    if move_ok!=[]:
        map_ok=map_draw(move_again)
        fruit_change=fruit_delete(move_ok, fruits)
        list_all=fruit_put(fruit_change[0][0],fruit_change[0][1],map_ok)
        build(list_all)
        fruits=fruit_change
        move_again=move_ok
    else:
        print('You are lost')
        break

