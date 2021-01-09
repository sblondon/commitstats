# List added or modified files

```
cd ${GIT_REPOSITORY}
git log --since 2020-01-01 --until 2020-12-31 --name-status | grep -P "^[AM]\t" | cut -f 2 | sort | uniq -c | sed "s/^[ \t]*//" > stats.txt
```

`stats.txt` contains list for year 2020. Each line uses the format `qty path`.

# Outputs statistics

```
mv stats.txt ${COMMITSTATS_DIR}
python3 analyze.py
```
