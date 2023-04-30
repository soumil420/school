a=int(input())
a2000=a//2000
r2000=a%2000
a500=r2000//500
r500=r2000%500
a200=r500//200
r200=r500%200
a100=r200//100
r100=r200%100
a20=r100//20
r20=r100%20
a10=r20//10
r10=r20%10
a5=r10//5
r5=r10%5
a2=r5//2
r2=r5%2
a1=r2//1

if a%2000==0:
    print("you have",a2000, "2000 ruppee notes")
elif r2000%500==0:
    print("you have",a2000, "2000 ruppee notes",a500, "500 ruppee notes,")
elif r200%100==0:
    print("you have",a2000, "2000 ruppee notes",a500, "500 ruppee notes,", a100,"100 ruppee notes,")
elif r100%20==0:
    print("you have",a2000, "2000 ruppee notes",a500, "500 ruppee notes,",a200, "200 ruppee notes,", a100,"100 ruppee notes,",a20,"20 ruppee notes,")
elif r20%10==0:
    print("you have",a2000, "2000 ruppee notes",a500, "500 ruppee notes,",a200, "200 ruppee notes,", a100,"100 ruppee notes,",a20,"20 ruppee notes,", a10,"10 ruppee notes,")
elif r10%2==0:
    print("you have",a2000, "2000 ruppee notes",a500, "500 ruppee notes,",a200, "200 ruppee notes,", a100,"100 ruppee notes,",a20,"20 ruppee notes,", a10,"10 ruppee notes,", a2, "2 ruppee coins,")
else:
    print("you have",a2000, "2000 ruppee notes",a500, "500 ruppee notes,",a200, "200 ruppee notes,", a100,"100 ruppee notes,",a20,"20 ruppee notes,", a10,"10 ruppee notes,", a2, "2 ruppee coins,", a1,"1 ruppee coins" )





#if you input lets
"""print("you have",a2000, "2000 ruppee notes",a500, "500 ruppee notes,",a200, "200 ruppee notes,", a100,"100 ruppee notes,",a20,"20 ruppee notes,", a10,"10 ruppee notes,", a2, "2 ruppee coins,", a1,"1 ruppee coins" )"""

