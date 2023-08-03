---
title: "优化HDFS性能:在Kunpeng920上实现硬件加速器和Arm64多核能力的均衡利用"
date: "2023-08-19T16:15:00" 
track: "performance"
presenters: "徐国栋"
stype: "中文演讲"
---
Hadoop/HDFS Transparent Encryption 对现有服务器提出性能挑战。传统上我们进行加密计算的有两种途径，一种是CPU专有指令，一种是专用硬件加速器。

专用硬件加速器通过优化的算法和架构，提供更高的加解密带宽。同一时期，CPU Processor（Intel AES-NI, Arm64 Crypto-Extension）也具备专有指令来针对性的调优加密性能。CPU和硬件加速器之间的速度差别逐渐缩小。我们有更多的理由把CPU核心与专有硬件放到同一个resource pool当中进行使用。如何更好的平衡CPU核心和专有硬件加速器之间两者的性能（例如，在硬件加速器到达性能瓶颈时，能够采用CPU核来作为后备处理单元）这是一个挑战。

本演讲介绍一种基于 OpenSSL 3.0 同一算法可以注册多个实现的特性，在算法的多种实现之间动态资源调配。所构成的resource pool调配资源库可以涵盖多种算法实现实体。“计算”得以在多种实现实体之间调配，从而获得更高资源使用效率。从云厂商角度，相同硬件可以支撑更多用户。从用户角度，可以达到更高性能。

演讲的最后介绍通过这种方法，在HDFS Transparent Encryption中达到的性能提升。

 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230617/2215411950.jpg" width="200" /><br>徐国栋: Linaro有限公司, 高级技术主管。
 
- 2012-2023 Linaro有限公司
  - Arm SVE/SVE2优化，进行软件库优化
  - 大数据，Apache Bigtop
  - 内核开发
- 2008-2011伟创力有限公司软件开发主管
- 2002-2007摩托罗拉移动，Linux内核设备驱动程序开发 
 <br><br>