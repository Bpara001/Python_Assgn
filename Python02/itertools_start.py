# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
    if( x <= 40):
        return True
    return False

def print2(x):
    i=0
    while i != 2:
        print(next(x))
        i += 1

def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 =itertools.cycle(seq1)
    print(next(cycle1))
    # TODO: use count to create a simple counter
    count1 = itertools.count(100,10)
    print2(count1)

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals)
    print2(acc)
    acc =list(itertools.accumulate(vals, max))
    print (acc)
    # TODO: use chain to connect sequences together
    x = itertools.chain("ABCD","1234")
    print(list(x))
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction,vals)))
    print(list(itertools.takewhile(testFunction,vals)))
    
if __name__ == "__main__":
    main()
    