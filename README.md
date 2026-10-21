# Git Workflow Playground

A tiny Python to-do list built to practice team Git & GitHub workflows: feature branches, interactive rebasing, resolving merge conflicts, and reviewing and merging pull requests.

## Run it

```bash
python3 todo.py add "Finish capstone report"
python3 todo.py list
python3 todo.py done 0
python3 -m unittest
```

## Practice scenario

A "teammate" has an open pull request (`teammate/priority-labels`) that changes how tasks are displayed. You'll build a competing feature (due dates) that touches the same lines, so you can practice:

1. **Feature branch:** do your work on `feature/due-dates`, never directly on `main`.
2. **Interactive rebase:** clean up messy work-in-progress commits with `git rebase -i`.
3. **Pull request review:** review and merge the teammate's PR on GitHub.
4. **Merge conflict:** rebase your branch onto the updated `main` and resolve the conflict in `format_task`.
5. **Your own PR:** push with `--force-with-lease`, open a PR, and squash-merge it.

Useful setup:

```bash
git config --global merge.conflictstyle zdiff3
git config --global alias.graph "log --oneline --graph --decorate --all"
```
