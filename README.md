# Jaumo ML task

I created the solution in [jupter notebook](jaumo_ml_task.ipynb) because I think it was appropriate for this kind of task.

Solution is split into four parts - data analysis, preparing data, training model and evaluation.

## Data analysis
I usually do this phase to get some information about data, which allows me to do better feature engineering, clean data and
find some possible problems in the data.

It was found out that all feature columns were generate from uniform distribution. Feature columns were independet to each other.

## Preparing data
Converts the input matrix to train/dev datasets - ids, features and labels for each dataset.

## Training model
I just picked of the shelf classifier - random forest. It wasn't neccessary to change model due to very good results.

## Evaluation
I used `f1` measure because it is better than accuracy in general for imbalanced datasets.
I plotted confusion matrix as requested.
