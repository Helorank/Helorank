HOST="ec2-54-225-91-60.compute-1.amazonaws.com"
DATABASE="deaensll3m9a0s"
USERNAME="zdudfdflhhgqbj"
COMMAND_STRING="-h $HOST -d $DATABASE -U $USERNAME"
if [ -n "$1" ]
	then 
		FILE=$1
		COMMAND_STRING+=" -f $FILE"
fi
psql $COMMAND_STRING
