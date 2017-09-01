#!/usr/bin/env bash

group=$1
project=$2
source=$group/$project.git
dest=$dgroup/$dproject.git

git clone --bare git@gitlab.hopebaytech.com:$source
pushd $project.git
python /Users/can/workspace/transfer_tera/create_project.py $project
git push --mirror git@code.hopebaytech.com:Tera/$project.git
popd
rm -rf $project.git
echo $project
echo ' Transfer done!!'
