---
title: "The practice and optimization of data Lake Iceberg in Xiaomi"
date: "2023-08-18T15:45:00" 
track: "datalake"
presenters: "肖杰宝"
stype: "Chinese Session"
---
Introduction: This sharing focuses on introducing the reasons and current situation of Xiaomi's internal introduction of Iceberg, as well as the practice of using Iceberg to upgrade its business architecture, including the optimization of Iceberg Parquet file filtering capability, and the evolution and landing of managed table optimization service architecture.
Outline:
- Why Iceberg is introduced and its current situation
This paper introduces the reason why Iceberg is introduced in Millet and the current production state of Iceberg in millet
- Lakehouse architecture upgrade practice
It is divided into two parts: table upgrade practice and business architecture upgrade practice. The table upgrading practice mainly describes how to upgrade Hive tables into Iceberg tables and how to make them into products. It also provides the selection of table building strategies, so that different parameters and optimization methods are used for tables with different strategies, so that the upgraded tables are more suitable for their respective scenarios. The service architecture upgrade practice mainly brings practical services to obtain greater benefits by upgrading links to the lake architecture
- Iceberg Parquet file filtering optimization
This paper mainly introduces the reading principle of Iceberg table and the internally developed Parquet Column Index function. How to further improve the Data Skipping ability of Iceberg table
- Construction and evolution of managed table optimization services
This paper mainly introduces how the managed table optimization service solves the usability problem and the architecture evolution process, and how to achieve the purpose of cost reduction and efficiency increase through the asynchronous optimization task of the service
- Future Planning
This paper mainly introduces the future work carried out by Xiaomi based on Iceberg, such as index construction, storage hybrid cloud architecture, extended table optimization service ability and so on
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230601/1439170843694195.png" width="200" /><br>Xiao Jiebao: millet, Software development engineer, Xiaomi software research and development engineer, currently mainly responsible for the research and development of Xiaomi's internal data lake Iceberg core and table optimization services.
 <br><br>