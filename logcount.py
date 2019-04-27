from pyspark import SparkContext
from operator import add
import time

start = time. time()
sc = SparkContext()
text  = sc.textFile('input').flatMap(lambda line: line.split(','))
text1 = text.map(lambda kval : (kval,1) if kval == "200" or kval=="206" or kval=="302" or kval=="304" else (kval,0))
text2 = text1.reduceByKey(add)
out = text2.collect()
end = time. time()
print("##############Time:",(end-start))
for o in out:
    print("@@@@@@@@@@@@Output",o)

