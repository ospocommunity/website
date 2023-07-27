---
title: "FlinkSQL's field parentage and data permission solution"
date: "2023-08-18T15:00:00" 
track: "streaming"
presenters: "白松"
stype: "Chinese Session"
---
1. At present, with the rise of real-time data warehouse represented by Flink, enterprises have an increasingly urgent demand for data kinship and data security. However, due to the relatively short development of Flink real-time data warehouse field, Apache Ranger and Atlas do not support FlinkSQL, and relying on Ranger and Atlas will lead to heavy system deployment and operation and maintenance. Therefore, I developed FlinkSQL field lineage and data permission solutions, hoping to create an Atlas+Ranger in the field of Flink real-time data warehouse. In terms of technical implementation, it can achieve zero intrusion of Flink and Calcite source code, and can be quickly integrated into real-time platform products.

2. From 0 to 1 technology innovation data desensitization and row-level permission solution in FlinkSQL, and open source on Github. The article "FlinkSQL's Data Desensitization Solution" was published on Apache Flink wechat on May 10, 2023 and received 4792 views and 19 likes, and was read on InfoQ website 4104.
https://github.com/HamaWhiteGG/flink-sql-security
https://mp.weixin.qq.com/s/gN1mvqIk7xOBpf68YgReSg

1. Self-developed FlinkSQL field level blood open source project obtained 215 star and 90 fork on Github, has been integrated into the one-stop real-time computing platform Dinky(2000 star), and the source code has been adopted by Shopee, Mihayou, Steady medical, Daily interaction and other companies. On March 9, 2023, I shared a video and published an article on DataFun, which was attended by more than 1000 people and read by 2236 articles.
https://github.com/HamaWhiteGG/flink-sql-lineage
https://mp.weixin.qq.com/s/aBPbITpUDCWgWvOLLcscqg
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230517/0910148400.jpg" width="200" /><br>White pine: Hangzhou Sulan Technology Co., LTD, Deputy general manager of R&D center, Co-founder of Sulan Technology Co., LTD., Deputy general manager of R & D Center, has 9 years of big data platform research experience, focusing on big data, real-time computing, data rights and other fields of research. Responsible for the company's core products digital platform and digital EMR product research and development, digital products have become hundreds of domestic and foreign companies to build data center infrastructure tools, such as CITIC Group, Foxconn, Vanke, BMW, Zhejiang Trading Group and so on.
 <br><br>