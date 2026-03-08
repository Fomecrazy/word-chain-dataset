<h1 align="center">Word Chain Dataset</h1>

Open-source dataset of word combinations used in the roblox game <a href="https://roblox.com">Word Chain</a>

## Contributing

We appreciate any help regarding the expansion of the dataset as any amount of new chains improves the gameplay by a lot. Feel free to open a pull request with changes and we will have it added to the game once verified.

### Contribution Guide

Wanna contribute and help us add more combinations? You can do so by following these steps:
1. Fork the repo by clicking the "Fork" button above the repo's About section. You will need:
	- a Github account(obviously)
	- an IDE(like [Visual Studio Code](https://code.visualstudio.com)) to edit the dataset comfortably,
	- [Git](https://git-scm.com) to be able to clone and commit the repo
2. Next, you'll want to run `git clone https://github.com/<your-username>/word-chain-dataset` and `cd word-chain-dataset` in a desired directory(you can do this through VSC).
	-  After you clone the repo, run `git remote add upstream https://github.com/Fomecrazy/word-chain-dataset` to set the upstream so you can be up-to-date with dataset updates later on.
3. Now that you have your fork in the IDE, it is recommended that you branch out with `git checkout -b <your-branch-name>` to avoid collisions with `main` later on.
	-  After you create the branch, run `git push -u origin <your-branch-name>` to publish the branch to your repo.
4. Once you've done that you can add combinations in `data/dataset/curated` or fix invalid ones in `data/subsets`. If you are gonna update `data/dataset/generated`, make sure it is ONLY to remove bad chains, for adding new ones use `data/dataset/curated`.
5. When you're done, run these commands in your IDE terminal:
```sh
	git add data/dataset/curated/<updated-file> #  git add . to stage all the changes
	git commit -m "<describe your change>"
	git push origin <your-branch-name>
```

6. Go to your fork on Github and open a pull request from <your-branch-name> to upstream main. The changes will be reviewed and merged after a while.
7. You can keep your fork's main branch up-to-date by switching to main and running these commands:
 - **make sure you move back into your feature branch and merge it with main with `git checkout <your-branch-name> git merge main` after doing this**
```sh
	git checkout main
	git fetch upstream
	git merge upstream/main
	git push origin main
```
