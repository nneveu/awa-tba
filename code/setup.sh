# general of opal
rm -rf results *.0 *_0
rm -rf tmp
mkdir tmp results
export QUEUE=knlall
export TEMPLATES=`pwd`/tmpl/
export FIELDMAPS=/lcrc/project/AWA-beam-dynamics/FieldFiles/DriveFiles
export OPAL_EXE_PATH=/lcrc/project/AWA-beam-dynamics/software/opal/opal-1.9/build-knl/src
