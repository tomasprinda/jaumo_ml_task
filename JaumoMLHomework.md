# Machine Learning Engineer Homework Test

Thank you for taking the time to do our technical test.

## Requirements
Feel free to spend as much or as little time as you like, as long as the 
following have been met:
- You completed the task and answered the questions (see below).
- Your code is simple to execute.
- Your code includes appropriate comments for the readers.
- You provide a `README.md` to briefly explain your code and decisions, 
e.g., why you have chosen such a model, etc.

## Task
Download the
[`data.csv`](https://www.dropbox.com/s/3kuy00wr9efjpso/data.csv?dl=1) file 
which contains data in the format:
    
    id,label,f1,f2,f3,c1
    100001,1,0.03,1.4,0.6,n
    100002,-1,0.47,-2.5,0.1,m
    100003,1,0.19,3.3,-0.2,f
    ...

The first row is the column headers.
The actual data can be different, but the columns must be:

- `id` -- integer, the sample identity number.
- `label` -- integer, either `-1` or `1`, the sample label.
- `f1` -- float, a sample feature.
- `f2` -- float, a sample feature.
- `f3` -- float, a sample feature.
- `c1` -- string, either `m`, `f`, or `n`, a sample feature.

You can assume there is no missing entry.

Your assignment is to write some code, preferably in Python, that accomplishes the following:

1. Read the data given in `data.csv`.
2. Train a model with the data, so that the model can be used to classify 
   samples into different labels (`-1` or `1`) given the above features. 
   (Do not struggle to get a "perfect" model accuracy, what we are focusing on 
    is your code logic and software engineering.)
3. Verify the model accuracy with a test split of the data. Also print a confusion matrix.

Don't feel limited to perform only the above mentioned. You may include anything
that you find necessary, but keep it as simple as possible.

## Questions
Please answer the following questions in a markdown file called 
[`Answers.md`](https://www.dropbox.com/s/0z6kqctlsfisk5e/Answers.md?dl=1):
- How long did you spend on the homework test?
- What would you add to your solution if you had more time? If you did not 
spend much time on the assignment, then use this as an opportunity to explain 
what you would add.
- Which parts did you spend the most time with?
- How did you find the test overall? We would love to hear your suggestions on 
how we can improve.

## Submission
Please make this a ZIP file named: `<firstname>_<lastname>.zip` containing:
- The code for solving the task.
- The `README.md` explaining the code and your decisions.
- The completed `Answers.md`.

Upload the file to a shared folder and send the link to your Jaumo contact.

**Thanks for your time, we look forward to hearing from you!**

The Jaumo Machine Learning Guild
