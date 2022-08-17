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
            "input": ['''one simple line
'''],
            "answer": 1
        },
        {
            "input": [''],
            "answer": 0,
            "explanation": "5+7=?"
        },
        {
            "input": ['''
only one line
            '''],
            "answer": 1
        },

        {
            "input": ['''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            '''],
            "answer": 3,
        },
    ],
    "Extra": [

        {
            "input": ['''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
Nullam ante ligula,
          
          fermentum a porta
            '''],
            "answer": 5,
        },

        {
            "input": ['''
Do you want,

a story
about lazy boy?
            '''],
            "answer": 3,
        },
    ]
}
