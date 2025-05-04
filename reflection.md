# Reflection

Student Name:  Gabrielle Russo
Student Email:  grusso01@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

This project was definitely the most rewarding thing we've done in IST356 because it pulled everything together, from reading and cleaning raw data to building a full interactive dashboard using Streamlit. I learned how each step in a data pipeline builds on the last, and I was able to actually see the results of my code visually, which made the work feel much more impactful than the assignments we did throughout the semester.

One of the biggest things I used from what we learned this semester was how to break up a larger project into separate parts, like `extract.py`, `transform.py`, and `analyze.py`. 

There were also a lot of issues that I ran into, especially with data cleaning. For example, the columns in my CSV file had different names than what I was expecting, like `REFUSETONSCOLLECTED` instead of `REFUSE_TONS_COLLECTED`, so I had to use `.rename()` to fix that and match what I needed for transformation. I also had trouble with division-by-zero errors when calculating the capture rate, which I solved by filtering out rows where the total waste was 0.

Another confusing part was the file paths and module imports. I kept getting `ModuleNotFoundError: No module named 'code.transform'` because I didn’t fully understand how Python’s module search path works. I eventually learned, with the help of ChatGPT, that I needed to add `sys.path.append(os.path.abspath('code'))` at the top of my test files in order to import my functions the way I had them organized in folders. That was one of the most frustrating issues because the code was technically fine, but Python just couldn’t find the file, so I thank ChatGPT for helping me navigate this issue.

I also struggled with writing tests. I originally tried to use `pytest`, but it wouldn’t recognize any of my test functions, even though everything was named correctly. After trying several debugging steps, including renaming files, adding print statements, and rewriting test logic, I eventually gave up and pasted what I had into ChatGPT so it could help me figure out all of the issues I was facing and make sure that the test was running, especially since I knew my code was working but I couldn't figure out the test.

Lastly, working with Streamlit was a really cool part of the project. I had never used Streamlit before this course, and I was surprised how easy it was to build something that looks professional and interactive. I liked being able to filter by borough and watch the line chart update in real time. It made the project feel like something someone could actually use.

If I had more time, I would improve the dashboard by adding comparisons between multiple boroughs at once, or even a map showing which boroughs are performing better. I did a very similar project for IST256 where I made a map showing which boroughs had the best capture rates compared to the other boroughs by showing that borough green, but I'm not really sure how to do that on streamlit, so I didn't recreate it. Overall, this project made me feel more confident about handling real-world data problems and gave me a better understanding of how to organize code for analysis and presentation.