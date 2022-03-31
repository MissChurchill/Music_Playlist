# music_playlist
This is my capstone project submitted after participating in the data analysis course 1 through Code Louisville. 

The purpose of the capstone project is to reinforce what was learned and show off my skills. This project shows off my new skills to potential employers and demonstrates my knowledge of Python, it’s methods and implementation. The project requirements include implementing a simple data analysis by reading data, performing calculations on the data, and displaying the results.

Packages that need to be installed to run the project include standard Python libraries and pip install of pandas in a virtual environment. Imports to the project include: json and requests.

The goal of the application is to allow users to create a music playlist and get information about songs that they enter and disply information in tabular form. The application can be used for creating a music playlist for your next car trip, tunes to run to on your next jog, or a playlist for your next family event.

The 3 features included in my project based on the requirements include:
1. Python Programming Basics: Implements a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program. Specifically, in this application the user inputs a song they would like added to their playlist. In order to exit the program, the user must enter quit in all lowercase.
2. Utilize External Data: Connect to an external/3rd party API (Application Programming Interface) and reads data into your app. In this application we use the following API source: https://itunes.apple.com which does not require an authentication key to access and returns information pertaining to the song.
3.  Data Display: Display data in tabular form. In our program, we use pandas to display the data in a dataframe for visual presentation.

Future Enhancements for the Project
What if the user enters a song and there is more than one version from various musicians? Currently, our program does not account for this edge case.  The API is set to return only one response so it will show the most popular option based on the search. In the future, I would want to enhance the app to allow the user to see all the various artists who have produced the song and allow the user to select their desired version to add to create their music playlist.
