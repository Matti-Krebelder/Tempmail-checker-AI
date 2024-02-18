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
    option = input("Want to check an email? Press (E). To start training, press (T). To save training data, press (S). To stop the program, press (B): ")
    if option.lower() == "b":
        break
    elif option.lower() == "e":
        email = input("Please Enter Email to check: ")
        prediction = predict_email(email)
        print("The E-Mail '{}' is '{}'.".format(email, prediction))
    elif option.lower() == "t":
        email = input("Enter Trainings E-Mail: ")
        label = input("Is the E-Mail 'valid' or 'temp'?: ")
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
