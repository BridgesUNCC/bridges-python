# First import the relevant Bridges classes
from bridges.bridges import *
from bridges.array import *
from bridges.symbol_collection import *
from bridges.rectangle import *

bridges = Bridges(1, "test", "137842425086")
sc = SymbolCollection()

disk1 = Rectangle(20, 10, -50, 10)
disk2 = Rectangle(30, 10, -50, 0)
disk3 = Rectangle(40, 10, -50, -10)

src = []
dest = []
aux = []

def makePegs(size):
    src_peg = Rectangle(10, 30, -50, 0)
    sc.add_symbol(src_peg)
    dest_peg = Rectangle(10, 30, 0, 0)
    sc.add_symbol(dest_peg)
    aux_peg = Rectangle(10, 30, 50, 0)
    sc.add_symbol(aux_peg)

def makeDisks(size):
    sc.add_symbol(disk1)
    sc.add_symbol(disk2)
    sc.add_symbol(disk3)

def isEmpty(peg):
    return len(peg) == 0

def push(peg, item):
    peg.append(item)

def pop(peg):
    if(isEmpty(peg)):
        return None
    return peg.pop()

def moveDisk(fromP, toP, disk):
    print("Move the disk", disk, " from ", fromP, " to ", toP)

def displayCurrent(src, aux, dest):
    #  very very inefficient but that's ok for now.

    s = src
    a = aux
    d = dest

    sS = ""
    # if len(s) == 0:
    #     sS = Array(num_elements=1)
    #     sS.get_element(0).set_label("Source is EMPTY")
    #     sS.get_element(0).get_visualizer().set_color('black')
    # else:
    #     sS = Array(num_elements=len(s))
    for i in range(len(s)):
        if s[i] == 1:
            disk1.set_location(-50, 10)
        elif s[i] == 2:
            disk2.set_location(-50, 0)
        elif s[i] == 3:
            disk3.set_location(-50, -10)

    # bridges.set_data_structure(sc)
    # bridges.setTitle("Source")
    # bridges.visualize()


    sA = ""
    # if len(a) == 0:
    #     sA = Array(num_elements=1)
    #     sA.get_element(0).set_label("Aux is EMPTY")
    #     sA.get_element(0).get_visualizer().set_color('black')
    # else:
    #     sA = Array(num_elements=len(a))
    for x in range(len(a)):
        if a[x] == 1:
            disk1.set_location(0, 10)
        elif a[x] == 2:
            disk2.set_location(0, 0)
        elif a[x] == 3:
            disk3.set_location(0, -10)
    # bridges.set_data_structure(sc)
   #  bridges.setTitle("Aux")
   #  bridges.visualize()


    # sD = ""
    # if len(d) == 0:
    #     sD = Array(num_elements=1)
    #     sD.get_element(0).set_label("Dest is EMPTY")
    #     sD.get_element(0).get_visualizer().set_color('black')
    # else:
    #     sD = Array(num_elements=len(d))
    for y in range(len(d)):
        if d[y] == 1:
            disk1.set_location(50, 10)
        elif d[y] == 2:
            disk2.set_location(50, 0)
        elif d[y] == 3:
            disk3.set_location(50, -10)

    print(src)
    bridges.set_data_structure(sc)
    # bridges.setTitle("Dest")
    bridges.visualize()



def moveBetweenPoles(src, dest, s, d):
    pole1TopDisk = pop(src)
    pole2TopDisk = pop(dest)

    if pole1TopDisk == None:
        push(src,pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
    elif pole2TopDisk == None:
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)
    elif pole1TopDisk > pole2TopDisk:
        push(src, pole1TopDisk)
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)
    else:
        push(dest, pole2TopDisk)
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)



def toh_inter(numDisks, src, aux, dest):
    i = 0
    numMoves = 0
    s = 'S'
    d = 'D'
    a = 'A'

    if numDisks % 2 == 0:
        temp = d
        d = a
        a = temp

    numMoves = pow(2,numDisks) - 1

    for x in range(numDisks, 0, -1):
        push(src, x)

    displayCurrent(src, aux, dest)

    for i in range(1, numMoves+1):
        if i%3 == 1:
            moveBetweenPoles(src, dest, s, d)
        elif i % 3 == 2:
            moveBetweenPoles(src, aux, s, a)
        elif i%3 == 0:
            moveBetweenPoles(aux, dest, a, d)

        displayCurrent(src, aux, dest)


def main():

    numbDisks = 3

    makePegs(numbDisks)
    makeDisks(numbDisks)

    toh_inter(numbDisks, src, aux, dest)


if __name__ == '__main__':
    main()

