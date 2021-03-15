parse_git_branch() {
    git branch 2>/dev/null | grep \* | awk '{ print $2 }'
}

export PS1="\u@\h \[\033[32m\]\w\[\033[33m\] \$(parse_git_branch)\[\033[00m\] $ "
