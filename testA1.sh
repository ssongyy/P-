#!/bin/sh
bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input1/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output1/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab1/input1/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /root/project/new.txt /lab1/input1/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../Project1/mapperA1.py -mapper ../Project1/mapperA1.py \
-file ../Project1/ReducerA1.py -reducer ../Project1/ReducerA1.py \
-input /lab1/input1/* -output /lab1/output1/
/usr/local/hadoop/bin/hdfs dfs -cat /lab1/output1/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/input1/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab1/output1/
bash /mapreduce-test/stop.sh
