#!/bin/bash
if [ $# -eq 6 ]
then
    FILES=`ls $1`
    N=$(ls $1| wc -l)
    for i in `seq 1 $N`
    do
        FILE=$(echo $FILES| cut -d ' ' -f $i)
        FULL="$1$FILE"
        for j in `seq 1 3`
        do
            for k in `seq 1 2`
            do
                for l in `seq 1 3`
                do
                NAME="$j$k$l"
                python3 main.py "$NAME" "$FULL" "$j" "$2" "$3" "$k" "$4" "$5" "$6" "$l"
                done
            done
        done
    done
else
    echo "usage: (path) (smooth filter size) (smoot sigma) (shap filter size) (sharp sigma) (equalization method)"
fi
