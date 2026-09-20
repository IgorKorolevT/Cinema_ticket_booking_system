## Git

The project was developed using Git and separate feature branches.

### Branches

* `master` — main branch containing the completed project.
* `feature/movies` — used to add movie management: movie list, adding movies and viewing movie information.
* `feature/booking` — used to implement ticket booking, selecting a movie and ticket quantity.
* `feature/cancel-booking` — used to implement booking cancellation.
* `feature/search` — used to add movie search by title.
* `feature/favorites` — used to add movies to the favorites list.
* `feature/menu` — used to create the first version of the main menu.
* `feature/menu-update` — used to create another version of the main menu.
* `feature/statistics` — used to add cinema statistics.
* `feature/discount` — used to add ticket discount calculation.
* `feature/test` — used to practice `git stash`.

### Merge Conflict

A merge conflict occurred between `feature/menu` and `feature/menu-update`.

Both branches modified the same part of `src/main.py` containing the main menu.

The conflict was resolved manually by opening the conflicting file, reviewing the changes from both branches, keeping the required menu version, removing the conflict markers, and then completing the merge with:

```bash
git add .
git commit
```

### Rebase

`git rebase` was used in the `feature/statistics` branch.

After new changes were added to `master`, the `feature/statistics` branch was rebased onto the updated `master`:

```bash
git switch feature/statistics
git rebase master
```

This demonstrated how feature branch commits can be replayed on top of the latest `master` commits.

### Cherry-pick

`git cherry-pick` was used with the `feature/discount` branch.

The ticket discount functionality was implemented and committed in `feature/discount`. The specific commit was then copied to `master` using:

```bash
git switch master
git cherry-pick <commit-hash>
```

### Stash

`git stash` was practiced in the `feature/test` branch.

Uncommitted changes were temporarily saved using:

```bash
git stash
```

After switching to another branch and completing the required work, the changes were restored with:

```bash
git stash pop
```

### Remote Branches

The following commands were used to work with local and remote branches:

```bash
git branch
git branch -r
git branch -a
git fetch
git remote -v
```

### Branch Deletion

After completing the work, the `feature/movies` branch was deleted locally and from GitHub:

```bash
git branch -d feature/movies
git push origin --delete feature/movies
```
