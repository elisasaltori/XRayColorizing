#!/bin/bash
N=$(ls $2| wc -l)
FILES=`ls $2`
for i in `seq 1 $N`
do
    FILE=$(echo $FILES| cut -d ' ' -f $i)
    FULL="$2$FILE"
    python3 main.py "$1" "$FULL" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "${10}"
done



