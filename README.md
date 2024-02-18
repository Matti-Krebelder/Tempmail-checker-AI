
# Tempmail-checker-AI

This AI is capable of identifying temporary email addresses, distinguishing between temporary and valid ones. It's easily trainable using your own data, and it's implemented in Python.


![Logo](https://skynethub.net/Tempmail-checker-AI.png)


## Getting Started 🚀
If you haven't installed git, you can install it with:
   ```bash
   winget install --id Git.Git -e --source winget
   ```

If you have git, you can simply start this:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Matti-Krebelder/Tempmail-checker-AI.git
   ```

2. **Move to folder:**
   ```bash
   cd Tempmail-checker-AI
   ```
3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```
    
## 🌐Documentation


To use the application, follow these steps:

### Starting the Program: 

Run the script. The console will prompt you to choose an option: (E) to check an email, (T) to start training, (S) to save data, or (B) to exit the program.

### Checking an Email (E):

   Type "e", followed by the email you want to check. The program will analyze the email and display the classification result.

### Starting Training (T):

   Choose "t" to initiate the training process. Enter the email to be trained and its corresponding label ("valid" or "temp"). The model will be updated with the new data.

### Saving Data (S):

   Press "s" to save the training data to the CSV file.

### Exiting the Program (B):

   Input "b" to exit the program.

## Support 📧

   For any questions or assistance, please contact Matti Krebelder at [info@skynethub.net](mailto:info@skynethub.net).

## Authors

- [@Matti-Krebelder](https://github.com/Matti-Krebelder/)
