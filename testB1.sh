#!/bin/sh
bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/input1/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output1/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab2/input1/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /root/project/shot_F.txt /lab2/input1/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../Project1/mapperB1.py -mapper ../Project1/mapperB1.py \
-file ../Project1/ReducerB1.py -reducer ../Project1/ReducerB1.py \
-input /lab2/input1/* -output /lab2/output1/
/usr/local/hadoop/bin/hdfs dfs -cat /lab2/output1/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/input1/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output1/
bash /mapreduce-test/stop.sh
