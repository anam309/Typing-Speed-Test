# Typing Speed Test

## Objective
The primary goal of this project is to help users improve their typing speed and accuracy. Users can practice typing either random letters or sentences and receive feedback on their performance, including typing speed (words per minute), accuracy, and total time taken.

## Overview
The application provides two practice options:
1. **Random Letters** - Users type randomly generated letters to focus on individual keystrokes.
2. **Random Sentences** - Users type randomly generated sentences to improve fluency and accuracy.

After the user submits their input, the program calculates and displays:
- **Total Words** typed
- **Time Taken** to complete the input
- **Typing Speed** (in words per minute)
- **Accuracy** (percentage of correct entries)

## Software and Libraries

- **Development Environment**: Python IDLE
- **Libraries Used**:
  - **Tkinter**: For creating the graphical user interface.
  - **Time**: To calculate the time taken by the user.
  - **Random**: To generate random letters and sentences.
  - **Difflib**: To assess typing accuracy by comparing user input to the provided text.

## Interface

The Typing Speed Test application is implemented with a **Command Line Interface (CLI)** using Python Shell but displays a graphical user interface using `Tkinter`. The GUI contains various interactive elements, including:
- **Labels**: Displaying instructions and results.
- **Buttons**: For submitting input.
- **Checkboxes**: To select between "Random Letters" or "Random Sentences" modes.

### Key Functions

1. **`PrintValue`**  
   - This function calculates and displays the typing metrics (time, speed, words, and accuracy) when the user submits their input.

2. **`Check_box`**  
   - This function manages the selection of either "Random Letters" or "Random Sentences" modes.
   - Depending on the user's choice, it generates either random letters or a random sentence for typing practice.
   - The function also enables the "Submit" button. When the user clicks "Submit," it triggers the `PrintValue` function to calculate and display results.

The main application loop then runs continuously until the user exits.
