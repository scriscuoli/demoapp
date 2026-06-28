#!/bin/bash
# deploy.sh - deploy script for all apps

ZIPFILE="${1}"
ZIPDIR=$(dirname $ZIPFILE)
ZIPNAME=$(basename ${ZIPFILE%.*})
UNZIPDIR="${ZIPDIR}/${ZIPNAME}"
REPONAME=$(echo $ZIPNAME | awk -F- '{print $1}')
DEPLOYDIR="/opt/apps/${REPONAME}"
DUSR="steve"
DGRP="www-data"

echo "ZIPFILE= $ZIPFILE"
echo "ZIPDIR= $ZIPDIR"
echo "ZIPNAME= $ZIPNAME"
echo "REPONAME= $REPONAME"
echo "DEPLOYDIR= $DEPLOYDIR"

sudo mkdir -p $DEPLOYDIR
sudo chmod 777 -p $DEPLOYDIR


echo "cd $ZIPDIR"
cd $ZIPDIR
echo "unzip $ZIPFILE"
unzip $ZIPFILE
echo "sudo cp -r $UNZIPDIR/* $DEPLOYDIR/"
sudo cp -r $UNZIPDIR/* $DEPLOYDIR/
echo "sudo chown -R $DUSR:$DGRP $DEPLOYDIR"
sudo chown -R $DUSR:$DGRP $DEPLOYDIR
echo "sudo chmod -R 777 $DEPLOYDIR"
sudo chmod -R 777 $DEPLOYDIR
echo "rm -rf $UNZIPDIR"
rm -rf $UNZIPDIR
echo "rm -f $ZIPFILE"
rm -f $ZIPFILE
exit

