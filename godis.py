#start
# vald vilken man har
print "1 Chocklad 10kr"

print "2 Festis 8kr"
print "Valj vilket number"

nr=int(raw_input("Vald number "))
print "Hur mycket pengar har du"
pengar=int(raw_input())
# om nr ar de som man har valt
if nr == 1:
    if pengar >= 10:
        print "Tack,Tack"
    else:
        print "Tyvarr for lite pengar"
elif nr == 2:
    if pengar >= 8:
        print "Tack,Tack"
    else:
        print "Tyvarr for lite pengar"
else:
    print "Tyvarr fel number vald"
 #    print "racker pengarna"
 #    elif pengar >= 10:
 #    print "tack"
 # else:
 # print "tyvarr"
