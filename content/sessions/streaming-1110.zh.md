---
title: "FlinkSQL的字段血缘及数据权限解决方案"
date: "2023-08-18T15:00:00" 
track: "streaming"
presenters: "白松"
stype: "中文演讲"
---
1.  当前随着以Flink为代表的实时数仓的兴起，企业对数据血缘、数据安全的需求越来越迫切。但由于Flink实时数仓领域发展相对较短，Apache Ranger 和Atlas 还不支持FlinkSQL，且依赖Ranger和Atlas会导致系统部署和运维过重。 因此，自研出FlinkSQL的字段血缘及数据权限解决方案，希望创造出Flink实时数仓领域的Atlas+Ranger 。在技术实现上做到对Flink和Calcite源码的零侵入，可以快速集成到实时平台产品中。

2. 从0到1技术创新出FlinkSQL中的数据脱敏和行级权限解决方案，并在Github开源。文章《FlinkSQL的数据脱敏解决方案》在2023年5月10日 发表在Apache Flink 微信公众号获得4792阅读和19赞，在InfoQ官网4104阅读。
https://github.com/HamaWhiteGG/flink-sql-security
https://mp.weixin.qq.com/s/gN1mvqIk7xOBpf68YgReSg

1.  自研的FlinkSQL字段级血缘开源项目在Github上获得215 star和90 fork，已被集成进一站式实时计算平台Dinky(2000 star)中，且源码被Shopee、米哈游、稳健医疗、每日互动等公司采用。2023年3月9日在DataFun上进行过视频分享并发布文章，1000多人次参加及2236文章阅读量。
https://github.com/HamaWhiteGG/flink-sql-lineage
https://mp.weixin.qq.com/s/aBPbITpUDCWgWvOLLcscqg
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230517/0910148400.jpg" width="200" /><br>白松: 杭州数澜科技有限公司, 研发中心副总经理, 数澜科技公司联合创始人、研发中心副总经理，拥有9年大数据平台研发经验，专注于大数据、实时计算、数据权限等领域的研究。负责公司核心产品数栖平台和数栖EMR的产品研发工作，目前数栖产品已成为国内外数百家公司建设数据中台的基础设施工具，例如中信集团、富士康、万科、宝马、浙江交投集团等。
 <br><br>