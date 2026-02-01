from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#using logistic regression model to train(yes/no, 0/1) and accuracy score to check how many predictions are correct

def train_model(X_train, X_test, y_train, y_test):
    model = LogisticRegression(max_iter=5000) #5000 iterations to ensure convergence- gives enuf time to learn
    model.fit(X_train, y_train) # this is the training part- i/p x, o/p y

    predictions = model.predict(X_test) #making predictions on test data
    accuracy = accuracy_score(y_test, predictions) #comparing predicted vs actual values to get accuracy

    return model, accuracy
