## Hadoop Word Polindrom or Not
Simple Word Polindrom using Hadoop MapReduce

### Requirements
1. Python3
2. Apache Hadoop
3. Apache Hadoop Streaming Library

### How To Use

1. Copy the sample data directory that contains many txt files for word counting to HDFS. Make sure to replace /home/hduser_ with the actual location in your local machine.

    ```
    hdfs dfs -copyFromLocal /home/hduser_/word /user/hduser_/word
    ```

2. Run this command to run Hadoop MapReduce.

    ```
    hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
    -file /home/hduser_/mapper-eks.py -mapper /home/hduser_/mapper-eks.py \
    -input /user/hduser_/word/* -output /user/hduser_/output_words
    ```

3. Check the result.

    ```
    hdfs dfs -cat output_words/part-00000
    ```