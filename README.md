# hadoop-streaming

A sample hadoop-streaming map-reduce program. The goal of this program is to count the number of times each keyword-value occurs in the given input data. The traditional python code (using pandas) was very slow and used to take more than 24 hours to complete. With hadoop-streaming, it came down to ~1hour.

# Run on Local Machine - 
cat sample_input.txt | python mapper.py | sort | python reducer.py

# Run on Hadoop/EMR cluster - 
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/mapper.py,/home/hadoop/reducer.py -mapper 'mapper.py' -reducer 'reducer.py' -input 's3://<loc>' -output 's3://<loc>'

# References - 
https://hadoop.apache.org/docs/current/hadoop-streaming/HadoopStreaming.html
http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
