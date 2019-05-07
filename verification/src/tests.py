"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [0],
            "answer": []
        },
        {
            "input": [1],
            "answer": [0]
        },
        {
            "input": [5],
            "answer": [0, 0, 0, 0, 0]
        }
    ],
    "Extra": [
        {
            "input": [2],
            "answer": [0, 0]
        }
    ]
}
