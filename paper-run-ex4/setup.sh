# general of opal
rm -rf results *.0 *_0
rm -rf tmp
mkdir tmp results
export QUEUE=knlall
export TEMPLATES=`pwd`/tmpl/
export TIME=01:00:00
