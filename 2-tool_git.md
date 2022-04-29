# 1. Tool Git

## Introduction
Git is an open source `Distributed Version Control System` and it was created by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) in 2005 for development of [Linux kernel](https://github.com/torvalds/linux).

At Eureka, each project generally have multiple developers working in parallel. So a version control system like Git is needed to ensure there are no code conflicts between the developers.

Additionally, the requirements in such projects change often. So a version control system allows developers to revert and go back to an older version of the code.

Finally, sometimes several projects which are being run in parallel involve the same codebase. In such a case, the concept of branching in Git is very important.

### Learning git

#### Important reading
There are many resources out there to get familiar with Git but here are two selected tutorials:

- [An introduction to Git and GitHub for beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners).
- Free Udacity course on [Version control with Git](https://www.udacity.com/course/version-control-with-git--ud123)

You can always refer to this [cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet/) if needed during learning.

#### Git clients
There are a few git clients available to interact with Git. Feel free to use what is most
convenient:

- git CLI (recommended for starting)
- [magit](https://magit.vc/) (emacs): Strong recommended.
- [edamagit](https://marketplace.visualstudio.com/items?itemName=kahole.magit)
  (VSCode): A magit clone for VSCode. Very popular in Eureka for
  VSCode users.
- [smartgit](https://www.syntevo.com/smartgit/): A graphical client.

Do note that these tools are radically different, so if you want to
ask someone for help (and to learn from), make sure to use the same
git client.

At the moment, git CLI, [magit](https://magit.vc/) and
[edamagit](https://marketplace.visualstudio.com/items?itemName=kahole.magit)
are the most popular clients in Eureka. If you want to ask for help,
try to have the git clients available on your PC so that others people
can have an easier time helping you.

You can start first with Git CLI, once you have good understand how Git works and how to use Git commands, it is recommended to try `Emacs` and `magit`. The shared configuration file for `Emacs` of Eureka can be found [here](https://github.com/eurekarobotics/eureka-dotfiles).

## Git workflow

When you join and start to contribute, you would be expected to follow
the so-called [Github
Flow](https://docs.github.com/en/get-started/quickstart/github-flow). Make
sure that you read and understand this well enough.

## Further reading
- Read the [Pro git book](https://git-scm.com/book/en/v2) for more advanced topics such as `git subtree` or `git cherry-pick`
- Use the company [udemy](https://www.udemy.com/course/github-ultimate/?src=sac&kw=GitHub+Ultima) account to study the course `GitHub Ultimate: Master Git and GitHub`. Please contact Hung for the account credentials (optional)

## Assignments

These are perharps the most common use cases for git at Eureka:

- Fetch code from a remote.
- Understand the remote branch and local branch.
- Merge a remote branch into a local branch.
- Know how to force push to your own feature branch, and to never
  force push to a public branch.
- Know how to rebase and squash commits.
- Write good commits message when you submit a PR. When you are
  working on your own branch, it's fine to have commit message such as
  "wip", or "working now". These are not allowed, however, if you want
  to merge your PR. Squash them and write meaningful commit messages.
- Know how to cherry pick (advanced).
- Know how to inspect git history.
- Squash several commits into one.

The assignment below consists of a few parts. 

Submit the git repository and list of commands you use for each part when you are done. Then prepare to do a demo of the parts when required.

### Part 0: Setup
Setup a empty git repo with name `git-test` on GitHub with your account

### Part 1: Test on git branching and commit
Use git commands you have learnt to execute some actions below:

- Clone the created repo in part 0 to your PC
- Create one local branch name `feature-1` from `main` branch
- Add any file (python script or text file) and make a commit with good message
- Add another file and make another commit
- Push `feature-1` to remote

### Part 2: Test on git merge 
- Create local branch name `feature-2` from `main` branch
- Create arbitrarily 2 commits
- Merge the remote `feature-1` branch into `feature-2` local branch
- Push `feature-2` to remote
- On GitHub page, in `feature-2` branch, directly change content of `README.md` file and make a commit
- Merge the remote `feature-2` branch to local `feature-2` branch

### Part 3: Test on git rebase
- Create local branch name `feature-3` from `main` branch
- Create 2 commits
- Push `feature-3` to remote
- Rebase branch `feature-3` on `feature-1` and at the same time, squash latest 2 commits into 1
- Force push local `feature-3` branch to remote

### Part 4: Test on git cherry pick
- Create local branch name `feature-4` from `main` branch
- Create 2 commits
- Cherry pick any commit of `feature-1` branch
- Push `feature-4` to remote

### Part 5: Create a PR

- Read about Github Flow and make a PR following it.
