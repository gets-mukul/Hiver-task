# Hiver-task
Question Paper Generator

## Getting Started
To get entire project into local machine write below command in terminal.

`$ git clone https://github.com/gets-mukul/Hiver-task.git`


You need to have venv folder inside  Hiver-task folder.

## Prerequisites
python version : 2.7+

## Running the tests
1. Open the terminal/cmd.
2. Got to the directory containing all .py files.
3. Runninng command given below will give the result for all the test-cases.

`$ python3 Main.py `

### Adding new test-case
1. Open the test_case.txt file.
2. Enter new test-case in the same format given below as JSON.

`{"total": total_marks, "difficulty_level": difficulty_marks_in_percentage, "difficulty_level": difficulty_marks_in_percentage, "difficulty_level": difficulty_marks_in_percentage}`

`Example : {"total": 100, "easy": 20, "medium": 30, "hard": 50}`


**make sure not to enter % sign in above json format**

### Adding new Questions
1. Open question.txt file.
2. Enter new question in the same format given below.

`qustion_id, difficulty_level, marks`

`Example : Q1, easy, 8`



