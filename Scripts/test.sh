#script for automatically running image tests
#!/bin/bash
if [ $# -eq 5 ]
then
    FILES=`ls $1`
    N=$(ls $1| wc -l)
    for i in `seq 1 $N`
    do
        FILE=$(echo $FILES| cut -d ' ' -f $i)
        FULL="$1/$FILE"
        for j in `seq 1 3`
        do
            for k in `seq 1 2`
            do
                for l in `seq 1 3`
                do
                    for m in `seq 0 2`
                    do
                        NAME="$j$k$l$m"
                        python3 main.py "$NAME" "$FULL" "$j" "$2" "$3" "$k" "$4" "$5" "$m" "$l"
                    done
                done
            done
        done
    done
else
    echo "usage: (path) (smooth filter size) (smoot sigma) (shap filter size) (sharp sigma)"
fi
