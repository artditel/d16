def qwert(my_moves, enemy_moves):
    m=my_moves
    e=enemy_moves
    rep=5
    for i in range(0,len(m)):
        if m[i] and not e[i]:
            rep-=5
        if e[i] and not m[i]:
            rep+=5
        if e[i] and m[i]:
            rep+=3
    if rep>0:
        return True
    else:
        return False
