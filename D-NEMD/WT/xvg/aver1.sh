for d in tpr[0-9]
do
    ( cd "$d" && gmx rms -s "$d".tpr -f "$d"_noPBC.xtc -b 0 -e 1 -a )
done
