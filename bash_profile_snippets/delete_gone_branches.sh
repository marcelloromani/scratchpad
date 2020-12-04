delete_gone_branches() {
    actually_delete="$1"
    git fetch -p
    branches=$(git branch -av | grep gone | awk '{ print $1 }')
    echo -e "Gone branches:\n$branches"
    if [[ "$actually_delete" == "--delete" ]] ; then echo "Deleting..." ; echo $branches | xargs -L 1 git branch -D ; else echo "use --delete to remove those branches" ; fi
}
