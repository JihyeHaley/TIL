# day2

`cat $HADOOP_HOME/etc/hadoop/core-site.xml` : 특정한 환경변수의 값을 사용할 때는 리눅스의 경우에는 $기호를 사용한다.​

**hdfs-site.xml** 

`cat $HADOOP_HOME/etc/hadoop/hdfs-site.xml`

```
   <property>
      <name>dfs.replication</name>
      <value>3</value>
   </property>
```

3개의 복제본을 복사해주세요 라는 것 !! main하나에 복제본 2개

```
   <property>
      <name>dfs.name.dir</name>
      <value>/root/hadoop-2.7.7/hdfs/name</value>
   </property>
```

namenode를 보관하는 곳 ↑

/root/hadoop-2.7.7/hdfs/ncame 이루트로 들어가서 ls하면 하둡 파일에 대한 전반적으로 담고 있는 이미지 파일이 들어있다.

m1

```
   <property>
      <name>dfs.data.dir</name>
      <value>/root/hadoop-2.7.7/hdfs/data</value>
   </property>
```

datanode를 보관하는 곳 ↑

/root/hadoop-2.7.7/hdfs/data 이 루트로 들어가서 더 들어가야한다. 순서대로 써보면 `cd current` `cd BP-128어쩌구저쩌구` `cd finalized` `cd current` `cd current` 에서 ll 치면 여기에 파일들이 숨어있다. `cat명령어를 사용해서 확인해보자!

m2, m3, m4

```
   <property>
      <name>dfs.support.append</name>
      <value>true</value>
   </property>
```

파일 시스템을 수정하지 않고 그냥 append만 한다. !! 파일이 너무 수정할 것이 많을것이고 수정하는게 어떤 파일을 해야할지 모르니까 그냥 안하는게 좋다고 판단하여 넣고 읽는것만 가능하고 새롭게 넣는 방식을 사용한다.



