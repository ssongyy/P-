#!/bin/sh
bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/input2/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output2/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/input21/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/output21/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab2/input2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab2/input21/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /root/project/shot_F.txt /lab2/input2/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../Project1/mapper1B2.py -mapper ../Project1/mapper1B2.py \
-file ../Project1/Reducer1B2.py -reducer ../Project1/Reducer1B2.py \
-input /lab2/input2/* -output /lab2/output2/
/usr/local/hadoop/bin/hdfs dfs -cat /lab2/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -cp /lab2/output2/part-00000 /lab2/input21/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../Project1/mapper2B2.py -mapper ../Project1/mapper2B2.py \
-file ../Project1/Reducer2B2.py -reducer ../Project1/Reducer2B2.py \
-input /lab2/input21/* -output /lab2/output21/
/usr/local/hadoop/bin/hdfs dfs -cat /lab2/output21/part-00000
bash /mapreduce-test/stop.sh
