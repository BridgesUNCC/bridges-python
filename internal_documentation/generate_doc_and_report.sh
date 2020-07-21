#!/bin/sh

(
    cat bridges_doxygen_python.cfg
    echo "PROJECT_NUMBER = `git describe --tags`"
) | doxygen - 2>&1 | tee log

rm report*

grep warning log | sed 's/.*\/\([a-Z_0-9]*\.py\).*/\1/g' | sort | uniq -c > report

for file in $(grep warning log | sed 's/.*\/\([a-Z_0-9]*\.py\).*/\1/g' | sort | uniq);
do
    grep /$file log > report.${file}
done

    
echo
echo
echo
cat report
echo
echo ===========================================
echo See per file report with "cat report.$file"
echo ===========================================

