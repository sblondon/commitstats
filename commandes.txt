Extraire les fichiers ajoutés ou modifiés

git log --since 2020 --name-status | grep -P "^[AM]\t" | cut -f 2 | sort | uniq -c | sort --ignore-leading-blanks --numeric-sort --reverse | sed "s/^[ \t]*//" > stats.txt

