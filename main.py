"""
Write a Python program to build a Stair Climb and Brace Builder using recursion.
You will solve the stair climb problem, trace how recursive calls branch like
a call tree, and generate valid balanced brace combinations.
"""

def waysToClimb(n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    return waysToClimb(n - 1) + waysToClimb(n - 2)


stairs = int(input("Number of Stairs: "))
print(f"Total ways to climb: {waysToClimb(stairs)}")
print()


print("Call Tree")

def traceWaysToClimb(n, space=""):
    print(f"{space}traceWaysToClimb({n})")

    if n == 0:
        print(f"{space}Reached 0 stairs -> 1")
        return 1

    if n < 0:
        print(f"{space}Went below 0 stairs -> 0")
        return 0

    oneStep = traceWaysToClimb(n - 1, space + "  ")
    twoSteps = traceWaysToClimb(n - 2, space + "  ")

    total = oneStep + twoSteps
    print(f"{space}Total ways for {n} stairs: {total}")

    return total


traceWaysToClimb(stairs)
print()


print("Balanced Parentheses")

def generateBraces(n, openCount=0, closeCount=0, current=""):
    if len(current) == 2 * n:
        print(current)
        return

    if openCount < n:
        generateBraces(n, openCount + 1, closeCount, current + "(")

    if closeCount < openCount:
        generateBraces(n, openCount, closeCount + 1, current + ")")


pairs = int(input("Number of Brace Pairs: "))
generateBraces(pairs)