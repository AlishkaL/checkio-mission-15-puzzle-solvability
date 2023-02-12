"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]]],
            "answer": True,
            "explanation": "1 to 15"
        },
        {
            "input": [[[15, 14, 13, 12],
                       [11, 10, 9, 8],
                       [7, 6, 5, 4],
                       [3, 2, 1, 16]]],
            "answer": False,
            "explanation": "15 to 1"
        },
        {
            "input": [[[1, 5, 9, 13],
                       [2, 6, 10, 14],
                       [3, 7, 11, 15],
                       [4, 8, 12, 16]]],
            "answer": True,
            "explanation": "Vertical"
        },
        {
            "input": [[[1, 3, 2, 4],
                       [5, 7, 6, 8],
                       [9, 11, 10, 12],
                       [13, 15, 14, 16]]],
            "answer": True,
            "explanation": "Skip Odd to Even"
        },
        {
            "input": [[[1, 9, 2, 10],
                       [3, 11, 4, 12],
                       [5, 13, 6, 14],
                       [7, 15, 8, 16]]],
            "answer": True,
            "explanation": "Vertical Odd/Even"
        },
        {
            "input": [[[1, 4, 5, 8],
                       [2, 3, 6, 7],
                       [9, 10, 13, 14],
                       [16, 11, 12, 15]]],
            "answer": True,
            "explanation": "Skip Odd/Even"
        },
        {
            "input": [[[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 15, 14, 16]]],
            "answer": False,
            "explanation": "13-15-14"
        },
    ],
    "Extra": [
        {
            "input": [[[7, 5, 12, 9],
                       [15, 4, 2, 3],
                       [10, 11, 1, 8],
                       [16, 13, 6, 14]]],
            "answer": True,
        },
        {
            "input": [[[6, 12, 7, 4],
                       [10, 15, 8, 5],
                       [11, 3, 1, 13],
                       [9, 2, 14, 16]]],
            "answer": True,
        },
        {
            "input": [[[14, 15, 6, 4],
                       [9, 11, 8, 7],
                       [1, 5, 16, 10],
                       [2, 3, 12, 13]]],
            "answer": False,
        },
        {
            "input": [[[15, 10, 7, 4],
                       [11, 3, 1, 16],
                       [13, 12, 9, 6],
                       [8, 14, 2, 5]]],
            "answer": True,
        },
        {
            "input": [[[1, 15, 11, 7],
                       [14, 6, 5, 8],
                       [4, 10, 3, 13],
                       [16, 12, 9, 2]]],
            "answer": False,
        },
    ]
}
