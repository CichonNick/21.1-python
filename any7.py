def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE

    for any7 in nums:
        if any7 == 7:
            print("True")
        else:
            print("False")

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

