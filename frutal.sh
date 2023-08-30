#!/bin/bash
declare -i jugadors=0
declare -i corb=0
jugadors_victoria="VICTORIA DELS JUGADORS"
corb_victoria="VICTORIA DEL CORB"

for (( c=1; c<=100; c++ ))
do 
   resultat=$(python frutal.py 1 4)
   if [ "$resultat" == "$jugadors_victoria" ]; then
      ((jugadors=jugadors + 1))
   fi

   if [ "$resultat" == "$corb_victoria" ]; then 
      ((corb=corb+1))
   fi
done

echo "Victòries dels jugadors: $jugadors"
echo "Victòries del corb: $corb"
