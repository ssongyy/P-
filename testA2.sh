#!/bin/sh
bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input2/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab1/input2/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /root/project/new.txt /lab1/input2/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../Project1/mapperA2.py -mapper ../Project1/mapperA2.py \
-file ../Project1/ReducerA2.py -reducer ../Project1/ReducerA2.py \
-input /lab1/input2/* -output /lab1/output2/
/usr/local/hadoop/bin/hdfs dfs -cat /lab1/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input2/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output2/
bash /mapreduce-test/stop.sh
