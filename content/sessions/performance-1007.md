---
title: "Optimizing HDFS Performance: Achieving Balanced Utilization of Hardware Accelerators and Arm64 Multi-Core Capabilities on Kunpeng920"
date: "2023-08-19T16:15:00" 
track: "performance"
presenters: "Guodong Xu"
stype: "Chinese Session"
---
Hadoop/HDFS Transparent Encryption presents performance challenges for existing servers. Traditionally, there are two ways to perform encryption calculations: one is through CPU proprietary instructions, and the other is through dedicated hardware accelerators.

Dedicated hardware accelerators provide higher encryption/decryption bandwidth through optimized algorithms and architecture. At the same time, CPU processors (Intel AES-NI, Arm64 Crypto-Extension) also have proprietary instructions to optimize encryption performance. The speed difference between CPU and hardware accelerators is gradually narrowing. We have more reasons to put CPU cores and dedicated hardware in the same resource pool for use. Balancing the performance between CPU cores and dedicated hardware accelerators (such as using CPU cores as backup processing units when the hardware accelerator reaches its performance bottleneck) is a challenge.

This presentation introduces a feature based on OpenSSL 3.0, which allows multiple implementations to be registered for the same algorithm, and dynamically allocates resources between multiple implementations of the algorithm. The resource pool allocation library can cover multiple algorithm implementation entities. "Calculation" can be allocated between multiple implementation entities to achieve higher resource utilization efficiency. From the perspective of cloud service providers, the same hardware can support more users. From the user's perspective, higher performance can be achieved.

The presentation concludes by discussing the performance improvement achieved in HDFS Transparent Encryption using this method.
 ### Speakers: 
 <img src="https://img.bagevent.com/resource/20230617/2215411950.jpg" width="200" /><br>Guodong Xu: Linaro Ltd., Senior Tech Lead

- 2012-2023 Linaro Ltd.
  - Arm SVE/SVE2 optimization, software library optimization
  - Big data, Apache Bigtop
  - Kernel development
- 2008-2011 Flextronics Ltd, Software development lead
- 2002-2007 Motorola Mobile, Linux kernel device driver development

 <br><br>