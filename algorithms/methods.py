import time


def time_of_function(func):
    def wrapped(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(f'[*] Runtime: {end-start}.')
    return wrapped


class Method:
    def __init__(self):
        self.before = []
        self.result = []


class Bubble(Method):
    @time_of_function
    def sort(self, nums):
        self.before = nums
        swap = True
        while swap:
            swap = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swap = True
        self.result = nums


class Insertion(Method):
    @time_of_function
    def sort(self, nums):
        self.before = nums
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert
        self.result = nums


class Merge(Method):
    @time_of_function
    def sort(self, nums):
        def merge(left_list, right_list):
            sorted_list = []
            left_list_index = right_list_index = 0

            left_list_length, right_list_length = len(left_list), len(right_list)

            for i in range(left_list_length + right_list_length):
                if left_list_index < left_list_length and right_list_index < right_list_length:
                    if left_list[left_list_index] <= right_list[right_list_index]:
                        sorted_list.append(left_list[left_list_index])
                        left_list_index += 1
                    else:
                        sorted_list.append(right_list[right_list_index])
                        right_list_index += 1
                elif left_list_index == left_list_length:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1
                elif right_list_index == right_list_length:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
            return sorted_list

        def merge_sort(temp):
            if len(temp) <= 1:
                return temp
            mid = len(temp) // 2
            left_list = merge_sort(temp[:mid])
            right_list = merge_sort(temp[mid:])
            return merge(left_list, right_list)

        self.before = nums
        self.result = merge_sort(nums)[:]


class Quick_sort(Method):
    @staticmethod
    def partition(nums, low, high):
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1
            j -= 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]

    @time_of_function
    def sort(self, nums):
        self.before = nums

        def _sort(items, low, high):
            if low < high:
                split_index = Quick_sort.partition(items, low, high)
                _sort(items, low, split_index)
                _sort(items, split_index + 1, high)
        _sort(nums, 0, len(nums) - 1)
        self.result = nums
