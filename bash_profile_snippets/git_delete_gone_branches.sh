git_delete_gone_branches() {
    actually_delete="$1"
    git fetch -p
    branches=$(git for-each-ref --format '%(refname:strip=2) %(upstream:track)' refs/heads | awk '$2 == "[gone]" {print $1}')
    echo -e "Gone branches:\n$branches"
    if [[ "$actually_delete" == "--delete" ]] ; then echo "Deleting..." ; git branch -D $branches; else echo "use --delete to remove those branches" ; fi
}
