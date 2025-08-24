# codemetric

# Rule-Based Chatbot

## Project Overview
This project implements a **simple rule-based chatbot** in Python. The chatbot interacts with users through the command line and responds to **greetings, farewells, general knowledge questions, sports queries, historical facts, and basic math expressions**.  

It is designed as an educational project to demonstrate **basic Python programming, conditional statements, and input handling**.

---

## Features

1. **Greetings**
   - Responds to greetings like `hi`, `hello`, `hey`.

2. **Farewell Messages**
   - Exits the conversation when user types `bye`, `goodbye`, or `see you`.

3. **User Inquiry**
   - Introduces itself when asked: `what is your name`, `who are you`, `introduce yourself`.

4. **Assistance Queries**
   - Responds to queries about its capabilities like `what can you do`, `help`, `can you help me`.

5. **Sports Information**
   - Provides information on famous sportspersons across categories:
     - Cricket
     - Kabaddi
     - Football
     - Tennis
     - Badminton
     - Athletics
     - Boxing
     - Chess
   - Can answer specific sports queries, e.g., `famous cricketer`, `famous tennis player`.

6. **History & General Knowledge**
   - Answers basic historical and general knowledge questions:
     - `Who is Mahatma Gandhi?`
     - `First president of India`
     - `Who discovered India?`
     - `Capital of India`
     - `Largest planet`
     - `National animal of India`

7. **Math Solver**
   - Evaluates basic arithmetic expressions typed by the user using Python’s `eval()` function.  
     Example: Input `5 + 3 * 2` → Output `The answer is 11`.

---

## Code Structure

### 1. `chatbot()` Function
The main function runs an infinite loop to interact with the user until they exit.

- **Input Handling**: Accepts user input and converts it to lowercase.
- **Conditional Responses**: Uses `if-elif-else` statements to determine the appropriate response based on keywords.
- **Math Evaluation**: Tries to evaluate the user input as a mathematical expression.
- **Exit Condition**: Breaks the loop when the user types a farewell word.

### 2. Response Categories
- **Greetings**: `hi`, `hello`, `hey`
- **Assistance**: `help`, `what can you do`
- **Sports**: `sports`, `famous cricketer`, `famous football player`
- **History & GK**: `first president of India`, `capital of India`
- **Math**: Any arithmetic expression (addition, subtraction, multiplication, division)

---

## How to Run

1. Clone the repository:
```bash
git clone <repository_url>
