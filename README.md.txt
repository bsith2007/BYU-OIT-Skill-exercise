Good Morning Eric,

I wanted to let you know I didnt get as far as I wanted to on this project. As such I hope that you will accept this verbal explaination as proof of my knowledge and experience. 

Technique
Per the instructions and due to my lack of previous experience with the other languages recomended I decided to dive into learning Python. As a whole I was pleased to see how powerful it is and capable of performing the operations to complete this project.

Assumptions
-Using the Github API repository by organization will give a list of all repositories that belong to byu-oit
-Python code will be executed on Python 3.4 as to be compatible with the MySQL/Python connector to allow connection to the Amazon RDS MySQL instance that I set up.
-Requests package has been installed on the Python 3.4 instance.

Steps
1-Use API Organization Repository method to get the repository name and URL write repository data to MySQL while iterating thought the for loop
2-Use API repository name to evaluate the files in the repository and get the download URL and Path to the .repo-meta.yml file (I know that the instructions said the repo.meta but I made the assumption that they are the same)
3-Use API to get additional file meta data as desired .repo-meta.yml file
4-Open the .repo-meta.yml file and use regular expressions to be able to parse the information and capture desired values.
5-write values to SQL using MySQL/Python connector while iterating through values
6-write repository URLs without .repo-meta.yml files to list on text file.

Accomplishments 
-I was able to get my script to capture API data by looping through the data and used nested looping statements to get the data needed to be able to get the download URL.
-I was able to install requests and MySQL/Python connector
-I was able to learn the Python language and begin to see how I would be able to complete the project from start to finish.
-given more time I would have been able to complete the project assuming that I would be able to resolve or work arround the issues below.

Issues,
-I was struggling with the API Rate Limit as I was trying to test my code.
-When I iterated through the repositorys to get the repository names I only got approximately 20 out of the 622 BYU public repositories. was not yet able to troubleshoot this issue.
-Had originally thought that the content element of the API repositories would give me content in plain text not requiring me to open the file. 
-I struggled with the instructions on how to install packages using pip as it would appear that the instalation has changed over time.