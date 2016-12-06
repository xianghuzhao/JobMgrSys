#!/bin/sh

if [ -n "$JSUB_log_dir" ]; then
    logdir=$JSUB_log_dir
else
    logdir=`pwd`
fi

out="$logdir/command.out"
err="$logdir/command.err"

# execution of command
cmd=$JSUB_command
eval $cmd 1>$out 2>$err

# save the exit code
result=$?

exit $result