# CECS 326 PROJECT 5 : PAGE REPLACEMENT

def print_Statement(numberOrder, page, holder, boolState):
    if numberOrder > 9:
        print(
            f"{numberOrder}   | {page}    | [{', '.join(str(slot) if slot != '-' else '-' for slot in holder)}]       | {boolState}")
    else:
        print(
            f"{numberOrder}    | {page}    | [{', '.join(str(slot) if slot != '-' else '-' for slot in holder)}]       | {boolState}")


def Testcase():
    # holder1 = ['-', '-']
    # holder2 = ['-', '-', '-']
    # holder3 = ['-', '-', '-', '-']

    print("FIFO Test case \n")

    print("TEST 1: Page frame 2")
    FIFO(1, ['-', '-'], 0, myList, 0)  # Test with 2 page frames
    print("\n")

    print("TEST 2: Page frame 3")
    FIFO(1, ['-', '-', '-'], 0, myList, 0)  # Test with 3 page frames
    print("\n")

    print("TEST 3: Page frame 4")
    FIFO(1, ['-', '-', '-', '-'], 0, myList, 0)  # Test with 4 page frames
    print("\n")

    # LRU TEST CASE

    print("LRU Test case \n")

    print("TEST 1: Page frame 2")
    LRU(1, ['-', '-'], myList, 0)  # Test with 2 page frames
    print("\n")

    print("TEST 2 : Page frame 3")
    LRU(1, ['-', '-', '-'], myList, 0)  # Test with 3 page frames
    print("\n")

    print("TEST 3 : Page frame 4")
    LRU(1, ['-', '-', '-', '-'], myList, 0)  # Test with 4 page frames
    print("\n")


def FIFO(numberOrder, holder, holderIndex, myList, pageFault):
    print("Step | Page | Memory State | Page Fault?")
    print("-------------------------------------------")
    for i in myList:
        page = i
        if i not in holder:
            holder[holderIndex] = i  # Replace the oldest page
            holderIndex += 1
            # Change the index based on the page frames
            if holderIndex >= len(holder):
                # Reset the index
                holderIndex = 0
            pageFault += 1
            boolState = "Yes"

            # print(numberOrder, " my holder: ", holder, "Yes")
        else:
            boolState = "No"
            # print(numberOrder, " my holder: ", holder, "No")

        print_Statement(numberOrder, page, holder, boolState)
        numberOrder += 1
    print(f"Total Page Faults: {pageFault}")


def LRU(numberOrder, displayList, myList, pageFault):
    holder = []  # Tracks the order of pages for LRU replacement
    print("Step | Page | Memory State | Page Fault?")
    print("-------------------------------------------")
    for page in myList:
        if page not in holder:
            # Page fault occurs
            if len(holder) == len(displayList):
                # Remove the least recently used page
                lru_page = holder.pop(0)  # Remove the oldest page in `holder`
                lru_index = displayList.index(lru_page)  # Find and replace it in `displayList`
                displayList[lru_index] = page
            else:
                # Place the new page in the first empty slot
                empty_index = displayList.index('-')  # Find the first available slot
                displayList[empty_index] = page
            holder.append(page)  # Add the new page to the `holder`
            pageFault += 1
            boolState = "Yes"
        else:
            # Page is already in memory; update its usage
            holder.remove(page)  # Remove it from `holder`
            holder.append(page)  # Re-add it to mark it as most recently used
            boolState = "No"

        # Print the memory state and page fault status
        print_Statement(numberOrder, page, displayList, boolState)
        numberOrder += 1

    print(f"Total Page Faults: {pageFault}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("IT START HERE \n")
    myList = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]  # Input: Page Request Sequence
    holderIndex = 0
    orderNum = 0
    Testcase()
    print("IT END HERE")
