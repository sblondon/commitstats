# List added or modified files

```
cd ${GIT_REPOSITORY}
git log --since 2020 --name-status | grep -P "^[AM]\t" | cut -f 2 | sort | uniq -c | sort --ignore-leading-blanks --numeric-sort --reverse | sed "s/^[ \t]*//" > stats.txt
```

# Outputs statistics

```
mv stats.txt ${COMMITSTATS_DIR}
python3 analyze.py
```
