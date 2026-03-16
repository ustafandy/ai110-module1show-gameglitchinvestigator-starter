# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- "There were no hints when I run the game first time." 
- "The range in the easy mode says from 1 to 20 while the secret number was 93"

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

- I used Claude inside VSCode, and Chat GPT on my browser. Chat GPT is my all time favorite AI

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 

- The AI suggested that I change variables to fix the out of range problems and I confirmed the edits. Then after rerunnning the game. The range problem was fixed and that's how I confirmed it was true suggestion. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- The suggested solution for the hint problem was not correct. The test case Claude wrote for me to add in the `test_game_logic.py` file was giving errors and Chat GPT fixed it for me. Furthermore, the fix I implemented using Claude still gives a misleading information in the game. It only fixed part of the problem. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

- By rerunning the game and trying that specific problem. 

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

- The 'Easy' range test. I changed it midplaying to make sure the secret number will be in range from 1 to 20 and it worked.

- Did AI help you design or understand any tests? How?

- Yes it helped me design the fix for the test easy range. It explicitly showed me that the problem was in the variables because the original code reset the range 1 to 100 with every new game.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script every time the user interacts with the app. This means the program starts executing from the top again on each interaction.

Session state is used to store information. For example, in the guessing game the secret number and previous hints must stay the same even when the page reruns. Without session state, those values would reset every time the user interacts with the app.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I want to reuse is using automated tests with pytest to verify code changes. Writing tests helped confirm that my fixes actually worked instead of relying only on manual testing.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time I work with AI on a coding task, I will verify the suggestions more carefully instead of assuming they are correct. In this project I learned that AI suggestions can be helpful but sometimes incomplete or incorrect, so reviewing the logic and testing the results is important.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI can be a useful assistant for debugging and explaining code, but it should not be trusted blindly. Developers still need to understand the code, test it, and verify that the suggested fixes actually solve the problem.