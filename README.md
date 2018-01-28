# hadoop-streaming

A sample hadoop-streaming map-reduce program. The goal of this program is to count the number of times each keyword-value occurs in the given input data. The traditional python code (using pandas) was very slow and used to take more than 24 hours to complete. With hadoop-streaming, it came down to ~1hour.

Run on Local Machine - 
cat sample_input.txt | python mapper.py | sort | python reducer.py

Run on Hadoop/EMR cluster - 
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -mapper 'python /home/hadoop/mapper.py' -reducer 'python /home/hadoop/reducer.py' -input 's3://<my-input-location>/' -output 's3://<my-output-location>/'
