import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier


file_path = "email_data.csv"
if not os.path.exists(file_path):

    data = pd.DataFrame(columns=["email", "label"])

    data.to_csv(file_path, index=False)
else:

    data = pd.read_csv(file_path)


if not data.empty:

    model = RandomForestClassifier()

    X_train = data["email"].apply(lambda x: len(x))
    X_train = X_train.values.reshape(-1, 1)
    y_train = data["label"]
    model.fit(X_train, y_train)
else:
    model = RandomForestClassifier()


def predict_email(email):
    if not data.empty:

        email_length = len(email)

        prediction = model.predict([[email_length]])
        return prediction[0]
    else:
        return "No model trained yet"


while True:
    option = input("Want to check an email? Press (e). To start training, press (t). To save training data, press (s). To stop the program, press (b) ")
    if option.lower() == "b":
        break
    elif option.lower() == "e":
        email = input("Enter Email: ")
        prediction = predict_email(email)
        print("Die E-Mail '{}' ist '{}'.".format(email, prediction))
    elif option.lower() == "t":
        email = input("Enter Trainings Email: ")
        label = input("Is the Mail 'valid' or 'temp'?: ")
        #
        new_data = pd.DataFrame([[email, label]], columns=["email", "label"])
        data = pd.concat([data, new_data], ignore_index=True)

        X_train = data["email"].apply(lambda x: len(x))
        X_train = X_train.values.reshape(-1, 1)
        y_train = data["label"]
        model.fit(X_train, y_train)
    elif option.lower() == "s":
        data.to_csv(file_path, index=False)
        print("Data Saved.")
    else:
        print("Invalid option")


data.to_csv(file_path, index=False)
