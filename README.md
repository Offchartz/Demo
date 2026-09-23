# **THIS IS A DEMO REPOSITORY**

## **CREATED TO LEARN GITHUB \& GIT**

### **THESE ARE THE STEPS TO CREATE AND ADD A GIT INTO GITHUB:**



**git init**

Initializes a new, empty Git repository in the current working directory.





**git config --global user.name "Your Name"**

**git config --global user.email "your-email@example.com"**

Sets your global author name and email address, which will be attached to all of your future commits.





**git status**

Displays the state of the working directory and staging area, allowing you to see which files are modified or currently untracked.





**git add .**

Stages all new, modified, and deleted files in the current directory, preparing them to be committed.





**git commit -m "Initial commit"**

Saves your staged changes into the local repository's version history along with the descriptive message "Initial commit".





**git branch -M main**

Renames the current default local branch to `main`.





**git remote add origin https://github.com/YourUsername/YourRepository.git**

Connects your local repository to a remote repository URL (hosted on GitHub) and assigns it the shorthand name `origin`.





**git remote -v**

Lists all configured remote repositories to verify that the connection URL was added successfully.





**git push -u origin main**

Uploads your local `main` branch commits to the remote `origin` repository. The `-u` flag sets the upstream tracking, meaning future pushes can be executed with just the `git push` command.

