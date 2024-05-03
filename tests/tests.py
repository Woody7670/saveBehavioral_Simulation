from main.bacteria import Bacteria
import main.bacteria

testAgent = Bacteria([10, 10], [20, 20], [20, 20], 5)
testCoordinates = [20, 20]


def testVision():
    assert main.base_agent.calcDistance(testCoordinates) == 14


def testMove():
    testAgent.move(testCoordinates)
    assert testAgent.coordinates == testCoordinates


def testDistance():
    distance, a, closeTargets = testAgent.vision(testCoordinates)
    assert distance == [14]
    assert a == [20, 20]
    assert closeTargets == [20, 20]


def testGoFood():
    testAgent.goFood()
    assert testAgent.coordinates == [20, 20]


def testGoWater():
    testAgent.goDrink()
    assert testAgent.coordinates == [20, 20]

