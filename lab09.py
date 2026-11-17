# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # my plan is to loop over the list twice the first time by putting the first num in a variable and 
    # second loop is basically one after the first one and check if they add up t target while i still being less than j 

    #   ...
    result = []
    for i in range(len(nums) - 1 ):
        for j in range(i + 1, len(nums) ):
            if nums[i] + nums[j]  == target and i < j:
                return [i,j]
     


def max_profit(prices):
    profit = 0
    for i in range(len(prices) -1 ):
       for j in range(i + 1, len(prices)):
           if prices[j] - prices[i] > profit:
               profit = prices[j] - prices[i]
    return profit



def max_subarray(nums):
    max_sum = nums[0]

    for i in range(len(nums)):
        current_sum = 0

        for j in range(i, len(nums)):
            current_sum += nums[j]

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
