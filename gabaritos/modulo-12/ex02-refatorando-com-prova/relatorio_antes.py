"""Codigo de partida do Modulo 12, Exercicio 02. Este e o PROBLEMA."""
v = [["arroz",5,4.5],["feijao",3,8.9],["oleo",12,7.2],["sal",1,2.3],["cafe",8,18.5]]
t=0
c=0
m=0
n=""
for i in range(len(v)):
    s=v[i][1]*v[i][2]
    t=t+s
    if v[i][1]<5:
        c=c+1
    if s>m:
        m=s
        n=v[i][0]
print("=== RELATORIO ===")
for i in range(len(v)):
    s=v[i][1]*v[i][2]
    if v[i][1]<5:
        st="BAIXO"
    else:
        st="OK"
    print(v[i][0]+" "+str(v[i][1])+" "+str(v[i][2])+" "+str(s)+" "+st)
print("Total: "+str(t))
print("Itens baixos: "+str(c))
print("Maior: "+n+" "+str(m))
