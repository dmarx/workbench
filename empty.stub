# Workbench

![Stable Diffusion illustration of a wizard's cluttered workshop](193496338_surrealist__illustration_of_a_workbench_cluttered_with_colorful_objects_and_items_representing_the_u.png)

A simple brainstorming space, powered by the github frontend, a github action, and a simple python script.

For people who don't mind sharing their ideas or their brainstorming process publicly.  
Remember: there are no bad ideas in brainstorming.

**What it looks like in action:** https://github.com/dmarx/bench-warmers  

# Setup

1. Fork this repository
2. Click on the "Actions" tab and activate github action workflows on your fork.
3. Change the name of `README.stub.template` to `README.stub`

<!--
2. Set "write" access on your `${{ secrets.GITHUB_TOKEN }}`, [instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-default-github_token-permissions) here.
-->


# Usage

1. Select `Add File > Create New File` to add a new markdown file containing the idea you want to log.
2. Upon committing, a github action runs which builds the README, which is customizable from a template.

The generated `README.md` will contain a Table of Contents for your ideas, and supports the following features:

* Infers modification date from commit history
* Sort most recently modified ideas at the top
* Hyperlink to document using markdown title as anchor text
* An "estimated idea maturity" metric (it's just character count atm).
* Custom tagging
* Wikipedia-esque "category" pages which group articles by tag

## Rules

1. markdown filenames contain no whitespace
2. the first line (title) starts with a single 'pound' character). 
3. use `lightgrey` badges to add a tag to an idea. Yes, this is begging for a simpler approach.

If you don't like these rules, I welcome PRs ;)


# Technical details


**How the README builds itself:**  https://stackoverflow.com/a/72918091/819544  

