from specification import Pile

def test_PileLIFO_base():
    test_Pile = Pile()

    assert test_Pile.is_void() == True #just init, no data inside #data[(None)]

    test_Pile.append(55) #data[55]
    assert test_Pile.is_void == False

    test_Pile.append(77) #data[77, 55]
    assert test_Pile.get() == 77 #data[55]
    assert test_Pile.get() == 55 #data[]
    

def test_PileLIFO_catch():
    test_Pile = Pile()

    assert test_Pile.get() == None #.get() with None data in Pile/LIFO data[]

