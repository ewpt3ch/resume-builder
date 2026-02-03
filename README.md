Resume [![status-badge](https://woodpecker.ewpt3ch.dev/api/badges/2/status.svg)](https://woodpecker.ewpt3ch.dev/repos/2)

# Resume builder

### TODO

- ~limit rebuild to changes in markdown folder~
- get resume.html with all relevant info
- create link to download pdf
- create sub resumes for different roles(dev, data science, sysops) with links to the relevant html and pdf for specific job applications.

Resume(s) are written in [markdown](https://www.markdownguide.org/) and stored in the markdown/ folder. When the project is pushed and has changes:
- in the markdown folder
- the src folder
- or the message [ALL] is in a commit
it outputs html and pdf files that get published at www.ewpt3ch.dev/resume.
