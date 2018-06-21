while true
do
	now=$(date +"%H")
	if [ $now == 9 ]
	then
		python3 weather.py
	fi
	sleep 60m
done
