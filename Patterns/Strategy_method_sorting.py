"""
Strategy is a behavioral design pattern that lets you define a family of algorithms,
put each of them into a separate class, and make their objects interchangeable.

https://stackabuse.com/sorting-algorithms-in-python/



"""

from abc import ABCMeta, abstractmethod
class SortStrategy(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, nums):
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, nums):
        # We set swapped to True so the loop looks runs at least once
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    # Swap the elements
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # Set the flag to True so we'll loop again
                    swapped = True

class SelectionSortStrategy(SortStrategy):
    def sort(self, nums):
        # This value of i corresponds to how many values were sorted
        for i in range(len(nums)):
            # We assume that the first item of the unsorted segment is the smallest
            lowest_value_index = i
            # This loop iterates over the unsorted items
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            # Swap values of the lowest unsorted element with the first unsorted
            # element
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

class InsertionSortStrategy(SortStrategy):
    def sort(self, nums):
        # Start on the second element as we assume the first element is sorted
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            # And keep a reference of the index of the previous element
            j = i - 1
            # Move all items of the sorted segment forward if they are larger than
            # the item to insert
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            # Insert the item
            nums[j + 1] = item_to_insert


class HeapSortStrategy(SortStrategy):

    def sort(self, nums):
        def heapify(nums, heap_size, root_index):
            # Assume the index of the largest element is the root index
            largest = root_index
            left_child = (2 * root_index) + 1
            right_child = (2 * root_index) + 2

            # If the left child of the root is a valid index, and the element is greater
            # than the current largest element, then update the largest element
            if left_child < heap_size and nums[left_child] > nums[largest]:
                largest = left_child

            # Do the same for the right child of the root
            if right_child < heap_size and nums[right_child] > nums[largest]:
                largest = right_child

            # If the largest element is no longer the root element, swap them
            if largest != root_index:
                nums[root_index], nums[largest] = nums[largest], nums[root_index]
                # Heapify the new root element to ensure it's the largest
                heapify(nums, heap_size, largest)

        n = len(nums)

        # Create a Max Heap from the list
        # The 2nd argument of range means we stop at the element before -1 i.e.
        # the first element of the list.
        # The 3rd argument of range means we iterate backwards, reducing the count
        # of i by 1
        for i in range(n, -1, -1):
            heapify(nums, n, i)

        # Move the root of the max heap to the end of
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)

class ListSortingOperations:
    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_sorting_inplace(self, nums):
        print("Before Sorting {}".format(nums))
        print("Applying: {}".format(self.strategy.__class__.__name__))
        self.strategy.sort(nums)
        print("After Sorting {}".format(nums))
        print("#"*50)

if __name__ == '__main__':
    bss = BubbleSortStrategy()
    sss = SelectionSortStrategy()
    iss = InsertionSortStrategy()
    hss = HeapSortStrategy()
    list_operations = ListSortingOperations()

    list_operations.set_strategy(bss)
    list_operations.do_sorting_inplace([8,3,9,2,6,5])

    list_operations.set_strategy(sss)
    list_operations.do_sorting_inplace([8, 3, 9, 2, 6, 5])

    list_operations.set_strategy(iss)
    list_operations.do_sorting_inplace([8, 3, 9, 2, 6, 5])

    list_operations.set_strategy(hss)
    list_operations.do_sorting_inplace([8, 3, 9, 2, 6, 5])

## OUTPUT
Before Sorting [8, 3, 9, 2, 6, 5]
Applying: BubbleSortStrategy
After Sorting [2, 3, 5, 6, 8, 9]
##################################################
Before Sorting [8, 3, 9, 2, 6, 5]
Applying: SelectionSortStrategy
After Sorting [2, 3, 5, 6, 8, 9]
##################################################
Before Sorting [8, 3, 9, 2, 6, 5]
Applying: InsertionSortStrategy
After Sorting [2, 3, 5, 6, 8, 9]
##################################################
Before Sorting [8, 3, 9, 2, 6, 5]
Applying: HeapSortStrategy
After Sorting [2, 3, 5, 6, 8, 9]
##################################################
