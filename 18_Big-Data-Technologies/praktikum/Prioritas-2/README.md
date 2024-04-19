## Hadoop Averrage Score
Simple Averrage Score using Hadoop MapReduce

### Requirements
1. Python3
2. Apache Hadoop
3. Apache Hadoop Streaming Library

### How To Use

1. Copy the sample data directory that contains many txt files for word counting to HDFS. Make sure to replace /home/hduser_ with the actual location in your local machine.

    ```
    hdfs dfs -copyFromLocal /home/hduser_/score /user/hduser_/score
    ```

2. Run this command to run Hadoop MapReduce.

    ```
    hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming.jar
    -file /home/hduser_/mapper-prio-2.py -mapper /home/hduser_/mapper-prio-2.py
    -file /home/hduser_/reducer-prio-2.py -reducer /home/hduser_/reducer-prio-2.py
    -input /user/hduser_/score/* -output /user/hduser_/output_score
    ```

3. Check the result.

    ```
    hdfs dfs -cat output_score/part-00000
    ```