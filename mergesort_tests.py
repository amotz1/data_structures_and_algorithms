from mergesort import sort

# [amotz] the only thing that is not completed i think is that it seems i get some weird assertion error.
# without the assertion the test function seems to run smoothly without errors
# and give correct answer for all the test cases, but somehow if i run the program with the assertion
# it stops the program when it hit the [] testcase and then it throws off an assertion error...


def test():
    testCases = [[3, 5, 11, 3, 13],
                 [7, 8, 7, 9, 5, 2],
                 [6, 8, 8, 5, 4, 3],
                 [6, 8, 9, 9, 4, 3],
                 [8, 6, 6, 6, 9, 3, 2, 1, 2],
                 [1, 2, 3],
                 [3, 2, 1],
                 [],
                 [1],
                 [1, 1, 1]]

    for testCase in testCases:
        print("in\t", testCase)
        sort(testCase)
        print("out\t", sort(testCase))
        assert(sort(testCase) == sorted(testCase))


test()