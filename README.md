Resume [![status-badge](https://woodpecker.ewpt3ch.dev/api/badges/2/status.svg)](https://woodpecker.ewpt3ch.dev/repos/2)

# Resume builder

### TODO

- ~limit rebuild to changes in markdown folder~
~ - get resume.html with all relevant info ~
~ - create link to download pdf ~
- create sub resumes for different roles(dev, data science, sysops) with links to the relevant html and pdf for specific job applications.

### How it works
Resume(s) are written in [markdown](https://www.markdownguide.org/) and stored in the markdown/ folder. When the project is pushed and has changes:
- in the markdown folder
- the src folder
- or the message [ALL] is in a commit
it outputs html and pdf files that get published at www.ewpt3ch.dev/resume.

### How to use it yourself
- clone the repo
- replace the content in markdown folder with you own
- replace 'name' in main.py, or import it somehow
- edit .woodpecker.yml or create github actions etc to build and publish at you domain.
