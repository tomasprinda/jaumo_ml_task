### Q) Your full name?
- Tomas Prinda

### Q) How long did you spend on the homework test?
- About 3 hours.

### Q) What would you add to your solution if you had more time? If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.
- I would test more models and done some hyperparameter tuning, but model had a 100% f1 measure so it was not neccessaty.
- For real task I would probably split the data to train/dev/test split so that I don't overfit to dev set during development. I would
print the results on test set before release to  estimate the performance in production.
-  I would use scaler in case of using other types of model, but random forrest doesn't require that.
- I would remove features with low importace to simplify the model.
- I would use error analysis if needed to improve performance and if the data was real. Manually go through
  incorrectly classified examples and categorised them according to type of an error.
  Then I would focus on creating features which would address problems in most promising error category (a lot of examples or simple to solve).

### Q) Which parts did you spend the most time with?
- 1 hour data download, thinking about the problem and writing results
- 1 hour data analysis
- 1 hour ML pipeline

### Q) How did you find the test overall? We’d love to hear your suggestions on how we can improve.
- I would appreciate working with real data. For example do some task that you have solved in the company before.
- I wasn't sure if I was supposed to make prototype/production code. I hope
you don't mind I made the solution in jupyter notebook. I like working with it for data analysis phase.
For production code I would probably use some tests, woudn't use pandas etc.
