# AI Usage Documentation
## Tools Used
- ChatGPT (GPT-4) for Flask routes and CRUD python Creation for First Table (companies),
for style.css, improving my edit/update forms, creating job match logic, and debugging.
## Key Prompts
1. "Create CRUD TABLE Functions using python for companies."
2. "Write Flask routes for my Crud Tables functions for companies and the function for the flask."
3. "Write a style.css file to make the pages look nice and organize for my tables and forms."
4. "How to edit/update forms from an identifier ,and it will load the pre-existing info only using HTML and python using my flask
routes and functions, not making a new one"
5. "How to read json to compare job requirements with user enter skills and display what jobs are best fitted for user
by comparing the two numbers and displaying the percentage to see what best fits in descending order"
6. Debug this error......("Enter error")

## What Worked Well
- AI-generated the CRUD Table for companies in python as functions and used it as a foundation for the other CRUDS
- AI-generated the basic CRUD routes for companies quickly and use it as a foundation for the other CRUDS
and the function for the flask
- The AI-generated style.css file made the UI look way better.
- Improving my edit/update forms
- Creating the logic for job match
- Debugging errors made the process faster

## What I Modified
- Changed variable names to match my schema
- When creating flash routes, change them to match my HTML pages and change variables to imported database variables to
remove redundant programming.
- I modified the style.css file to remove elements that were not needed and changed the colors
- Modified my update/edit forms to match my workflow, variables, and python functions
- Modified the code for job search by change variable names and moving it the database.py and calling the functions in app.py
## Lessons Learned
- Always test AI code it never works great at first.
- Asking why the AI programs it one way and not the other way helps me understand concepts
- Ask the AI after it gives the answer "is this correct", sometimes it will correct itself if it spots a mistake
- Using AI for the companies CRUD flask routes taught me its best to create a different flask route for
each different CRUD operation than combing everything under one flask route. When separating them it is easier
to find which one went wrong and how. Combining them will make it harder to find errors.
- I learned how to access json information and comparing it with user input