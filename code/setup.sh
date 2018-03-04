# general of opal
rm -rf results
rm -rf tmp
mkdir tmp results
export TIME=00:30:00
export QUEUE=knlall
export TEMPLATES=`pwd`/tmpl/
export FIELDMAPS=/lcrc/project/AWA-beam-dynamics/FieldFiles/DriveFiles
export OPAL_EXE_PATH=/home/neveu/software/opal-1.9/knl/bin
