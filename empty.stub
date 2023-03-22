# Workbench

A simple brainstorming space, powered by the github frontend, a github action, and a simple python script.

For people who don't mind sharing their ideas or their brainstorming process publicly.  
Remember: there are no bad ideas in brainstorming.

**What it looks like in action:** https://github.com/dmarx/bench-warmers  

## How To Use

1. Follow the setup instructions below build your own workbench.
2. Select `Add File > Create New File` to add a new markdown file containing the idea you want to log.
3. Upon committing, a github action runs which builds the README, which is customizable from a template.

The generated `README.md` will contain a Table of Contents for your ideas, and supports the following features:

* Sorting the most recently modified ideas at the top
* Customized tags
* An "estimated idea maturity" metric (it's just a wordcount).

**How the README builds itself:**  https://stackoverflow.com/a/72918091/819544  

# Setup your own

1. Fork this repository
2. Set "write" access on your `${{ secrets.GITHUB_TOKEN }}`,[instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-default-github_token-permissions) here.
3. Change the name of README.stub.template to README.stub
4. Author markdown files

# Rules

1. markdown filenames contain no whitespace
2. the first line (title) starts with a single 'pound' character). 
3. use `lightgrey` badges to add a tag to an idea. Yes, this is begging for a simpler approach.

If you don't like these rules, I welcome PRs ;)
