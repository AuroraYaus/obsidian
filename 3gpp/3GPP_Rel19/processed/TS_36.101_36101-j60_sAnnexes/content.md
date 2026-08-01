# TS 36.101 36101-j60_sAnnexes

## Annex A (normative): Measurement channels

## A.1General

The throughput values defined in the measurement channels specified in Annex A, are calculated and are valid per datastream (codeword). For multi-stream (more than one codeword) transmissions, the throughput referenced in the minimum requirements is the sum of throughputs of all datastreams (codewords).

The UE category entry in the definition of the reference measurement channel in Annex A is only informative and reveals the UE categories, which can support the corresponding measurement channel. Whether the measurement channel is used for testing a certain UE category or not is specified in the individual minimum requirements.

## A.2UL reference measurement channels

## A.2.1General

The measurement channels in the following subclauses are defined to derive the requirements in clause 6 (Transmitter Characteristics) and clause 7 (Receiver Characteristics). The measurement channels represent example configurations of physical channels for different data rates.

## A.2.1.1Applicability and common parameters

The UL reference measurement channels comprise transmission of PUSCH and Demodulation Reference signals only. The following conditions apply:

-1 HARQ transmission

-Cyclic Prefix normal

-PUSCH hopping off

-Link adaptation off

-Demodulation Reference signal as per TS 36.211 [4] subclause 5.5.2.1.2.

Where ACK/NACK is transmitted, it is assumed to be multiplexed on PUSCH as per TS 36.212 [5] subclause 5.2.2.6.

-ACK/NACK 1 bit

-ACK/NACK mapping adjacent to Demodulation Reference symbol

-ACK/NACK resources punctured into data

-Max number of resources for ACK/NACK: 4 SC-FDMA symbols per subframe

-No CQI transmitted, no RI transmitted

## A.2.1.2Determination of payload size

The algorithm for determining the payload size A is as follows; given a desired coding rate R and radio block allocation NRB

1. Calculate the number of channel bits Nch that can be transmitted during the first transmission of a given sub-frame.

2. Find A such that the resulting coding rate is as close to R as possible, that is,

,

subject to

a) A is a valid TB size according to section 7.1.7 of TS 36.213 [6] assuming an allocation of NRB resource blocks.

b) C is the number of Code Blocks calculated according to section 5.1.2 of TS 36.212 [5].

c) For RMC-s, which at the nominal target coding rate do not cover all the possible UE categories for the given modulation, reduce the target coding rate gradually (within the same modulation), until the maximal possible number of UE categories is covered.

3. If there is more than one A that minimises the equation above, then the larger value is chosen per default and the chosen code rate should not exceed 0.93.

## A.2.1.3Overview of UL reference measurement channels

In Table A.2.1.3-1 to A.2.1.3-1K are listed the UL reference measurement channels specified in annexes A.2.2 and A.2.3 of this release of TS 36.101. This table is informative and serves only to a better overview. The reference for the concrete reference measurement channels and corresponding implementation’s parameters as to be used for requirements are annexes A.2.2 and A.2.3 as appropriate.

Table A.2.1.3-1: Overview of UL reference measurement channels (FDD, Full RB allocation, QPSK)

Table A.2.1.3-1A: Overview of UL reference measurement channels (FDD, Full RB allocation, 16-QAM)

Table A.2.1.3-1B: Overview of UL reference measurement channels (FDD, Full RB allocation, 64-QAM)

Table A.2.1.3-1Ba: Overview of UL reference measurement channels (FDD, Full RB allocation, 256-QAM)

Table A.2.1.3-1C: Overview of UL reference measurement channels (FDD, Partial RB allocation, QPSK)

Table A.2.1.3-1D: Overview of UL reference measurement channels (FDD, Partial RB allocation, 16-QAM)

Table A.2.1.3-1E: Overview of UL reference measurement channels (FDD, Partial RB allocation, 64-QAM)

Table A.2.1.3-1Ea: Overview of UL reference measurement channels (FDD, Partial RB allocation, 256-QAM)

Table A.2.1.3-1F: Overview of UL reference measurement channels (TDD, Full RB allocation, QPSK)

Table A.2.1.3-1G: Overview of UL reference measurement channels (TDD, Full RB allocation, 16-QAM)

Table A.2.1.3-1H: Overview of UL reference measurement channels (TDD, Full RB allocation, 64-QAM)

Table A.2.1.3-1Ha: Overview of UL reference measurement channels (TDD, Full RB allocation, 256-QAM)

Table A.2.1.3-1I: Overview of UL reference measurement channels (TDD, Partial RB allocation, QPSK)

Table A.2.1.3-1J: Overview of UL reference measurement channels (TDD, Partial RB allocation, 16-QAM)

Table A.2.1.3-1K: Overview of UL reference measurement channels (TDD, Partial RB allocation, 64-QAM)

Table A.2.1.3-1Ka: Overview of UL reference measurement channels (TDD, Partial RB allocation, 256-QAM)

Table A.2.1.3-1L: Overview of UL reference measurement channels (HD-FDD, NB-IoT, QPSK)

## A.2.2Reference measurement channels for FDD

## A.2.2.1Full RB allocation

## A.2.2.1.1QPSK

Table A.2.2.1.1-1: Reference Channels for QPSK with full RB allocation

Table A.2.2.1.1-1a: Reference Channels for QPSK with full/maximum RB allocation for UE UL category 0

Table A.2.2.1.1-1b: Reference Channels for QPSK with full/maximum RB allocation for UE UL category M1

Table A.2.2.1.1-1c: Reference Channels for QPSK with full/maximum RB allocation for UE UL category M2

## A.2.2.1.216-QAM

Table A.2.2.1.2-1: Reference Channels for 16-QAM with full RB allocation

Table A.2.2.1.2-1a: Reference Channels for 16-QAM with maximum RB allocation for UE UL category 0

Table A.2.2.1.2-1b: Reference Channels for 16-QAM with maximum RB allocation for UE UL category M1

Table A.2.2.1.2-1c: Reference Channels for 16-QAM with maximum RB allocation for UE UL category M2

## A.2.2.1.364-QAM

Table A.2.2.1.3-1: Reference Channels for 64-QAM with full RB allocation

## A.2.2.1.4256 QAM

Table A.2.2.1.4-1: Reference Channels for 256 QAM with full RB allocation

## A.2.2.2Partial RB allocation

For each channel bandwidth, various partial RB allocations are specified. The number of allocated RBs is chosen according to values specified in the Tx and Rx requirements. The single allocated RB case is included.

The allocated RBs are contiguous and start from one end of the channel bandwidth. A single allocated RB is at one end of the channel bandwidth.

## A.2.2.2.1QPSK

Table A.2.2.2.1-1: Reference Channels for QPSK with partial RB allocation

Table A.2.2.2.1-1a: Reference Channels for QPSK with partial RB allocation for UE UL category 0

Table A.2.2.2.1-1b: Reference Channels for QPSK with partial RB allocation for UE UL category M1

Table A.2.2.2.1-1c: Reference Channels for QPSK with partial RB allocation for UE UL category M2

## A.2.2.2.216-QAM

Table A.2.2.2.2-1 Reference Channels for 16-QAM with partial RB allocation

Table A.2.2.2.2-1a Reference Channels for 16-QAM with partial RB allocation for UE UL category 0

Table A.2.2.2.2-1b Reference Channels for 16-QAM with partial RB allocation for UE UL category M1

Table A.2.2.2.2-1c Reference Channels for 16-QAM with partial RB allocation for UE UL category M2

## A.2.2.2.364-QAM

Table A.2.2.2.3-1: Reference Channels for 64-QAM with partial RB allocation

## A.2.2.2.4256 QAM

Table A.2.2.2.4-1: Reference Channels for 256 QAM with partial RB allocation

## A.2.2.3Void

Table A.2.2.3-1: Void

## A.2.2.4subPRB allocation

The location of allocated RB for subPRB allocation is chosen according to values specified in the Tx requirements.

Table A.2.2.4-1: Reference Channels for SubPRB allocation

## A.2.3Reference measurement channels for TDD

For TDD, the measurement channel is based on DL/UL configuration ratio of 2DL:2UL. or 1DL:4UL. 2DL:2UL is the default and used unless explicitly specified in the test case

## A.2.3.1Full RB allocation

## A.2.3.1.1QPSK

Table A.2.3.1.1-1: Reference Channels for QPSK with full RB allocation

Table A.2.3.1.1-1A: Reference Channels for QPSK with full RB allocation, UL-DL configuration 0

Table A.2.3.1.1-1a: Reference Channels for QPSK with full/maximum RB allocation for UE UL category 0

Table A.2.3.1.1-1b: Reference Channels for QPSK with full/maximum RB allocation for UE UL category M1

Table A.2.3.1.1-1c: Reference Channels for QPSK with full/maximum RB allocation for UE UL category M2

## A.2.3.1.216-QAM

Table A.2.3.1.2-1: Reference Channels for 16-QAM with full RB allocation

Table A.2.3.1.2-1A: Reference Channels for 16-QAM with full RB allocation, UL-DL configuration 0

Table A.2.3.1.2-1a: Reference Channels for 16-QAM with maximum RB allocation for UE UL category 0

Table A.2.3.1.2-1b: Reference Channels for 16-QAM with maximum RB allocation for UE UL category M1

Table A.2.3.1.2-1c: Reference Channels for 16-QAM with maximum RB allocation for UE UL category M2

## A.2.3.1.364-QAM

Table A.2.3.1.3-1: Reference Channels for 64-QAM with full RB allocation

## A.2.3.1.4256 QAM

Table A.2.3.1.4-1: Reference Channels for 256 QAM with full RB allocation

## A.2.3.2Partial RB allocation

For each channel bandwidth, various partial RB allocations are specified. The number of allocated RBs is chosen according to values specified in the Tx and Rx requirements. The single allocated RB case is included.

The allocated RBs are contiguous and start from one end of the channel bandwidth. A single allocated RB is at one end of the channel bandwidth.

## A.2.3.2.1QPSK

Table A.2.3.2.1-1: Reference Channels for QPSK with partial RB allocation

Table A.2.3.2.1-1A: Reference Channels for QPSK with partial RB allocation, UL-DL configuration 0

Table A.2.3.2.1-1a: Reference Channels for QPSK with partial RB allocation for UE UL category 0

Table A.2.3.2.1-1b: Reference Channels for QPSK with partial RB allocation for UE UL category M1

Table A.2.3.2.1-1c: Reference Channels for QPSK with partial RB allocation for UE UL category M2

## A.2.3.2.216-QAM

Table A.2.3.2.2-1: Reference Channels for 16QAM with partial RB allocation

Table A.2.3.2.2-1A: Reference Channels for 16-QAM with partial RB allocation, UL-DL configuration 0

Table A.2.3.2.2-1a: Reference Channels for 16QAM with partial RB allocation UE UL category 0

Table A.2.3.2.2-1b: Reference Channels for 16QAM with partial RB allocation UE UL category M1

Table A.2.3.2.2-1c: Reference Channels for 16QAM with partial RB allocation UE UL category M2

## A.2.3.2.364-QAM

Table A.2.3.2.3-1: Reference Channels for 64-QAM with partial RB allocation

## A.2.3.2.4256 QAM

Table A.2.3.2.4-1: Reference Channels for 256 QAM with partial RB allocation

## A.2.3.3Void

Table A.2.3.3-1: Void

## A.2.3.4subPRB allocation

The location of allocated RB for subPRB allocation is chosen according to values specified in the Tx requirements.

Table A.2.3.4-1: Reference Channels for SubPRB allocation

## A.2.4Reference measurement channels for UE category NB1

Table A.2.4-1 Reference Channels for UE category NB1

Table A.2.4-2: NPDCCH configuration for NPUSCH format 1 scheduling

## A.2.5Reference measurement channels for LAA

## A.2.5.1Full RB allocation

## A.2.5.1.1QPSK

Table A.2.5.1.1-1: Reference Channels for QPSK with full RB allocation

## A.2.5.1.216QAM

Table A.2.5.1.2-1: Reference Channels for 16QAM with full RB allocation

## A.2.5.1.364QAM

Table A.2.5.1.3-1: Reference Channels for 64QAM with full RB allocation

## A.2.5.2Partial RB allocation

For each channel bandwidth, various partial RB allocations are specified. The number of allocated RBs is chosen according to values specified in the Tx and Rx requirements.

## A.2.5.2.1QPSK

Table A.2.5.2.1-1: Reference Channels for QPSK with partial RB allocation

## A.2.5.2.216QAM

Table A.2.5.2.2-1: Reference Channels for 16QAM with partial RB allocation

## A.2.5.2.364QAM

Table A.2.5.2.3-1: Reference Channels for 64QAM with partial RB allocation

## A.3DL reference measurement channels

## A.3.1General

The number of available channel bits varies across the sub-frames due to PBCH and PSS/SSS overhead. The payload size per sub-frame is varied in order to keep the code rate constant throughout a frame.

Unless otherwise stated, no user data is scheduled on subframes #5 in order to facilitate the transmission of system information blocks (SIB).

The algorithm for determining the payload size A is as follows; given a desired coding rate R and radio block allocation NRB

1. Calculate the number of channel bits Nch that can be transmitted during the first transmission of a given sub-frame.

2. Find A such that the resulting coding rate is as close to R as possible, that is,

,

subject to

a) A is a valid TB size according to section 7.1.7 of TS 36.213 [6] assuming an allocation of NRB resource blocks.

b) C is the number of Code Blocks calculated according to section 5.1.2 of TS 36.212 [5].

3. If there is more than one A that minimizes the equation above, then the larger value is chosen per default and the chosen code rate should not exceed 0.93.

4. For TDD, the measurement channel is based on DL/UL configuration ratio of 2DL+DwPTS (12 OFDM symbol): 2UL

## A.3.1.1Overview of DL reference measurement channels

In Table A.3.1.1-1 to A.3.1.1-1V are listed the DL reference measurement channels specified in annexes A.3.2 to A.3.15 of this release of TS 36.101. This table is informative and serves only to a better overview. The reference for the concrete reference measurement channels and corresponding implementation’s parameters as to be used for requirements are annexes A.3.2 to A.3.15 as appropriate.

Table A.3.1.1-1: Overview of DL reference measurement channels (FDD, Receiver requirements)

Table A.3.1.1-1A: Overview of DL reference measurement channels (TDD, Receiver requirements)

Table A.3.1.1-1B: Overview of DL reference measurement channels (FDD, Receiver requirements, Maximum input level)

Table A.3.1.1-1C: Overview of DL reference measurement channels (TDD, Receiver requirements, Maximum input level)

Table A.3.1.1-1D: Overview of DL reference measurement channels (FDD, PDSCH Performance, Single-antenna transmission (CRS))

Table A.3.1.1-1E: Overview of DL reference measurement channels (PDSCH Performance: Carrier aggregation with power imbalance)

Table A.3.1.1-1F: Overview of DL reference measurement channels (FDD, PDSCH Performance, Multi-antenna transmission (CRS))

Table A.3.1.1-1G: Overview of DL reference measurement channels (FDD, PDSCH Performance (UE specific RS))

Table A.3.1.1-1H: Overview of DL reference measurement channels (TDD, PDSCH Performance, Single-antenna transmission (CRS))

Table A.3.1.1-1I: Overview of DL reference measurement channels (TDD, PDSCH Performance, Multi-antenna transmission (CRS))

Table A.3.1.1-1J: Overview of DL reference measurement channels (TDD, PDSCH Performance (DRS))

Table A.3.1.1-1K: Overview of DL reference measurement channels (TDD, PDSCH Performance (UE specific RS))

Table A.3.1.1-1L: Overview of DL reference measurement channels (PDCCH / PCFICH Performance)

Table A.3.1.1-1M: Overview of DL reference measurement channels (PHICH Performance)

Table A.3.1.1-1N: Overview of DL reference measurement channels (PBCH Performance)

Table A.3.1.1-1O: Overview of DL reference measurement channels (PMCH Performance)

Table A.3.1.1-1P: Overview of DL reference measurement channels (Sustained data rate)

Table A.3.1.1-1Q: Overview of DL reference measurement channels (EPDCCH)

Table A.3.1.1-1R: Overview of DL reference measurement channels (MPDCCH)

Table A.3.1.1-1S: Overview of DL reference measurement channels (NPDSCH)

Table A.3.1.1-1T: Overview of DL reference measurement channels (NPDCCH)

Table A.3.1.1-1U: Overview of DL reference measurement channels (NPBCH)

Table A.3.1.1-1V: Overview of DL reference measurement channels (FS3)

Table A.3.1.1-1W: Overview of DL reference measurement channels (Slot-PDSCH/Subslot-PDSCH)

Table A.3.1.1-1X: Overview of DL reference measurement channels (SPDCCH)

Table A.3.1.1-1Y: Overview of DL reference measurement channels (PMCH)

## A.3.2Reference measurement channel for receiver characteristics

Unless otherwise stated, Tables A.3.2-1, A.3.2-1a, A.3.2-1b, A.3.2-2, A.3.2-2a and A.3.2-2b  are applicable for measurements on the Receiver Characteristics (clause 7) with the exception of subclause 7.4 (Maximum input level).

Unless otherwise stated, Tables A.3.2-3, A.3.2-3a, A.3.2-3b, A.3.2-4, A.3.2-4a and A.3.2-4b are applicable for subclause 7.4 (Maximum input level).

Unless otherwise stated, Tables A.3.2-1, A.3.2-1a, A.3.2-1b, A.3.2-2, A.3.2-2a and A.3.2-2b also apply for the modulated interferer used in Clauses 7.5, 7.6 and 7.8 with test specific bandwidths.

For transmissions in TDD Band 46, Table A.3.2-2c is applicable for measurements of Receiver Characteristics (clause 7) except for the Maximum Input Level (clause 7.4A) for which Table A.3.2-4d and Table A.3.2-7 apply. For these measurements, the discovery signals measurement timing configuration (DMTC) periodicity shall be set at dmtc-Periodicity = 40 ms with an offset dmtc-Offset = 0 for the channel and the DRS shall be transmitted in the first subframe of each DMTC occasion. Furthermore, no PBCH is transmitted and the PDSCH is also scheduled in subframe #5.

Table A.3.2-1 Fixed Reference Channel for Receiver Requirements (FDD)

Table A.3.2-1a Fixed Reference Channel for Receiver Requirements (FDD)

Table A.3.2-1b Fixed Reference Channel for Receiver Requirements (FDD and HD-FDD) – for CAT-M1

Table A.3.2-1c Fixed Reference Channel for Receiver Requirements (HD-FDD) without repetition – for CAT-NB1

Table A.3.2-1d: Void

Table A.3.2-1e: General configuration for CAT-NB1

Table A.3.2-1f: NPDCCH configuration for NPDSCH scheduling

Table A.3.2-1g: NPUSCH format 2 configurations for NPDSCH scheduling

Table A.3.2-1h: Fixed Reference Channel for Receiver Requirements (FDD and HD-FDD) – for CAT-M2

Table A.3.2-2 Fixed Reference Channel for Receiver Requirements (TDD)

Table A.3.2-2a Fixed Reference Channel for Receiver Requirements (TDD)

Table A.3.2-2b Fixed Reference Channel for Receiver Requirements (TDD) – for CAT-M1

Table A.3.2-2c Fixed Reference Channel for Receiver Requirements (TDD Band 46)

Table A.3.2-2d: Fixed Reference Channel for Receiver Requirements (TDD) – for CAT-M2

Table A.3.2-2e Fixed Reference Channel for Receiver Requirements (TDD) – for CAT-NB1 and CAT-NB2

Table A.3.2-3 Fixed Reference Channel for Maximum input level for UE Categories ≥ 3(FDD)

Table A.3.2-3a Fixed Reference Channel for Maximum input level for UE Category 1 (FDD)

Table A.3.2-3b Fixed Reference Channel for Maximum input level for UE Category 2 (FDD)

Table A.3.2-3c Fixed Reference Channel for Maximum input level for UE DL Category 0 (FDD)

Table A.3.2-3d Fixed Reference Channel for Maximum input level for UE DL Category M1 (FDD and HD-FDD)

Table A.3.2-3e: Fixed Reference Channel for Maximum input level for UE DL Category M2 (FDD and HD-FDD)

Table A.3.2-4 Fixed Reference Channel for Maximum input level for UE Categories ≥ 3 (TDD)

Table A.3.2-4a Fixed Reference Channel for Maximum input level for UE Category 1 (TDD)

Table A.3.2-4b Fixed Reference Channel for Maximum input level for UE Category 2 (TDD)

Table A.3.2-4c Fixed Reference Channel for Maximum input level for UE DL Category 0 (TDD)

Table A.3.2-4d Fixed Reference Channel for Maximum input level for UE Categories ≥ 3 (TDD Band 46)

Table A.3.2-4e Fixed Reference Channel for Maximum input level for UE DL Category M1 (TDD)

Table A.3.2-4f: Fixed Reference Channel for Maximum input level for UE DL Category M2 (TDD)

Table A.3.2-5 Fixed Reference Channel for Maximum input level for UE Categories 11/12 and UE DL categories ≥ 11 (FDD)

Table A.3.2-6 Fixed Reference Channel for Maximum input level for UE Categories 11/12 and UE DL categories ≥ 11 (TDD)

Table A.3.2-7 Fixed Reference Channel for Maximum input level for UE Categories 11/12 and UE DL categories ≥ 11 (TDD Band 46)

Table A.3.2-8 Fixed Reference Channel for Maximum input level for UE DL category 20 and UE DL categories ≥ 22 (FDD)

Table A.3.2-9 Fixed Reference Channel for Maximum input level for UE DL category 20 and UE DL categories ≥ 22 (TDD)

Table A.3.2-10 Fixed Reference Channel for Maximum input level for UE DL category 20 and UE DL categories ≥ 22 (TDD Band 46)

## A.3.3Reference measurement channels for PDSCH performance requirements (FDD)

## A.3.3.1Single-antenna transmission (Common Reference Symbols)

Table A.3.3.1-1: Fixed Reference Channel QPSK R=1/3

Table A.3.3.1-2: Fixed Reference Channel 16QAM R=1/2

Table A.3.3.1-3: Fixed Reference Channel 64QAM R=3/4

Table A.3.3.1-3a: Fixed Reference Channel 64QAM R=3/4

Table A.3.3.1-4: Fixed Reference Channel Single PRB (Channel Edge)

Table A.3.3.1-5: Fixed Reference Channel Single PRB (MBSFN Configuration)

Table A.3.3.1-6: Fixed Reference Channel QPSK R=1/10

Table A.3.3.1-7: Fixed Reference Channel for CA demodulation with power imbalance

## A.3.3.2Multi-antenna transmission (Common Reference Symbols)

## A.3.3.2.1Two antenna ports

Table A.3.3.2.1-1: Fixed Reference Channel two antenna ports

Table A.3.3.2.1-2: Fixed Reference Channel two antenna ports

Table A.3.3.2.1-3: Fixed Reference Channel two antenna ports

Table A.3.3.2.1-4: Fixed Reference Channel two antenna ports

Table A.3.3.2.1-5: Fixed Reference Channel two antenna ports

Table A.3.3.2.1-6: Fixed Reference Channel two antenna ports

Table A.3.3.2.1-7: Fixed Reference Channel two antenna ports

Table A.3.3.2.1-8: Fixed Reference Channel two antenna ports

Table A.3.3.2.1-9: Fixed Reference Channel two antenna ports

## A.3.3.2.2Four antenna ports

Table A.3.3.2.2-1: Fixed Reference Channel four antenna ports

Table A.3.3.2.2-2: Fixed Reference Channel four antenna ports

Table A.3.3.2.2-3: Fixed Reference Channel four antenna ports

Table A.3.3.2.2-4: Fixed Reference Channel four antenna ports

## A.3.3.3Reference Measurement Channel for UE-Specific Reference Symbols

## A.3.3.3.0Two antenna ports (no CSI-RS)

The reference measurement channels in Table A.3.3.3.0-1 apply with two CRS antenna ports and without CSI-RS.

Table A.3.3.3.0-1: Fixed Reference Channel without CSI-RS

The reference measurement channels in Table A.3.3.3.0-2 apply for verifying demodulation performance for UE-specific reference symbols without CSI-RS.

Table A.3.3.3.0-2: Fixed Reference Channel without CSI-RS

## A.3.3.3.1Two antenna port (CSI-RS)

The reference measurement channels in Table A.3.3.3.1-1 apply for verifying demodulation performance for UE-specific reference symbols with two cell-specific antenna ports and two CSI-RS antenna ports.

Table A.3.3.3.1-1: Fixed Reference Channel for CDM-multiplexed DM RS with two CSI-RS antenna ports

The reference measurement channels in Table A3.3.3.1-2 apply for verifying demudlation performance for UE-specific reference symbols with two cell specific antenna ports and two CSI-RS antenna ports with ZP CSI-RS and NZP CSI-RS in same subframe.

Table A.3.3.3.1-2: Fixed Reference Channel for CDM-multiplexed DM RS with two CSI-RS antenna ports with ZP CSI-RS and NZP CSI-RS

Table A.3.3.3.1-3: Fixed Reference Channel for CDM-multiplexed DM RS with two CSI-RS antenna ports

## A.3.3.3.2Four antenna ports (CSI-RS)

The reference measurement channels in Table A.3.3.3.2-1 apply for verifying demodulation performance for UE-specific reference symbols with two cell-specific antenna ports and four CSI-RS antenna ports.

Table A.3.3.3.2-1: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports

The reference measurement channels in Table A.3.3.3.2-2 apply for verifying FDD PMI accuracy measurement and CRI accuracy measurement with two CRS antenna ports and four CSI-RS antenna ports.

Table A.3.3.3.2-2: Fixed Reference Channel for four antenna ports (CSI-RS)

The reference measurement channels in Table A.3.3.3.2-3 apply for verifying demodulation performance for UE-specific reference symbols with two cell-specific antenna ports and four CSI-RS antenna ports.

Table A.3.3.3.2-3: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports

The reference measurement channels in Table A.3.3.3.2-4 apply with two CRS antenna ports and four CSI-RS antenna ports.

Table A.3.3.3.2-4: Fixed Reference Channel for four antenna ports (CSI-RS)

The reference measurement channels in Table A.3.3.3.2-5 apply with two CRS antenna ports and four CSI-RS antenna ports.

Table A.3.3.3.2-5: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports with ZP CSI-RS and NZP CSI-RS

The reference measurement channels in Table A.3.3.3.2-6 apply with four CRS antenna ports and four CSI-RS antenna ports.

Table A.3.3.3.2-6: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports with ZP CSI-RS and NZP CSI-RS

## A.3.3.3.2AEight antenna ports (CSI-RS)

The reference measurement channels in Table A.3.3.3.2A-1 apply for verifying FDD CRI accuracy measurement with two CRS antenna ports and eight CSI-RS antenna ports.

Table A.3.3.3.2A-1: Fixed Reference Channel for eight antenna ports (CSI-RS)

Table A.3.3.3.2A-2: Fixed Reference Channel for eight antenna ports (CSI-RS)

## A.3.3.3.3Twelve antenna port (CSI-RS)

The reference measurement channels in Table A.3.3.3.3-1 apply for verifying PMI accuracy performance for UE-specific reference symbols with two cell-specific antenna ports and twelve CSI-RS antenna ports.

Table A.3.3.3.3-1: Fixed Reference Channel for CDM-multiplexed DM RS with twelve CSI-RS antenna ports

## A.3.3.3.4Sixteen antenna port (CSI-RS)

The reference measurement channels in Table A.3.3.3.4-1 apply for verifying PMI accuracy performance for UE-specific reference symbols with two cell-specific antenna ports and sixteen CSI-RS antenna ports.

Table A.3.3.3.4-1: Fixed Reference Channel for CDM-multiplexed DM RS with sixteen CSI-RS antenna ports

## A.3.3.3.5Twenty-four antenna port (CSI-RS)

The reference measurement channels in Table A.3.3.3.5-1 apply for verifying PMI accuracy performance for UE-specific reference symbols with two cell-specific antenna ports and twenty-four CSI-RS antenna ports.

Table A.3.3.3.5-1: Fixed Reference Channel for CDM-multiplexed DM RS with twenty-four CSI-RS antenna ports

## A.3.3.3.6Thirty-two antenna port (CSI-RS)

The reference measurement channels in Table A.3.3.3.6-1 apply for verifying PMI accuracy performance for UE-specific reference symbols with two cell-specific antenna ports and thirty-two CSI-RS antenna ports.

Table A.3.3.3.6-1: Fixed Reference Channel for CDM-multiplexed DM RS with thirty-two CSI-RS antenna ports

## A.3.4Reference measurement channels for PDSCH performance requirements (TDD)

## A.3.4.1Single-antenna transmission (Common Reference Symbols)

Table A.3.4.1-1: Fixed Reference Channel QPSK R=1/3

Table A.3.4.1-2: Fixed Reference Channel 16QAM R=1/2

Table A.3.4.1-3: Fixed Reference Channel 64QAM R=3/4

Table A.3.4.1-3a: Fixed Reference Channel 64QAM R=3/4

Table A.3.4.1-4: Fixed Reference Channel Single PRB

Table A.3.4.1-5: Fixed Reference Channel Single PRB (MBSFN Configuration)

Table A.3.4.1-6: Fixed Reference Channel QPSK R=1/10

Table A.3.4.1-7: Fixed Reference Channel for CA demodulation with power imbalance

## A.3.4.2Multi-antenna transmission (Common Reference Signals)

## A.3.4.2.1Two antenna ports

Table A.3.4.2.1-1: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-2: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-3: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-4: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-5: Fixed Reference Channel two antenna ports when EIMTA-MainConfigServCell-r12 is configured

Table A.3.4.2.1-6: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-7: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-8: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-9: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-10: Fixed Reference Channel two antenna ports

Table A.3.4.2.1-11: Fixed Reference Channel two antenna ports

## A.3.4.2.2Four antenna ports

Table A.3.4.2.2-1: Fixed Reference Channel four antenna ports

Table A.3.4.2.2-2: Fixed Reference Channel four antenna ports

Table A.3.4.2.2-3: Fixed Reference Channel four antenna ports

Table A.3.4.2.2-4: Fixed Reference Channel four antenna ports

## A.3.4.3Reference Measurement Channels for UE-Specific Reference Symbols

## A.3.4.3.1Single antenna port (Cell Specific)

The reference measurement channels in Table A.3.4.3.1-1 apply for verifying demodulation performance for UE-specific reference symbols with one cell-specific antenna port.

Table A.3.4.3.1-1: Fixed Reference Channel for DRS

The reference measurement channels in Table A.3.4.3.1-2 apply for verifying demodulation performance for UE-specific reference symbols with one cell-specific antenna port.

Table A.3.4.3.1-2: Fixed Reference Channel for DRS

## A.3.4.3.2Two antenna ports (Cell Specific)

The reference measurement channels in Table A.3.4.3.2-1 apply for verifying demodulation performance for CDM-multiplexed UE specific reference symbols with two cell-specific antenna ports.

Table A.3.4.3.2-1: Fixed Reference Channel for CDM-multiplexed DM RS

The reference measurement channels in Table A.3.4.3.2-2 apply with two CRS antenna ports.

Table A.3.4.3.2-2: Fixed Reference Channel for CDM-multiplexed DM RS

## A.3.4.3.3Two antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.3-1 apply for verifying demodulation performance for CDM-multiplexed UE specific reference symbols with two cell-specific antenna ports and two CSI-RS antenna ports.

Table A.3.4.3.3-1: Fixed Reference Channel for CDM-multiplexed DM RS with two CSI-RS antenna ports

The reference measurement channels in Table A3.4.3.3-2 apply for verifying demudlation performance for UE-specific reference symbols with two cell specific antenna ports and two CSI-RS antenna ports with ZP CSI-RS and NZP CSI-RS in same subframe.

Table A.3.4.3.3-2: Fixed Reference Channel for CDM-multiplexed DM RS with two CSI-RS antenna ports with ZP CSI-RS and NZP CSI-RS

Table A.3.4.3.3-3: Fixed Reference Channel for CDM-multiplexed DM RS with two CSI-RS antenna ports

## A.3.4.3.4Four antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.4-1 apply for verifying demodulation performance for CDM-multiplexed UE specific reference symbols with two cell-specific antenna ports and four CSI-RS antenna ports.

Table A.3.4.3.4-1: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports

The reference measurement channels in Table A.3.4.3.4-2 apply for verifying TDD PMI accuracy measurement with two CRS antenna ports and four CSI-RS antenna ports.

Table A.3.4.3.4-2: Fixed Reference Channel for four antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.4-3 apply for verifying demodulation performance for CDM-multiplexed UE specific reference symbols with two cell-specific antenna ports and four CSI-RS antenna ports.

Table A.3.4.3.4-3: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports

The reference measurement channels in Table A.3.4.3.4-4 apply for verifying demodulation performance for CDM-multiplexed UE specific reference symbols with two cell-specific antenna ports and four CSI-RS antenna ports.

Table A.3.4.3.4-4: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports

The reference measurement channels in Table A.3.4.3.4-5 apply for verifying CRI reporting accuracy with two cell-specific antenna ports and four CSI-RS antenna ports.

Table A.3.3.3.4-5: Fixed Reference Channel for four antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.4-6 apply with two CRS antenna ports and four CSI-RS antenna ports.

Table A.3.4.3.4-6: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports with ZP CSI-RS and NZP CSI-RS

The reference measurement channels in Table A.3.4.3.4-7 apply with four CRS antenna ports and four CSI-RS antenna ports.

Table A.3.4.3.4-7: Fixed Reference Channel for CDM-multiplexed DM RS with four CSI-RS antenna ports with ZP CSI-RS and NZP CSI-RS

## A.3.4.3.5Eight antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.5-1 apply for verifying demodulation performance for CDM-multiplexed UE specific reference symbols with two cell-specific antenna ports and eight CSI-RS antenna ports.

Table A.3.4.3.5-1: Fixed Reference Channel for CDM-multiplexed DM RS with eight CSI-RS antenna ports

The reference measurement channels in Table A.3.4.3.5-2 apply for verifying TDD PMI accuracy measurement with two CRS antenna ports and eight CSI-RS antenna ports.

Table A.3.4.3.5-2: Fixed Reference Channel for eight antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.5-3 apply for verifying CRI reporting accuracy with two cell-specific antenna ports and four CSI-RS antenna ports.

Table A.3.4.3.5-3: Fixed Reference Channel for eight antenna ports (CSI-RS)

Table A.3.4.3.5-4: Fixed Reference Channel for eight antenna ports (CSI-RS)

## A.3.4.3.6Twelve antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.6-1 apply for verifying TDD PMI accuracy measurement with two CRS antenna ports and twelve CSI-RS antenna ports.

Table A.3.4.3.6-1: Fixed Reference Channel for twelve antenna ports (CSI-RS)

## A.3.4.3.7Sixteen antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.7-1 apply for verifying TDD PMI accuracy measurement with two CRS antenna ports and sixteen CSI-RS antenna ports.

Table A.3.4.3.7-1: Fixed Reference Channel for sixteen antenna ports (CSI-RS)

## A.3.4.3.8Twenty-four antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.8-1 apply for verifying TDD PMI accuracy measurement with two CRS antenna ports and twenty-four CSI-RS antenna ports.

Table A.3.4.3.8-1: Fixed Reference Channel for twenty-four antenna ports (CSI-RS)

## A.3.4.3.9Thirty-two antenna ports (CSI-RS)

The reference measurement channels in Table A.3.4.3.9-1 apply for verifying TDD PMI accuracy measurement with two CRS antenna ports and thirty-two CSI-RS antenna ports.

Table A.3.4.3.9-1: Fixed Reference Channel for thirty-two antenna ports (CSI-RS)

## A.3.5Reference measurement channels for PDCCH/PCFICH performance requirements

## A.3.5.1FDD

Table A.3.5.1-1: Reference Channel FDD

Table A.3.5.1-2: Void

## A.3.5.2TDD

Table A.3.5.2-1: Reference Channel TDD

Table A.3.5.2-2: Void

## A.3.5.3LAA

Table A.3.5.3-1: Reference Channel for FS3 with FDD primary cell

Table A.3.5.3-2: Reference Channel for FS3 with TDD primary cell

## A.3.6Reference measurement channels for PHICH performance requirements

Table A.3.6-1: Reference Channel FDD/TDD

## A.3.7Reference measurement channels for PBCH performance requirements

Table A.3.7-1: Reference Channel FDD/TDD

## A.3.8Reference measurement channels for MBMS performance requirements

## A.3.8.1FDD

Table A.3.8.1-1: Fixed Reference Channel QPSK R=1/3

Table A.3.8.1-2: Fixed Reference Channel 16QAM R=1/2

Table A.3.8.1-3: Fixed Reference Channel 64QAM R=2/3

Table A.3.8.1-4: Fixed Reference Channel for subcarrier spacing 1.25kHz with FeMBMS MBMS/Unicast-mixed cell

Table A.3.8.1-5: Fixed Reference Channel for subcarrier spacing 7.5kHz with FeMBMS MBMS/Unicast-mixed cell

Table A.3.8.1-6: Fixed Reference Channel for subcarrier spacing 1.25kHz with MBMS dedicated cell

Table A.3.8.1-7: Fixed Reference Channel for subcarrier spacing 7.5kHz with with MBMS dedicated cell

Table A.3.8.1-8: Fixed Reference Channel for subcarrier spacing 15kHz with with MBMS dedicated cell

Table A.3.8.1-9: Fixed Reference Channel for subcarrier spacing 0.37 kHz with LTE based 5G terrestrial broadcast MBMS dedicated cell

Table A.3.8.1-10: Fixed Reference Channel for subcarrier spacing 2.5 kHz with LTE based 5G terrestrial broadcast MBMS dedicated cell

Table A.3.8.1-11: Fixed Reference Channel for subcarrier spacing 1.25 kHz with LTE based 5G terrestrial broadcast MBMS dedicated cell with time-frequency interleaving

## A.3.8.2TDD

Table A.3.8.2-1: Fixed Reference Channel QPSK R=1/3

Table A.3.8.2-2: Fixed Reference Channel 16QAM R=1/2

Table A.3.8.2-3: Fixed Reference Channel 64QAM R=2/3

## A.3.9Reference measurement channels for sustained downlink data rate provided by lower layers

## A.3.9.1FDD

Table A.3.9.1-1: Fixed Reference Channel for sustained data-rate test (FDD 64QAM)

Table A.3.9.1-2: Fixed Reference Channel for sustained data-rate test (FDD 64QAM)

Table A.3.9.1-3: Fixed Reference Channel for sustained data-rate test (FDD 256QAM)

Table A.3.9.1-4: Fixed Reference Channel for sustained data-rate test (FDD 1024QAM)

## A.3.9.2TDD

Table A.3.9.2-1: Fixed Reference Channel for sustained data-rate test (TDD 64QAM)

Table A.3.9.2-1A: Fixed Reference Channel for sustained data-rate test (TDD 64QAM)

Table A.3.9.2-2: Fixed Reference Channel for sustained data-rate test (TDD 256QAM)

Table A.3.9.2-3: Fixed Reference Channel for sustained data-rate test (TDD 256QAM)

Table A.3.9.2-4: Fixed Reference Channel for sustained data-rate test (TDD 1024QAM)

## A.3.9.3FDD (EPDCCH scheduling)

Table A.3.9.3-1: Fixed Reference Channel for sustained data-rate test with EPDCCH scheduling (FDD)

## A.3.9.4TDD (EPDCCH scheduling)

Table A.3.9.4-1: Fixed Reference Channel for sustained data-rate with EPDCCH scheduling (TDD)

## A.3.9.5LAA

Table A.3.9.5-1: Fixed Reference Channel for sustained data-rate test (FS3 64QAM)

Table A.3.9.5-2: Fixed Reference Channel for sustained data-rate test (FS3 256QAM)

## A.3.10Reference Measurement Channels for EPDCCH performance requirements

## A.3.10.1FDD

Table A.3.10.1-1: Reference Channel FDD

## A.3.10.2TDD

Table A.3.10.2-1: Reference Channel TDD

## A.3.11Reference Measurement Channels for MPDCCH performance requirements

## A.3.11.1FDD and half-duplex FDD

Table A.3.11.1-1: Reference Channel FDD and half-duplex FDD

## A.3.11.2TDD

Table A.3.11.2-1: Reference Channel TDD

## A.3.12Reference measurement channels for NPDSCH performance requirements

## A.3.12.1In-band

## A.3.12.1.2Two-antenna transmission

Table A.3.12.1.2-1: NPDSCH Reference Channel with 2 TX Antennas for FDD

Table A.3.12.1.2-2: NPDSCH Reference Channel with 2 TX Antennas for TDD

## A.3.12.2Standalone/Guard-band

## A.3.12.2.1 Single-antenna transmission

Table A.3.12.2.1-1: NPDSCH Reference Channel with 1Tx Antenna for UE Category NB1 and NB2 for FDD

Table A.3.12.2.1-1a: NPDSCH Reference Channel with 1Tx Antenna for UE Category NB1 and NB2 for TDD

Table A.3.12.2.1-2: NPDSCH Reference Channel with 1Tx Antenna for UE Category NB2 for FDD

Table A.3.12.2.1-2a: NPDSCH Reference Channel with 1Tx Antenna for UE Category NB2 for TDD

## A.3.13Reference measurement channels for NPDCCH performance requirements

## A.3.13.1Half-duplex FDD

Table A.3.13.1-1: NPDCCH Reference Channel for Category NB1 UE

## A.3.13.2TDD

Table A.3.13.2-1: NPDCCH Reference Channel for Category NB1 UE

## A.3.14Reference measurement channels for NPBCH performance requirements for Cat NB1 UEs

Table A.3.14-1: NPBCH Reference Channel for Category NB1 UE

## A.3.15Reference Measurement Channels for LAA SCell with frame structure Type-3

## A.3.15.1Multi-antenna transmission (Common Reference Symbols)

## A.3.15.1.1Four antenna ports

Table A.3.15.1.1-2: Reference Channel with four CRS ports

## A.3.15.2Reference Measurement Channel for UE-Specific Reference Symbols

## A.3.15.2.1Two antenna ports (CSI-RS)

The reference measurement channels in Table A.3.15.2.1-1 apply for verifying demodulation performance for UE-specific reference symbols with two cell-specific antenna ports and two CSI-RS antenna ports for LAA SCell.

Table A.3.15.2.1-1: Reference Channel with two CRS ports

Table A.3.15-2: Void

## A.3.16Reference measurement channels for Slot-PDSCH and Subslot-PDSCH performance requirements

## A.3.16.1FDD

Table A.3.16.1-1: Fixed Reference Channel Slot-PDSCH (Cell-Specific Reference Signals)

Table A.3.16.1-2: Fixed Reference Channel Subslot-PDSCH (Cell-Specific Reference Signals)

Table A.3.16.1-3: Fixed Reference Channel Slot-PDSCH (User-Specific Reference Signals)

Table A.3.16.1-4: Fixed Reference Channel Subslot-PDSCH (User-Specific Reference Signals)

## A.3.16.2TDD

Table A.3.16.2-1: Fixed Reference Channel Slot-PDSCH (Cell-Specific Reference Signals)

Table A.3.16.2-2: Fixed Reference Channel Slot-PDSCH (User-Specific Reference Signals)

## A.3.17Reference measurement channels for SPDCCH performance requirements

## A.3.17.1FDD

Table A.3.17.1-1: Reference Channel FDD

## A.3.17.2TDD

Table A.3.17.2-1: Reference Channel TDD

## A.3.18Reference Measurement Channels for LTE based 5G broadcast PMCH receiver requirements

## A.3.18.1SDO

Table A.3.18.1-1 Fixed Reference Channel for PMCH Receiver Requirements (15 kHz SCS)

Table A.3.18.1-2 Fixed Reference Channel for PMCH Receiver Requirements (2.5 kHz SCS)

Table A.3.18.1-3 Fixed Reference Channel for PMCH Receiver Requirements (1.25 kHz SCS)

Table A.3.18.1-4 Fixed Reference Channel for PMCH Receiver Requirements (0.37 kHz SCS)

## A.4CSI reference measurement channels

This section defines the DL signal applicable to the reporting of channel status information (Clause 9.2, 9.3 and 9.5).

In Table A.4-1 are specified the reference channels. Table A.4-13 specifies the mapping of CQI index to modulation coding scheme, which complies with the CQI definition specified in Section 7.2.3 of [6].

Table A.4-0: Void

Table A.4-1: CSI reference measurement channels

Table A.4-1a: Void

Table A.4-1b: Void

Table A.4-1c: Void

Table A.4-1d: Void

Table A.4-1e: Void

Table A.4-2: Void

Table A.4-2a: Void

Table A.4-2b: Void

Table A.4-2c: Void

Table A.4-2d: Void

Table A.4-2e: Void

Table A.4-3: Void

Table A.4-3a: Void

Table A.4-3b: Void

Table A.4-3c: Void

Table A.4-3d: Void

Table A.4-3e: Void

Table A.4-3f: Void

Table A.4-3g: Void

Table A.4-3h: Void

Table A.4-3i: Void

Table A.4-3j: Void

Table A.4-3k: Void

Table A.4-3l: Void

Table A.4-3m: Void

Table A.4-4: Void

Table A.4-4a: Void

Table A.4-4b: Void

Table A.4-5: Void

Table A.4-5a: Void

Table A.4-5b: Void

Table A.4-6: Void

Table A.4-6a: Void

Table A.4-6b: Void

Table A.4-6c: Void

Table A.4-6d: Void

Table A.4-6e: Void

Table A.4-6f: Void

Table A.4-7: Void

Table A.4-8: Void

Table A.4-9: Void

Table A.4-10: Void

Table A.4-11: Void

Table A.4-12: Void

Table A.4-13: Mapping of CQI Index to Modulation coding scheme (MCS)

Table A.4-14: Mapping of CQI Index to Modulation coding scheme (Modulation and TBS index Table 2 and 4-bit CQI Table 2 are used)

Table A.4-15: Mapping of CQI Index to Modulation coding scheme (Modulation and TBS index Table 2 and 4-bit CQI Table 2 are used)

Table A.4-16: Mapping of CQI Index to Modulation coding scheme (Modulation and TBS indx Table 3)

Table A.4-17: Mapping of CQI Index to Modulation coding scheme (Slot-PDSCH)

Table A.4-18: Mapping of CQI Index to Modulation coding scheme (Subslot-PDSCH)

Table A.4-19: Mapping of CQI Index to Modulation coding scheme (4-bit CQI Table 5)

Table A.4-20: Mapping of CQI Index to Modulation coding scheme (4-bit CQI Table 6)

Table A.4-21: Mapping of CQI Index to Modulation coding scheme (Modulation and TBS index Table 3 and 4-bit CQI Table 4)

Table A.4-22: Mapping of channel quality reported value to Modulation coding scheme

## A.5OFDMA Channel Noise Generator (OCNG)

## A.5.1OCNG Patterns for FDD

The following OCNG patterns are used for modelling allocations to virtual UEs (which are not under test) and/or allocations used for MBSFN. The OCNG pattern for each sub frame specifies the allocations that shall be filled with OCNG, and furthermore, the relative power level of each such allocation.

In each test case the OCNG is expressed by parameters OCNG_RA and OCNG_RB which together with a relative power level () specifies the PDSCH EPRE-to-RS EPRE ratios in OFDM symbols with and without reference symbols, respectively. The relative power, which is used for modelling boosting per virtual UE allocation, is expressed by:

where  denotes the relative power level of the i:th virtual UE. The parameter settings of OCNG_RA, OCNG_RB, and the set of relative power levels are chosen such that when also taking allocations to the UE under test into account, as given by a PDSCH reference channel, a constant transmitted power spectral density that is constant on an OFDM symbol basis is targeted.

Moreover the OCNG pattern is accompanied by a PCFICH/PDCCH/PHICH reference channel which specifies the control region. For any aggregation and PHICH allocation, the PDCCH and any unused PHICH groups are padded with resource element groups with a power level given respectively by PDCCH_RA/RB and PHICH_RA/RB as specified in the test case such that a total power spectral density in the control region that is constant on an OFDM symbol basis is targeted.

For the performance requirements of UE with the CA capability, the OCNG patterns apply for each CC.

## A.5.1.1OCNG FDD pattern 1: One sided dynamic OCNG FDD pattern

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is continuous in frequency domain (one sided).

Table A.5.1.1-1: OP.1 FDD: One sided dynamic OCNG FDD Pattern

## A.5.1.2OCNG FDD pattern 2: Two sided dynamic OCNG FDD pattern

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is discontinuous in frequency domain (divided in two parts by the allocated area – two sided), starts with PRB 0 and ends with PRB .

Table A.5.1.2-1: OP.2 FDD: Two sided dynamic OCNG FDD Pattern

## A.5.1.3OCNG FDD pattern 3: 49 RB OCNG allocation with MBSFN in 10 MHz

Table A.5.1.3-1: OP.3 FDD: OCNG FDD Pattern 3

## A.5.1.3AOCNG FDD pattern 3A: 49 RB OCNG allocation with MBSFN enhancement in 10 MHz

Table A.5.1.3A-1: OP.3A FDD: OCNG FDD Pattern 3A

## A.5.1.4OCNG FDD pattern 4: One sided dynamic OCNG FDD pattern for MBMS transmission

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is continuous in frequency domain (one sided) and MBMS performance is tested.

Table A.5.1.4-1: OP.4 FDD: One sided dynamic OCNG FDD Pattern for MBMS transmission

## A.5.1.4AOCNG FDD pattern 4A: One sided dynamic OCNG FDD pattern for enhanced MBMS transmission

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is continuous in frequency domain (one sided) and MBMS performance is tested.

Table A.5.1.4A-1: OP.4A FDD: One sided dynamic OCNG FDD Pattern for MBMS transmission

## A.5.1.5OCNG FDD pattern 5: One sided dynamic 16QAM modulated OCNG FDD pattern

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of DL sub-frames, when the unallocated area is continuous in the frequency domain (one sided).

Table A.5.1.5-1: OP.5 FDD: One sided dynamic 16QAM modulated OCNG FDD Pattern

## A.5.1.6OCNG FDD pattern 6: dynamic OCNG FDD pattern when user data is in 2 non-contiguous blocks

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is discontinuous in frequency domain (divided in two parts by the first allocated block). The second allocated block ends with PRB .

Table A.5.1.6-1: OP.6 FDD: OCNG FDD Pattern when user data is in 2 non-contiguous blocks

A.5.1.7OCNG FDD pattern 7: dynamic OCNG FDD pattern when user data is in multiple non-contiguous blocks

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data, EPDCCH or system information) of the DL sub-frames, when the unallocated area is discontinuous in frequency domain (divided in multiple parts by the M allocated blocks for data transmission). The m-th allocated block starts with RPB  and ends with PRB , where m = 1, …, M. The system bandwidth starts with RPB 0 and ends with.

Table A.5.1.7-1: OP.7 FDD: OCNG FDD Pattern when user data is in multiple non-contiguous blocks

## A.5.1.8OCNG FDD pattern 8: Dynamic OCNG FDD pattern for TM10 transmission

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is discontinuous in frequency domain where there are M unallocated PRB blocks labled from 1-st block to M-th block (M>1) and the m-th block starts with PRB and end with PRB , or when the unallocated area is continuous in frequency domain where M =1  (one sided). The system bandwidth starts with RPB 0 and ends with. should be equal to or less than .

Table A.5.1.8-1: OP.8 FDD: Dynamic OCNG FDD Pattern

## A.5.2OCNG Patterns for TDD

The following OCNG patterns are used for modelling allocations to virtual UEs (which are not under test). The OCNG pattern for each sub frame specifies the allocations that shall be filled with OCNG, and furthermore, the relative power level of each such allocation.

In each test case the OCNG is expressed by parameters OCNG_RA and OCNG_RB which together with a relative power level () specifies the PDSCH EPRE-to-RS EPRE ratios in OFDM symbols with and without reference symbols, respectively. The relative power, which is used for modelling boosting per virtual UE allocation, is expressed by:

where  denotes the relative power level of the i:th virtual UE. The parameter settings of OCNG_RA, OCNG_RB, and the set of relative power levels are chosen such that when also taking allocations to the UE under test into account, as given by a PDSCH reference channel, a transmitted power spectral density that is constant on an OFDM symbol basis is targeted.

Moreover the OCNG pattern is accompanied by a PCFICH/PDCCH/PHICH reference channel which specifies the control region. For any aggregation and PHICH allocation, the PDCCH and any unused PHICH groups are padded with resource element groups with a power level given respectively by PDCCH_RA/RB and PHICH_RA/RB as specified in the test case such that a total power spectral density in the control region that is constant on an OFDM symbol basis is targeted.

## A.5.2.1OCNG TDD pattern 1: One sided dynamic OCNG TDD pattern

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the subframes available for DL transmission (depending on TDD UL/DL configuration), when the unallocated area is continuous in frequency domain (one sided).

Table A.5.2.1-1: OP.1 TDD: One sided dynamic OCNG TDD Pattern

## A.5.2.2OCNG TDD pattern 2: Two sided dynamic OCNG TDD pattern

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the subframes available for DL transmission (depending on TDD UL/DL configuration), when the unallocated area is discontinuous in frequency domain (divided in two parts by the allocated area – two sided), starts with PRB 0 and ends with PRB .

Table A.5.2.2-1: OP.2 TDD: Two sided dynamic OCNG TDD Pattern

## A.5.2.3OCNG TDD pattern 3: 49 RB OCNG allocation with MBSFN in 10 MHz

Table A.5.2.3-1: OP.3 TDD: OCNG TDD Pattern 3 for 5ms downlink-to-uplink switch-point periodicity

## A.5.2.4OCNG TDD pattern 4: One sided dynamic OCNG TDD pattern for MBMS transmission

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is continuous in frequency domain (one sided) and MBMS performance is tested.

Table A.5.2.4-1: OP.4 TDD: One sided dynamic OCNG TDD Pattern for MBMS transmission

## A.5.2.5OCNG TDD pattern 5: One sided dynamic 16QAM modulated OCNG TDD pattern

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the sub-frames available for DL transmission (depending on TDD UL/DL configuration), when the unallocated area is continuous in frequency domain (one sided).

Table A.5.2.5-1: OP.5 TDD: One sided dynamic 16QAM modulated OCNG TDD Pattern

## A.5.2.6OCNG TDD pattern 6: dynamic OCNG TDD pattern when user data is in 2 non-contiguous blocks

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the subframes available for DL transmission (depending on TDD UL/DL configuration), when the unallocated area is discontinuous in frequency domain (divided in two parts by the first allocated block). The second allocated block ends with PRB .

Table A.5.2.6-1: OP.6 TDD: OCNG TDD Pattern when user data is in 2 non-contiguous blocks

A.5.2.7OCNG TDD pattern 7: dynamic OCNG TDD pattern when user data is in multiple non-contiguous blocks

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data, EPDCCH or system information) of the DL sub-frames, when the unallocated area is discontinuous in frequency domain (divided in multiple parts by the M allocated blocks for data transmission). The m-th allocated block starts with RPB  and ends with PRB , where m = 1, …, M. The system bandwidth starts with RPB 0 and ends with.

Table A.5.2.7-1: OP.7 TDD: OCNG TDD Pattern when user data is in multiple non-contiguous blocks

## A.5.2.8OCNG TDD pattern 8: Dynamic OCNG TDD pattern for TM10 transmission

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is discontinuous in frequency domain where there are M unallocated PRB blocks labled from 1-st block to M-th block (M>1) and the m-th block starts with PRB and end with PRB , or when the unallocated area is continuous in frequency domain where M =1 (one sided). The system bandwidth starts with RPB 0 and ends with. should be equal to or less than .

Table A.5.2.8-1: OP.8 TDD: Dynamic OCNG TDD Pattern

## A.5.3OCNG Patterns for Narrowband IoT

The following OCNG patterns are used for modelling allocations to virtual narrowband IoT UEs (which are not under test). The OCNG pattern for each sub frame specifies the allocations that shall be filled with OCNG, and furthermore, the relative power level of each such allocation.

In each test case the OCNG is expressed by parameters OCNG_RA and OCNG_RB which together with a relative power level () specifies the NPDSCH EPRE-to-NRS EPRE ratios in OFDM symbols with and without Narrowband reference symbols, respectively. The relative power, which is used for modelling boosting per virtual UE allocation, is expressed by:

where  denotes the relative power level of the i:th virtual UE. The parameter settings of OCNG_RA, OCNG_RB, and the set of relative power levels are chosen such that when also taking allocations to the UE under test into account, as given by a NPDSCH or NPDCCH reference channel, a transmitted power spectral density that is constant on an OFDM symbol basis is targeted.

## A.5.3.1Narrowband IoT OCNG pattern 1

Table A.5.3.1-1: NB.OP.1 FDD: OCNG FDD Pattern 1

## A.5.4OCNG Patterns for frame structure type 3

The following OCNG patterns are used for modelling allocations to virtual UEs (which are not under test). The OCNG pattern for each sub frame specifies the allocations that shall be filled with OCNG, and furthermore, the relative power level of each such allocation.

In each test case the OCNG is expressed by parameters OCNG_RA and OCNG_RB which together with a relative power level () specifies the PDSCH EPRE-to-RS EPRE ratios in OFDM symbols with and without reference symbols, respectively. The relative power, which is used for modelling boosting per virtual UE allocation, is expressed by:

where  denotes the relative power level of the i:th virtual UE. The parameter settings of OCNG_RA, OCNG_RB, and the set of relative power levels are chosen such that when also taking allocations to the UE under test into account, as given by a PDSCH reference channel, a constant transmitted power spectral density that is constant on an OFDM symbol basis is targeted.

Moreover the OCNG pattern is accompanied by a PDCCH reference channel which specifies the control region. For any aggregationthe PDCCH are padded with resource element groups with a power level given respectively by PDCCH_RA/RB as specified in the test case such that a total power spectral density in the control region that is constant on an OFDM symbol basis is targeted.

For the performance requirements of UE with the CA capability, the OCNG patterns apply for eachLAA Scell.

## A.5.4.1OCNG FS3 pattern 1: One sided dynamic OCNG frame structure type 3 pattern

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is continuous in frequency domain (one sided).

Table A.5.4.1-1: OP.1 FS3: One sided dynamic OCNG frame structure type 3 Pattern

## A.5.4.2OCNG FS3 pattern 2: Two sided dynamic OCNG frame structure 3 pattern

This OCNG Pattern fills with OCNG all empty PRB-s (PRB-s with no allocation of data or system information) of the DL sub-frames, when the unallocated area is discontinuous in frequency domain (divided in two parts by the allocated area – two sided), starts with PRB 0 and ends with PRB .

Table A.5.4.2-1: OP.2 FS3: Two sided dynamic OCNG frame structure type 3 Pattern

## A.6Sidelink reference measurement channels

## A.6.1General

The algorithm for determining the payload size A is as follows; given a desired coding rate R and radio block allocation NRB

1. Calculate the number of channel bits Nch that can be transmitted during the first transmission of a given sub-frame.

2. Find A such that the resulting coding rate is as close to R as possible, that is,

,

subject to

a) A is a valid TB size according to section 7.1.7 of TS 36.213 [6] assuming an allocation of NRB resource blocks.

b) C is the number of Code Blocks calculated according to section 5.1.2 of TS 36.212 [5].

3. If there is more than one A that minimizes the equation above, then the larger value is chosen per default and the chosen code rate should not exceed 0.93.

## A.6.1.1Overview of ProSe reference measurement channels

In Table A.6.1.1-1 are listed the ProSe reference measurement channels specified in annexes A.6.2 to A.6.6 of this release of TS 36.101. This table is informative and serves only to a better overview. The reference for the concrete reference measurement channels and corresponding implementation’s parameters as to be used for requirements are annexes A.6.2 to A.6.6 as appropriate.

Table A.6.1.1-1: Overview of ProSe reference measurement channels

## A.6.2Reference measurement channel for receiver characteristics

For ProSe Direct Discovery, Table A.6.2-1 is applicable for measurements on the Receiver Characteristics (clause 7) including the requirements of subclause 7.4D (Maximum input level).

For ProSe Direct Communication, Table A.6.2-2 is applicable for measurements on the Receiver Characteristics (clause 7) with the exception of subclause 7.4D (Maximum input level). Tables A.6.2-3, A.6.2-4, are applicable for subclause 7.4D (Maximum input level).

Table A.6.2-1: Fixed Reference measurement channel for ProSe Direct Discovery receiver requirements and maximum input level

Table A.6.2-2: Fixed Reference measurement channel for ProSe Direct Communication receiver requirements

Table A.6.2-3: Fixed Reference measurement channel for ProSe Direct Communicationfor maximum input power for UE categories 2-8

Table A.6.2-4: Fixed Reference measurement channel for ProSe Direct Communicationfor maximum input power for UE category 1

## A.6.3Reference measurement channels for PSDCH performance requirements

Table A.6.3-1: Fixed Reference measurement channel for PSDCH performance requirement

## A.6.4Reference measurement channels for PSCCH performance requirements

Table A.6.4-1: Fixed reference measurement channel for PSCCH performance requirement

## A.6.5Reference measurement channels for PSSCH performance requirements

Table A.6.5-1: Fixed reference measurement channel for PSSCH performance requirement

Table A.6.5-2: Fixed reference measurement channel for PSSCH for maximum Sidelink processes test

## A.6.6Reference measurement channels for PSBCH performance requirements

Table A.6.6-1: Fixed reference measurement channel for PSBCH performance requirement

## A.7Sidelink reference resource pool configurations

## A.7.1Reference resource pool configurations for ProSe Direct Discovery demodulation tests

## A.7.1.1FDD

Table A.7.1.1-1: ProSe Direct Discovery configuration for E-UTRA FDD (Configuration #1-FDD)

Table A.7.1.1-2: ProSe Direct Discovery configuration for E-UTRA FDD (Configuration #2-FDD)

Table A.7.1.1-3: ProSe Direct Discovery configuration for E-UTRA FDD (Configuration #3-FDD)

Table A.7.1.1-4: ProSe Direct Discovery configuration for E-UTRA FDD for out-of-network coverage operation (Configuration #4-FDD)

## A.7.1.2TDD

Table A.7.1.2-1: ProSe Direct Discovery configuration for E-UTRA TDD Config 0 (Configuration #1-TDD)

Table A.7.1.2-2: ProSe Direct Discovery configuration for E-UTRA TDD (Configuration #2-TDD)

## A.7.2Reference resource pool configurations for ProSe Direct Communication demodulation tests

## A.7.2.1FDD

Table A.7.2.1-1: ProSe Direct Communication pre-configuration for E-UTRAN FDD for out-of-network coverage operation (Configuration #1-FDD)

Table A.7.2.1-2: ProSe Direct Communication configuration for E-UTRA FDD (Configuration #2-FDD)

Table A.7.2.1-3: ProSe Direct Communication configuration for E-UTRA FDD (Configuration #3-FDD)

Table A.7.2.1-4: ProSe Direct Communication configuration for E-UTRA FDD (Configuration #4-FDD)

Table A.7.2.1-5: ProSe Direct Communication configuration for E-UTRA FDD (Configuration #5-FDD)

## A.8V2X reference measurement channels

## A.8.1General

The algorithm for determining the payload size A is as follows; given a desired coding rate R and radio block allocation NRB

1. Calculate the number of channel bits Nch that can be transmitted during the first transmission of a given sub-frame.

2. Find A such that the resulting coding rate is as close to R as possible, that is,

,

subject to

a) A is a valid TB size according to section 7.1.7 of TS 36.213 [6] assuming an allocation of NRB resource blocks.

b) C is the number of Code Blocks calculated according to section 5.1.2 of TS 36.212 [5].

3. If there is more than one A that minimizes the equation above, then the larger value is chosen per default and the chosen code rate should not exceed 0.93.

## A.8.1.1Overview of V2X reference measurement channels

In Table A.8.1.1-1 are listed the Sidelink reference measurement channels specified in annexes A.8.2 to A.8.6 of this release of TS 36.101. This table is informative and serves only to a better overview. The reference for the concrete reference measurement channels and corresponding implementation’s parameters as to be used for requirements are annexes A.8.2 to A.8.6 as appropriate.

Table A.8.1.1-1: Overview of Sidelink reference measurement channels

## A.8.2Reference measurement channel for receiver characteristics

For V2X side link transmission over PC5, Table A.8.2-1 is applicable for measurements on the Receiver Characteristics (clause 7) with the exception of Maximum input level (subclause 7.4G). Table A.8.2-2 and Table A.8.2-3, are applicable for Maximum input level (subclause 7.4G).

Table A.8.2-1 Fixed Reference measurement channel for V2X receiver requirements

Table A.8.2-2 Fixed Reference measurement channel for V2X maximum input level requirements for 16QAM

Table A.8.2-3 (Void)

Table A.8.2-4 Fixed Reference measurement channel for V2X maximum input level for 64QAM

## A.8.3Reference measurement channel for transmitter characteristics

For V2X side link transmission over PC5, Table A.8.3-1 and Table A.8.3-2 are applicable for measurements on the Transmitter Characteristics (clause 6).

Table A.8.3-1 Fixed Reference measurement channel for V2X Transmitter requirements for QPSK

Table A.8.3-2 Fixed Reference measurement channel for V2X Transmitter requirements for 16QAM

Table A.8.3-3 Fixed Reference measurement channel for V2X Transmitter requirements for 64QAM

## A.8.4Reference measurement for PSCCH performance requirements

Table A.8.4-1: Fixed reference measurement channel for PSCCH performance requirement

## A.8.5Reference measurement for PSSCH performance requirements

Table A.8.5-1: Fixed reference measurement channel for PSSCH performance requirement

Table A.8.5-2: Fixed reference measurement channel for PSSCH performance requirement

## A.8.6Reference measurement for PSBCH performance requirements

Table A.8.6-1: Fixed reference measurement channel for PSBCH performance requirement

## A.9V2X reference resource pool configurations

Table A.9-1: V2X sidelink communication pre-configuration for PSSCH/PSCCH tests (Configuration #1-V2X)

Table A.9-2: V2X sidelink communication pre-configuration for power imbalance test (Configuration #2-V2X)

Table A.9-3: V2X sidelink communication communication configuration for PSSCH with eNB based synchronization test (Configuration #3-V2X)

Table A.9-4: V2X sidelink communication pre-configuration for soft buffer test (Configuration #4-V2X)

Table A.9-5: V2X sidelink communication pre-configuration for PSCCH/PSSCH decoding capability test (Configuration #5-V2X)

Table A.9-6: V2X sidelink communication pre-configuration for PSCCH/PSSCH decoding capability test (Configuration #6-V2X)

## Annex B (normative): Propagation conditions

## B.1Static propagation condition

## B.1.1UE Receiver with 2Rx

For 1 port transmission the channel matrix is defined in the frequency domain by

.

For 2 port transmission the channel matrix is defined in the frequency domain by

.

For 4 port transmission the channel matrix is defined in the frequency domain by

For 8 port transmission the channel matrix is defined in the frequency domain by

## B.1.2UE Receiver with 4Rx

For 1 port transmission the channel matrix is defined in the frequency domain by

.

For 2 port transmission the channel matrix is defined in the frequency domain by

.

For 4 port transmission the channel matrix is defined in the frequency domain by

.

For 8 port transmission the channel matrix is defined in the frequency domain by

## B.1.3UE Receiver with 8Rx

For 1 port transmission the channel matrix is defined in the frequency domain by

.

For 2 port transmission the channel matrix is defined in the frequency domain by

.

For 4 port transmission the channel matrix is defined in the frequency domain by

.

For 8 port transmission the channel matrix is defined in the frequency domain by

## B.2Multi-path fading propagation conditions

The multipath propagation conditions consist of several parts:

-A delay profile in the form of a "tapped delay-line", characterized by a number of taps at fixed positions on a sampling grid. The profile can be further characterized by the r.m.s. delay spread and the maximum delay spanned by the taps.

-A combination of channel model parameters that include the Delay profile and the Doppler spectrum, that is characterized by a classical spectrum shape and a maximum Doppler frequency

-A set of correlation matrices defining the correlation between the UE and eNodeB antennas in case of multi-antenna systems.

-Additional multi-path models used for CQI (Channel Quality Indication) tests

## B.2.1Delay profiles

The delay profiles are selected to be representative of low, medium and high delay spread environments. The resulting model parameters are defined in Table B.2.1-1 and the tapped delay line models are defined in Tables B.2.1-2, B.2.1-3 and B.2.1-4.

Table B.2.1-1 Delay profiles for E-UTRA channel models

Table B.2.1-2 Extended Pedestrian A model (EPA)

Table B.2.1-3 Extended Vehicular A model (EVA)

Table B.2.1-4 Extended Typical Urban model (ETU)

## B.2.2Combinations of channel model parameters

The propagation conditions used for the performance measurements in multi-path fading environment are indicated as EVA[number], EPA[number] or ETU[number] where ‘number’ indicates the maximum Doppler frequency (Hz).

Table B.2.2-1 Void

## B.2.3MIMO Channel Correlation Matrices

The MIMO channel correlation matrices defined in B.2.3 apply for the antenna configuration using uniform linear arrays at both eNodeB and UE.

## B.2.3.1Definition of MIMO Correlation Matrices

Table B.2.3.1-1 defines the correlation matrix for the eNodeB

Table B.2.3.1-1 eNodeB correlation matrix

Table B.2.3.1-2 defines the correlation matrix for the UE:

Table B.2.3.1-2 UE correlation matrix

Table B.2.3.1-3 defines the channel spatial correlation matrix . The parameters, α and β in Table B.2.3.1-3 defines the spatial correlation between the antennas at the eNodeB and UE.

Table B.2.3.1-3:  correlation matrices

For cases with more antennas at either eNodeB or UE or both, the channel spatial correlation matrix can still be expressed as the Kronecker product of  and  according to.

## B.2.3.2MIMO Correlation Matrices at High, Medium and Low Level

The  and  for different correlation types are given in Table B.2.3.2-1.

Table B.2.3.2-1: The  and  parameters for ULA MIMO correlation matrices

The correlation matrices for high, medium, low and medium A correlation are defined in Table B.2.3.1-2, B.2.3.2-3, B.2.3.2-4 and B.2.3.2-5 as below.

The values in Table B.2.3.2-2 have been adjusted for the 4x2 and 4x4 high correlation cases to insure the correlation matrix is positive semi-definite after round-off to 4 digit precision. This is done using the equation:

Where the value “a” is a scaling factor such that the smallest value is used to obtain a positive semi-definite result. For the 4x2 high correlation case, a=0.00010. For the 4x4 high correlation case, a=0.00012.

The same method is used to adjust the 2x4 and 4x4 medium correlation matrix in Table B.2.3.2-3 to insure the correlation matrix is positive semi-definite after round-off to 4 digit precision with a = 0.00010 and a = 0.00012.

Table B.2.3.2-2: MIMO correlation matrices for high correlation

Table B.2.3.2-3: MIMO correlation matrices for medium correlation

Table B.2.3.2-4: MIMO correlation matrices for low correlation

In Table B.2.3.2-4, is the identity matrix.

Table B.2.3.2-5: MIMO correlation matrices for medium correlation A

## B.2.3AMIMO Channel Correlation Matrices using cross polarized antennas

The MIMO channel correlation matrices defined in B.2.3A apply for the antenna configuration using cross polarized (XP/X-pol) antennas at both eNodeB and UE. The cross-polarized antenna elements with +/-45 degrees polarization slant angles are deployed at eNB and cross-polarized antenna elements with +90/0 degrees polarization slant angles are deployed at UE.

For the cross-polarized antennas, the N antennas are labelled such that antennas for one polarization are listed from 1 to N/2 and antennas for the other polarization are listed from N/2+1 to N, where N is the number of transmit or receive antennas.

## B.2.3A.1Definition of MIMO Correlation Matrices using cross polarized antennas

For the channel spatial correlation matrix, the following is used:

where

- is the spatial correlation matrix at the UE with same polarization,

- is the spatial correlation matrix at the eNB with same polarization,

- is a polarization correlation matrix, and

-denotes transpose.

The matrix is defined as

A permutation matrixelements are defined as

.

where  and  is the number of transmitter and receiver respectively. This is used to map the spatial correlation coefficients in accordance with the antenna element labelling system described in B.2.3A.

## B.2.3A.2Spatial Correlation Matrices using cross polarized antennas at eNB and UE sides

## B.2.3A.2.1Spatial Correlation Matrices at eNB side

For 2-antenna transmitter using one pair of cross-polarized antenna elements, .

For 4-antenna transmitter using two pairs of cross-polarized antenna elements, .

For 8-antenna transmitter using four pairs of cross-polarized antenna elements, .

## B.2.3A.2.2Spatial Correlation Matrices at UE side

For 2-antenna receiver using one pair of cross-polarized antenna elements, .

For 4-antenna receiver using two pairs of cross-polarized antenna elements, .

B.2.3A.3MIMO Correlation Matrices using cross polarized antennas

The values for parameters α, β and γ for the cross polarized antenna models are given in Table B.2.3A.3-1.

Table B.2.3A.3-1: : The  and  parameters for cross-polarized MIMO correlation matrices

The correlation matrices for high spatial correlation and medium correlation A are defined in Table B.2.3A.3-2 and Table B.2.3A.3-3 as below.

The values in Table B.2.3A.3-2 have been adjusted to insure the correlation matrix is positive semi-definite after round-off to 4 digit precision. This is done using the equation:

Where the value “a” is a scaling factor such that the smallest value is used to obtain a positive semi-definite result. For the 8x2 high spatial correlation case, a=0.00010.

Table B.2.3A.3-2: MIMO correlation matrices for high spatial correlation

Table B.2.3A.3-3: MIMO correlation matrices for medium correlation A

## B.2.3A.4Beam steering approach

Given the channel spatial correlation matrix in B.2.3A.1, the corresponding random channel matrix H can be calculated. The signal model for the k-th subframe is denoted as

Where

-H is the Nr xNt channel matrix per subcarrier.

- is the steering matrix,

For 8 transmission antennas, ;

For 4 transmission antennas, .

- controls the phase variation, and the phase for k-th subframe is denoted by, where is the random start value with the uniform distribution, i.e., ,  is the step of phase variation, which is defined in Table B.2.3A.4-1, and k is the linear increment of 1 for every subframe throughout the simulation,

- is the precoding matrix for Nt transmission antennas,

- is the received signal,  is the transmitted signal, and is AWGN.

Table B.2.3A.4-1: The step of phase variation

## B.2.3BMIMO Channel Correlation Matrices using two-dimension cross polarized antennas at eNB and cross polarized antennas at UE

The MIMO channel correlation matrices defined in B.2.3B apply for the antenna configuration using two-dimension (2D) cross polarized antennas at eNodeB and the antenna configuration using cross polarized antennas at UE. The cross-polarized antenna elements with +/-45 degrees polarization slant angles are deployed at eNB and cross-polarized antenna elements with +90/0 degrees polarization slant angles are deployed at UE.

For 2D cross-polarized antenna array at eNodeB, the N antennas are indexed by , and total number of antennas is , where

- is the number of antenna elements in first dimension (i.e. vertical direction) with same polarization,

- is the number of antenna elements in second dimension (i.e. horizontal direction) with same polarization, and

- is the number of polarization groups.

For the 2D cross-polarized antennas at eNB, the N antennas are labelled such that antennas shall be in increasing order of the second dimension firstly, then the first dimension, and finally the polarization group. For a specific antenna element at p-th polarization, n1-th row, and n2-th column within the 2D antenna array, the following index number is used for antenna labelling:

where N is the number of transmit antennas, p is the polarization group index, n1 is the row index, and n2 is the column index of the antenna element.

For the cross-polarized antennas at UE, the N antennas are labelled such that antennas for one polarization are listed from 1 to N/2 and antennas for the other polarization are listed from N/2+1 to N, where N is the number of receive antennas.

## B.2.3B.1Definition of MIMO Correlation Matrices using two-dimension cross polarized antennas at eNB and cross polarized antennas at UE

For the channel spatial correlation matrix, the following is used:

where

- is the spatial correlation matrix at the UE with same polarization,

- is the spatial correlation matrix at the eNB with same polarization,

- is a polarization correlation matrix, and

-denotes transpose.

The spatial correlation matrix at the eNB is further expressed as following:

where

- is the correlation matrix of antenna elements in first dimension with same polarization, and

- is the correlation matrix of antenna elements in second dimension with same polarization.

The matrix  is defined as

A permutation matrix  elements are defined as

.

where  and  is the number of transmitter and receiver respectively. This is used to map the spatial correlation coefficients in accordance with the antenna element labelling system described in B.2.3B.

## B.2.3B.2Spatial Correlation Matrices using two-dimension cross polarized antennas at eNB and cross polarized antennas at UE

## B.2.3B.2.1Spatial Correlation Matrices at eNB side

For one direction of the 2D antenna array at the eNB side, the followings are used to construct the spatial correlation matrix:

For 1 antenna element of the same polarization in one direction, .

For 2 antenna elements of the same polarization in one direction, .

For 3 antenna elements of the same polarization in one direction, .

For 4 antenna elements of the same polarization in one direction, .

where the index  stands for first dimension and second dimension respectively.

## B.2.3B.2.2Spatial Correlation Matrices at UE side

For 2-antenna receiver using one pair of cross-polarized antenna elements, .

For 4-antenna receiver using two pairs of cross-polarized antenna elements, .

## B.2.3B.3MIMO Correlation Matrices using two-dimension cross polarized antennas at eNB and cross polarized antennas at UE

The values for parameters α1, α2, β and γ for high and medium spatial correlation are given in Table B.2.3B.3-1.

Table B.2.3B.3-1

The correlation matrices for high spatial correlation with12(2,3,2)x2 case and 16(2,4,2)x2 case are defined in Table B.2.3B.3-2 as below.

The values in Table B.2.3B.3-2 have been adjusted to insure the correlation matrix is positive semi-definite after round-off to 4 digit precision. This is done using the equation:

where the value “a” is a scaling factor such that the smallest value is used to obtain a positive semi-definite result. For the 16(2,4,2)x2 high spatial correlation case, a=0.00012.

The same method is used to adjust the the 24(3,4,2)x2 and 32(4,4,2)x2 high correlation matrix to insure the correlation matrix is positive semi-definite after round-off to 4 digit precision with a =0.00012 and a=0.00022.

Table B.2.3B.3-2: MIMO correlation matrices for high spatial correlation

## B.2.3B.4Beam steering approach

Given the channel spatial correlation matrix in B.2.3B.1, the corresponding random channel matrix H can be calculated. The signal model for the k-th subframe is denoted as

And the steering matrix is further expressed as following:

where

-H is the Nr xNt channel matrix per subcarrier.

- is the steering matrix,

- is the steering matrix in first dimension with same polarization,

- is the steering matrix in second dimension with same polarization,

- is the number of antenna elements infirst dimension with same polarization,

- is the number of antenna elements in second dimension with same polarization,

For 1 antenna element of the same polarization in one direction, .

For 2 antenna elements of the same polarization in one direction, .

For 3 antenna elements of the same polarization in one direction,.

For 4 antenna elements of the same polarization in one direction, .

where the index  stands for first dimension and second dimension respectively.

- controls the phase variation in first dimension and second dimension respectively, and the phase for k-th subframe is denoted by, where is the random start value with the uniform distribution, i.e., ,  is the step of phase variation, which is defined in Table B.2.3B.4-1, and k is the linear increment of 1 for every subframe throughout the simulation, the index  stands for first dimension and second dimension respectively.

- is the precoding matrix for Nt transmission antennas,

- is the received signal,  is the transmitted signal, and is AWGN.

Table B.2.3B.4-1: The step of phase variation

## B.2.3B.4ABeam steering approach with dual cluster beams

Given the channel spatial correlation matrix in B.2.3B.1, the corresponding random channel matrix H can be calculated. The signal model for the k-th subframe is denoted as

And the steering matrix is further expressed as following:

where

-,are independent channels for  the first beam and second beam with the Nr xNt channel matrix per subcarrier.

-, are the steering matrix for first beam and second beam

- is the steering matrix in first dimension with same polarization,

- is the steering matrix in second dimension with same polarization,

- is the number of antenna elements infirst dimension with same polarization,

- is the number of antenna elements in second dimension with same polarization,

- is the relative power ratio of the second beam to the first beam, the value of is specific to a test case,

For 1 antenna element of the same polarization in one direction, .

For 2 antenna elements of the same polarization in one direction, .

For 3 antenna elements of the same polarization in one direction,.

For 4 antenna elements of the same polarization in one direction, .

where the index  stands for first dimension and second dimension respectively.

- controls the phase variation in first dimension and second dimension respectively, and the phase for k-th subframe is denoted by, where is the random start value with the uniform distribution, i.e., ,  is the step of phase variation, which is defined in Table B.2.3B.4-1, and k is the linear increment of 1 for every subframe throughout the simulation, the index  stands for first dimension and second dimension respectively.

- is the precoding matrix for Nt transmission antennas,

- is the received signal,  is the transmitted signal, and is AWGN.

Table B.2.3B.4A-1: The step of phase variation

## B.2.4Propagation conditions for CQI tests

For Channel Quality Indication (CQI) tests, the following additional multi-path profile is used:

,

in continuous time representation, with  the delay, a a constant andthe Doppler frequency. The same h(t,τ) is used to describe the fading channel between every pair of Tx and Rx.

## B.2.4.1Propagation conditions for CQI tests with multiple CSI processes

For CQI tests with multiple CSI processes, the following additional multi-path profile is used for 2 port transmission:

Whererepresents Hadamard product, indicates the 2x2 propagation channel generated in the manner defined in Clause B.2.4. °  HMP

## B.2.5Void

## B.2.6MBSFN Propagation Channel Profile

## B.2.6.1Subcarrier spacing 15kHz or 7.5kHz

Table B.2.6.1-1 shows propagation conditions that are used for the MBSFN performance requirements in multi-path fading environment in an extended delay spread environment.

Table B.2.6.1-1: Propagation Conditions for Multi-Path Fading Environments for MBSFN Performance Requirements in an extended delay spread environment with subcarrier spacing 15kHz or 7.5kHz

## B.2.6.2Subcarrier spacing 1.25kHz

Table B.2.6.2-1 shows propagation conditions that are used for the MBSFN performance requirements in multi-path fading environment in an extended delay spread environment for subcarrier spacing as 1.25kHz.

Table B.2.6.2-1: Propagation Conditions for Multi-Path Fading Environments for MBSFN Performance Requirements in an extended delay spread environment with subcarrier spacing 1.25kHz

Table B.2.6.2-2: Propagation Conditions for Multi-Path Fading Environments for MBSFN Performance Requirements in an extended delay spread environment with subcarrier spacing 1.25kHz and 50 Hz Doppler frequency

## B.2.6.3Subcarrier spacing 0.37kHz

Table B.2.6.3-1 shows propagation conditions that are used for the MBSFN performance requirements in multi-path fading environment in an extended delay spread environment for subcarrier spacing as 0.37kHz.

Table B.2.6.3-1: Propagation Conditions for Multi-Path Fading Environments for MBSFN Performance Requirements in an extended delay spread environment with subcarrier spacing 0.37kHz

## B.2.6.4Subcarrier spacing 2.5kHz

Table B.2.6.4-1 shows propagation conditions that are used for the MBSFN performance requirements in multi-path fading environment in an extended delay spread environment for subcarrier spacing as 2.5kHz.

Table B.2.6.4-1: Propagation Conditions for Multi-Path Fading Environments for MBSFN Performance Requirements in an extended delay spread environment with subcarrier spacing 2.5kHz

## B.3High speed train scenario

The high speed train condition for the test of the baseband performance is a non fading propagation channel with one tap. Doppler shift is given by

(B.3.1)

where  is the Doppler shift and  is the maximum Doppler frequency. The cosine of angle is given by

, (B.3.2)

, (B.3.3)

, (B.3.4)

where  is the initial distance of the train from eNodeB, and  is eNodeB Railway track distance, both in meters;  is the velocity of the train in m/s,  is time in seconds.

Doppler shift and cosine angle are given by equation B.3.1 and B.3.2-B.3.4 respectively, where the required input parameters listed in table B.3-1 and the resulting Doppler shift shown in Figure B.3-1 are applied for all frequency bands.

Table B.3-1: High speed train scenario

NOTE 1:Parameters for HST conditions in table B.3-1 including  and Doppler shift trajectories presented on figure B.3-1 were derived from Band 7 and are applied for performance verification in all frequency bands.

Figure B.3-1: Doppler shift trajectory

For 1x2 antenna configuration, the same h(t,τ) is used to describe the channel between every pair of Tx and Rx.

For 2x2 antenna configuration, the same h(t,τ) is used to describe the channel between every pair of Tx and Rx with phase shift according to .

## B.3AHST-SFN scenario

There is an infinite number of RRHs distributed equidistantly along the track with the same Cell ID as depicted in figure B.3A-1.

Figure B.3A-1: Deployment of HST-SFN

The location of RRH k is given as:

(B.3A.1)

where:,  and is the distance between the RRHs and railway track, while  is the distance of two RRHs, both in meters.

The train location is denoted as:

(B.3A.2)

where: and a means distance in meters, which means the train is right on the track.

The HST-SFN scenario for the test of the baseband performance is a non fading propagation channel with four taps, namely the four nearest RRHs. Thus RRH k is visible for the train only in the range:

(B.3A.3)

Power level  (dB) for the signal from kth RRH, normalized to the total power received from all visible RRHs, is given by:

for (B.3A.4)

Doppler shift (Hz) from kth RRH is given by:

for (B.3A.5)

The relative delay  (s) for the signal from kth RRH can be derived as:

for (B.3A.6)

In the above v (m/s) is the moving speed of the train, fC (Hz) is the center frequency, and C (m/s) is the velocity of light.

Power level, Doppler shift and relative delay are given by equations B.3A.4 ~ B.3A.6 respectively, where the required input parameters listed in table B.3A-1 and the resulting Doppler shift shown in Figure B.3A-3 are applied for all frequency bands.

Table B.3A-1: HST-SFN scenario

NOTE 1:Parameters for HST-SFN scenario in Table B.3A-1 includingand Doppler shift trajectories presented in Figure B.3A-2 were derived from Band 7 and are applied for performance verification in all frequency bands. And the trajectories of ralative power, Doppler shifts and relative delay presented in Figures B.3A-2~ B.3A-4 are derived from the equations B.3A.4 ~ B.3A.6 respectively.

Figure B.3A-2 Ralative power level trajectories

Figure B.3A-3 Doppler shifts trajectories

Figure B.3A-4 Relative delay trajectories

For 2x2 antenna configuration, the same h(t,τ) is used to describe the channel between every pair of Tx and Rx with phase shift according to .

For 2x4 antenna configuration, the same h(t,τ) is used to describe the channel between every pair of Tx and Rx with phase shift according to .

## B.3BHST-SFN scenario for 500 km/h speed

The channel model for this scenario is the same as B.3A, with the following parameters replacing Table B.3A-1:

Table B.3B-1-500: HST-SFN scenario for higher speed

## B.3CHST scenario for 500 km/h speed

The channel model for this scenario is the same as B.3, with the following parameters replacing Table B.3-1:

Table B.3C-1: HST-500 scenario for higher speed

## B.4Beamforming Model

## B.4.1Single-layer random beamforming (Antenna port 5, 7, or 8)

Single-layer transmission on antenna port 5 or on antenna port 7 or 8 without a simultaneous transmission on the other antenna port, is defined by using a precoder vector  of size  or  randomly selected with the number of layers  from Table 6.3.4.2.3-1 or Table 6.3.4.2.3-2 in [4] as beamforming weights. This precoder takes as an input the signal, , for antenna port , with  the number of modulation symbols including the user-specific reference symbols (DRS), and generates a block of signals  the elements of which are to be mapped onto the same physical RE but transmitted on different antenna elements:

Single-layer transmission on antenna port 7 or 8 with a simultaneous transmission on the other antenna port, is defined by using a pair of precoder vectors  and  each of size  or , which are not identical and randomly selected with the number of layers  from Table 6.3.4.2.3-1 or Table 6.3.4.2.3-2 in [4], as beamforming weights, and normalizing the transmit power as follows:

The precoder update granularity is specific to a test case.

The CSI reference symbols  satisfying , , are transmitted on the same physical antenna element as the modulation symbols . The CSI reference symbols  satisfying , , are transmitted on the same physical antenna element as the modulation symbols .

## B.4.1ASingle-layer random beamforming (Antenna port 7, 8, 11 or 13 with enhanced DMRS table configured)

Single-layer transmission on antenna port 11 with a simultaneous transmission on one antenna port from antenna port 7,8 or 13, is defined by using a pair of precoder vectors  and  each of size , which are not identical and randomly selected with the number of layers  from Table 6.3.4.2.3-1 in [4], as beamforming weights, and normalizing the transmit power as follows:

The precoders takes and as the input the signals, , with  the number of modulation symbols including the user-specific reference symbols (DM-RS), and generates a block of signals  the elements of which are to be mapped onto the same physical RE but transmitted on different antenna elements.

The antenna port  update granularity is specific to a test case.

The precoder update granularity is specific to a test case.

The CSI reference symbols  satisfying, , are transmitted on the same physical antenna element as the modulation symbols . The CSI reference symbols  satisfying, , are transmitted on the same physical antenna element as the modulation symbols .

## B.4.2Dual-layer random beamforming (antenna ports 7 and 8)

Dual-layer transmission on antenna ports 7 and 8 is defined by using a precoder matrix  of size  randomly selected with the number of layers  from Table 6.3.4.2.3-1 in [4] as beamforming weights. This precoder takes as an input a block of signals for antenna ports 7 and 8, , , with  being the number of modulation symbols per antenna port including the user-specific reference symbols, and generates a block of signals the elements of which are to be mapped onto the same physical RE but transmitted on different antenna elements:

,

The precoder update granularity is specific to a test case.

The CSI reference symbols  satisfying , , are transmitted on the same physical antenna element as the modulation symbols . The CSI reference symbols  satisfying , , are transmitted on the same physical antenna element as the modulation symbols .

## B.4.3Generic beamforming model (antenna ports 7-14)

The transmission on antenna port(s)  is defined by using a precoder matrix  of size , where is the number of CSI reference signals configured per test and  is the number of spatial layers. This precoder takes as an input a block of signals for antenna port(s) , , , with  being the number of modulation symbols per antenna port including the user-specific reference symbols (DM-RS), and generates a block of signals  the elements of which are to be mapped onto the same time-frequency index pair  but transmitted on different physical antenna elements:

The precoder matrix is specific to a test case.

The physical antenna elements are identified by indices , where  is the number of physical antenna elements configured per test.

Modulation symbols  with  (i.e. beamformed PDSCH and DM-RS) are mapped to the physical antenna index .

Modulation symbols  with  (i.e. PBCH, PDCCH, PHICH, PCFICH) are mapped to the physical antenna index , where  is the number of cell-specific reference signals configured per test.

Modulation symbols  with (i.e. CRS) are mapped to the physical antenna index , where  is the number of cell-specific reference signals configured per test.

Modulation symbols  with  (i.e. CSI-RS) are mapped to the physical antenna index , where is the number of CSI reference signals configured per test.

## B.4.4Random beamforming for EPDCCH distributed transmission (Antenna port 107 and 109)

EPDCCH distributed transmission on antenna port 107 and antenna port 109 is defined by using a pair of precoder vectors  and  each of size , which are not identical and randomly selected per EPDCCH PRB pair with the number of layers  from Table 6.3.4.2.3-1 in [4], as beamforming weights. This precoder takes as an input the signal, , for antenna port , with  the number of modulation symbols including the user-specific reference symbols (DMRS), and generates a block of signals . When EPDCCH is associated with port 107, the transmitted block of signals is deonted as

.

When EPDCCH is associated with port 109, the transmitted block of signals is denoted as

.

## B.4.5Random beamforming for EPDCCH localized transmission (Antenna port 107, 108, 109 or 110)

EPDCCH localized transmission on antenna port 107, 108, 109 or 110 is defined by using a precoder vector  of size 2×1 randomly selected with the number of layers  from Table 6.3.4.2.3-1 in [4] as beamforming weights. This precoder takes as an input the signal,, for antenna port , with  the number of modulation symbols including the user-specific reference symbols (DMRS), and generates a block of signals  the elements of which are to be mapped onto the same physical RE but transmitted on different antenna elements:

.

## B.4.6Beamforming model for CRI test

The transmission on antenna port(s)  is defined by using a precoder matrix  of size , where is the number of CSI reference signals configured per test and  is the number of spatial layers. This precoder takes as an input a block of signals for antenna port(s) , , , with  being the number of modulation symbols per antenna port including the user-specific reference symbols (DM-RS), and generates a block of signals  the elements of which are to be mapped onto the same time-frequency index pair  but transmitted on different physical antenna elements:

-is precoder matrix

- is amplitude scaling factor for CRI test,

- is power scaling factor as following definition:

●, A = 5 dB, B = -1.3351 dB.

● controls the phase variation, and the phase for m-th subframe is denoted by, where is the random start value with the uniform distribution, i.e., ,  is the step of phase variation which is defined in Table B.4.6-1, and m is the linear increment of 1 for every sub-frame throughout the simulation.

●K is the number of configured CSI-RS resources

●

-For following CRI with multiple CSI-RS resources configured, equals to CRI value reported by UE

-For fixed CRI with single CSI-RS resource configure, equals to 0.

Table B.4.6-1: The step of phase variation

The physical antenna elements are identified by indices, where  is the number of physical antenna elements configured per test.

Modulation symbols  with  (i.e. beamformed PDSCH and DM-RS) are mapped to the physical antenna index.

For the k-th configured CSI-RS resource, modulation symbols  with  (i.e. CSI-RS) are firstly multipled by amplitude scaling factor  to generate power scaled symols :

-equals to CSI-RS resource index (k-th)

And power scaled symols with  (i.e. power scaled CSI-RS) are mapped to the physical antenna index, where is the number of CSI reference signals configured per test.

Modulation symbols  with  (i.e. PBCH, PDCCH, PHICH, PCFICH) are mapped to the physical antenna index , where  is the number of cell-specific reference signals configured per test.

Modulation symbols  with (i.e. CRS) are mapped to the physical antenna index , where  is the number of cell-specific reference signals configured per test.

## B.5Interference models for enhanced performance requirements Type-A

This clause provides a description for the modelling of interfering cell transmissions for enhanced performance requirements Type-A including: definition of dominant interferer proportion, transmission mode 3, 4 and 9 type of interference modelling.

## B.5.1Dominant interferer proportion

Each interfering cell involved in enhanced performance requirements Type-A is characterized by its associated dominant interferer proportion (DIP) value:

where is  is the average received power spectral density from the i-th strongest interfering cell involved in the requirement scenario (is assumed to be the power spectral density associated with the serving cell) and  where  is the average power spectral density of a white noise source consistent with the definition provided in subclause 3.2 and  is the total number of cells involved in a given requirement scenario.

## B.5.2Transmission mode 3 interference model

This subclause provides transmission mode 3 interference modelling for each explicitly modelled interfering cell in the requirement scenario. In each subframe, each interfering cell shall transmit randomly modulated data over the entire PDSCH region and the full transmission bandwidth. Transmitted physical channels shall include PSS, SSS and PBCH.

For each subframe and each CQI subband as defined in subclause 7.2 of [6], a transmission rank shall be randomly determined independently from other CQI subbands as well as other interfering cells. Probabilities of occurrence of each possible transmission rank are as specified in the requirement scenario.

For rank-1 transmission over a subband, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to 16QAM randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4].

For rank-2 transmission over a subband, precoding for spatial multiplexing with large delay CDD over two layers for the number of antenna ports in the requirement scenario shall be applied to 16QAM randomly modulated layer symbols, as specified in subclause 6.3.4.2.2 of [4].

For unallocated REs in the control region, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio for these REs shall be as defined for PDCCH in Annex C.3.2.

## B.5.3Transmission mode 4 interference model

This subclause provides transmission mode 4 interference modelling for each explicitly modelled interfering cell in the requirement scenario. In each subframe, each interfering cell shall transmit randomly modulated data over the entire PDSCH region and the full transmission bandwidth according to the probabilities of occurrence. Transmitted physical channels shall include PSS, SSS and PBCH. Probabilites of occurrence in each subframe are as specified in the requirement scenario. If the probabilities of occurrence in each subframe are not specified in the requirement scenario, as default, they are equal to 1.

For each subframe and each CQI subband as defined in subclause 7.2 of [6], a transmission rank shall be randomly determined independently from other CQI subbands as well as other interfering cells. Probabilities of occurrence of each possible transmission rank are as specified in the requirement scenario.

For each subframe and CQI subband, a precoding matrix for the number of layers  associated to the selected rank shall be selected randomly from Table 6.3.4.2.3-1 of [4]. Note that codebook index 0 shall be excluded from random precoder selection when the number of layers is .

Precoding for spatial multiplexing with cell-specific reference signals for the number of antenna ports in the requirement scenario shall be applied to 16QAM randomly modulated layer symbols, as specified in subclause 6.3.4.2.1 of [4] with the selected precoding matrices for each subframe and each CQI subband.

For unallocated REs in the control region, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio for these REs shall be as defined for PDCCH in Annex C.3.2.

## B.5.4Transmission mode 9 interference model

This subclause provides transmission mode 9 interference modelling for each explicitly modelled interfering cell in the requirement scenario. In each subframe, each interfering cell shall transmit randomly modulated data over the entire PDSCH region and the full transmission bandwidth according to the probabilities of occurrence. Transmitted physical channels shall include PSS, SSS and PBCH. Probabilites of occurrence in each subframe are as specified in the requirement scenario. If the probabilities of occurrence in each subframe are not specified in the requirement scenario, as default, they are equal to 1.

For each subframe and each CQI subband as defined in subclause 7.2 of [6], a transmission rank shall be randomly determined independently from other CQI subbands as well as other interfering cells. Probabilities of occurrence of each possible transmission rank are as specified in the requirement scenario.

For each subframe and each CQI subband, a precoding matrix for the number of layers  associated to the selected rank shall be selected randomly from Table 6.3.4.2.3-2 of [4].

The generic beamforming model in subclause B.4.3 shall be applied assuming cell-specific reference signals and CSI reference signals as specified in the requirement scenario. Random precoding with selected rank and precoding matrices for each subframe and each CQI subband shall be applied to 16QAM randomly modulated layer symbols including the user-specific reference symbols over antenna port 7 when the rank is one and antenna ports 7, 8 when the rank is two.

For unallocated REs in the control region, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio for these REs shall be as defined for PDCCH in Annex C.3.2.

## B.6Interference models for enhanced performance requirements Type-B

This clause provides a description for the modelling of interfering cell transmissions for enhanced performance requirements Type-B including: transmission mode 2, 3, 4 and 9 type of interference modelling and a definition of the random interference model.

## B.6.1Transmission mode 2 interference model

This subclause provides transmission mode 2 interference modelling for each explicitly modelled interfering cell in the requirement scenario. In each subframe, each interfering cell shall transmit randomly modulated data over the PDSCH region as specified in subclause B.6.6. Transmitted physical channels shall include PSS, SSS and PBCH.

The MCS shall be randomly determined with probabilities of occurrence of each possible MCS as specified in subclause B.6.6.

Precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to the randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4].

For unallocated REs in the control region, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio for these REs shall be as defined for PDCCH in Annex C.3.2.

## B.6.2Transmission mode 3 interference model

This subclause provides transmission mode 3 interference modelling for each explicitly modelled interfering cell in the requirement scenario. In each subframe, each interfering cell shall transmit randomly modulated data over the PDSCH region as specified in subclause B.6.6.  Transmitted physical channels shall include PSS, SSS and PBCH.

The transmission rank shall be randomly determined for each user defined in section B.6.6 with probabilities of occurrence of each possible transmission rank as specified in subclause B.6.6.

The MCS shall be randomly determined with probabilities of occurrence of each possible MCS as specified in subclause B.6.6.

For rank-1 transmission, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to the randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4].

For rank-2 transmission, precoding for spatial multiplexing with large delay CDD over two layers for the number of antenna ports in the requirement scenario shall be applied to the randomly modulated layer symbols, as specified in subclause 6.3.4.2.2 of [4].

For unallocated REs in the control region, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio for these REs shall be as defined for PDCCH in Annex C.3.2.

## B.6.3Transmission mode 4 interference model

This subclause provides transmission mode 4 interference modelling for each explicitly modelled interfering cell in the requirement scenario. In each subframe, each interfering cell shall transmit randomly modulated data over the PDSCH region as specified in subclause B.6.6.  Transmitted physical channels shall include PSS, SSS and PBCH.

The transmission rank shall be randomly determined with probabilities of occurrence of each possible transmission rank as specified in subclause B.6.6.

The MCS shall be randomly determined with probabilities of occurrence of each possible MCS as specified in subclause B.6.6.

For each TTI, for each user defined in B.6.6, a single precoding matrix for the number of layers  associated to the selected rank shall be selected randomly from Table 6.3.4.2.3-1 of [4]. Note that codebook index 0 shall be excluded from random precoder selection when the number of layers is .

Precoding for spatial multiplexing with cell-specific reference signals for the number of antenna ports in the requirement scenario shall be applied to randomly modulated layer symbols, as specified in subclause 6.3.4.2.1 of [4] with the selected precoding matrices as specified in subclause B.6.6.

For unallocated REs in the control region, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio for these REs shall be as defined for PDCCH in Annex C.3.2.

## B.6.4Transmission mode 9 interference model

This subclause provides transmission mode 9 interference modelling for each explicitly modelled interfering cell in the requirement scenario. In each subframe, each interfering cell shall transmit randomly modulated data over the PDSCH region as specified in subclause B.6.6.  Transmitted physical channels shall include PSS, SSS and PBCH.

The transmission rank shall be randomly determined with probabilities of occurrence of each possible transmission rank as specified in subclause B.6.6.

The MCS shall be randomly determined with probabilities of occurrence of each possible MCS as specified in subclause B.6.6.

For each TTI, for each user defined in B.6.6, a single precoding matrix for the number of layers  associated to the selected rank shall be selected randomly from Table 6.3.4.2.3-1 of [4].  Note that codebook index 0 shall be excluded from random precoder selection when the number of layers is .

The generic beamforming model in subclause B.4.3 shall be applied assuming cell-specific reference signals and CSI reference signals as specified in the requirement scenario. Random precoding with selected rank and precoding matrices for each subframe shall be applied to randomly modulated layer symbols including the user-specific reference symbols over antenna port 7 when the rank is one and antenna ports 7, 8 when the rank is two.

For each TTI, for each user defined in B.6.6, the scrambling ID value nSCID is randomly assigned from the set of {0,1}.

For unallocated REs in the control region, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio for these REs shall be as defined for PDCCH in Annex C.3.2.

## B.6.5CRS interference model

This subclause provides for the CRS interference modelling for each explicitly modelled interfering cell in the requirement scenario. In each subframe there is no PDSCH transmitted. Transmitted physical channels shall include PSS, SSS and PBCH.

For unallocated REs in the control region, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio for these REs shall be as defined for PDCCH in Annex C.3.2.

## B.6.6Random interference model

This subclause presents the interference model which defines the resource allocation, MCS and rank for the two interference cells. The model includes approximately 10% DTX on these interference cells. Table B.6.6-1 shows the resource allocation for four users in two different configurations for each of the two interferers. Table B.6.6-2 shows the resource allocation to be used for special subframes with TM9 interference. Table B.6.6-3 shows the probabilities for the MSC and rank for these users.

Table B.6.6-1: Resource allocation for the random interference model

Table B.6.6-2: Resource allocation for the random interference model for TM9 special subframes

Table B.6.6-3 MCS and rank configuration for the random interference model

## B.7Interference models for enhanced downlink control channel performance requirements Type A and B

This clause provides a description for the modelling of interfering cell transmissions for the enhanced downlink control channel performance requirements Type A and B.

## B.7.1PDCCH, PCFICH and PHICH interference model

This subclause provides a description of the interfering cell transmissions model for the enhanced PDCCH/PCFICH and PHICH downlink control channel performance requirements Type A and B under synchronous network scenarios.

The transmitted physical signals and channels shall include CRS, PSS, SSS, PBCH and PCFICH. The PDCCH and PHICH transmit signals are emulated as virtual PDCCH signals described further in the clause.

The PDCCH signals are modelled with a per control channel element (CCE) level granularity and have guaranteed 50% CCE resource loading in each subframe. For each subframe the set of active and inactive CCEs is derived in accordance to the following procedure:

1)All available CCEs for the PDCCH and PHICH are marked as CCE0, CCE1, …, CCEN-1.

2)For the given partial loading ratio X = 50% the numbers of active CCEs MActive and inactive CCEs MInactive are derived

3)The indexes of MInactive inactive CCEs are randomly selected out of the full set of CCEs.

4)The remaining MActive CCEs are assigned to be active.

No signals are transmitted in the REs corresponding to the inactive CCEs. The PDCCH signals are transmitted in the REs corresponding to the active CCEs. For PDCCH REs, precoding for transmit diversity for the number of antenna ports in the requirement scenario shall be applied to QPSK randomly modulated layer symbols, as specified in subclause 6.3.4.3 of [4]. The EPRE ratio of the PDCCH REs in the active CCEs shall be derived in accordance to the following procedure:

1)For each generated active i-th CCE the PDCCH power boosting level  shall be randomly generated using the uniform distribution in the [Pmin, Pmax] range. The Pmin is equal to -6 dB, the Pmax is equal to 6 dB. The random values should be derived in the dB scale.

2)Additional power normalization is applied for each generated i-th PDCCH power boosting level:

where  and  are the PDCCH power boosting coefficients before and after normalization in the dB scale; the power normalization factor α is equal to 1.3 dB.

3)The normalized PDCCH power boosting coefficients  are further applied to the PDCCH_RA and PDCCH_RB values to derive the EPRE ratio of the PDCCH signals transmitted in the REs corresponding the i-th CCE in each subframe.

## B.8Burst transmission models for Frame structure type 3

This clause provides a description for burst transmission models for Frame structure type 3.

## B.8.1Burst transmission model for one LAA SCell

One burst is defined as downlink transmissions which occupy one or more consecutive subframes. The burst transmission format is determined according to the steps below:

1)Select the number of subframes  randomly from a given set of the number of subframes  with equal probability as the total length of burst transmission format. The length includes both occupied OFDM symbols and non-occupied OFDM symbols within the burst format.   is given per test case. NS1S1

2)If  is equal to 1, the subframe is set as fully occupied, otherwise:N

-For demodulation test, the starting position for the first subframe is randomly selected from OFDM symbol 0 and OFDM symbol 7 with equal probability. For CSI test, the starting position for the first subframe is OFDM symbol 0.

-The configuration of occupied OFDM symbols in the last subframe is randomly selected from configuration set . is given per test case.S2 S2

A uniform random variable from [0, 1] is generated. If the random variable is less than p which is given per test case,

-If both the last subframe of previous burst and first subframe of new burst format are fully occupied, start burst transmission after deferring one subframe from the last subframe of previous burst. Otherwise, start burst transmission at the end of last subframe of previous burst.

Otherwise, the burst transmission is muted and the muting duration is the same as the number of subframes for determined burst format.

## B.8.2Burst transmission model for multiple LAA SCell(s)

This clause provides a description for burst transmission models for Frame structure type 3 when there are multiple LAA Scell(s) in the test.

One burst is defined as downlink transmissions which occupy one or more consecutive subframes. Assuming M carriers are configured, the burst transmission format is determined according to the steps below:M

1)For each carrier cm (m=0,⋯, M-1), select the number of subframes Nm randomly from a given set of the number of subframes S1 with equal probability as the total length of burst transmission format used for carrier cm. The length includes both occupied OFDM symbols and non-occupied OFDM symbols within the burst format. S1 is given per test case.

2)If any Nm is equal to 1, the first subframe is set as fully occupied for all carriers, otherwise:

-For demodulation test, the starting position for the first subframe is randomly selected from OFDM symbol 0 and OFDM symbol 7 with equal probability. For CSI test, the starting position for the first subframe is OFDM symbol 0. The starting position is common for all carriers.

-The configuration of occupied OFDM symbols in the last subframe is randomly selected from configuration set S2 for each carrier cm. S2 is given per test case.

A uniform random variable pm from [0, 1] is generated for each carrier cm to determine whether the burst is transmitted or not on each carrier.

For each carrier cm, if pm is less than p which is given per test case,

-If both the last subframe of previous longest transmitted burst over M carriers and first subframe of new burst format are fully occupied, start burst transmission according to the determined burst transmission format for this carrier after deferring one subframe from the last subframe of previous longest transmitted burst. Otherwise, start burst transmission for this carrier at the end of last subframe of previous longest transmitted burst.

Otherwise, the burst transmission is muted and the muting duration is Nmax and Nmax is the maximum of Nj wherein j∈{0,1,⋯,M-1} and pj is less than p.

## Annex C (normative): Downlink Physical Channels

## C.1General

This annex specifies the downlink physical channels that are needed for setting a connection and channels that are needed during a connection.

## C.2Set-up

Table C.2-1 describes the downlink Physical Channels that are required for connection set up.

Table C.2-1: Downlink Physical Channels requiredfor connection set-up

## C.3Connection

The following clauses, describes the downlink Physical Channels that are transmitted during a connection i.e., when measurements are done.

## C.3.1Measurement of Receiver Characteristics

Unless otherwise stated, Table C.3.1-1 is applicable for measurements on the Receiver Characteristics (clause 7).

Table C.3.1-1: Downlink Physical Channels transmitted during a connection (FDD and TDD)

NOTE 1:No boosting is applied.

For measurements on cells in TDD Band 46, Table C.3.1-1a is applicable for measurements of Receiver Characteristics (clause 7).

Table C.3.1-1a: Downlink Physical Channels transmitted during a connection (TDD Band 46)

Table C.3.1-2: Power allocation for OFDM symbols and reference signals

## C.3.2Measurement of Performance requirements

Table C.3.2-1 is applicable for measurements in which uniform RS-to-EPRE boosting for all downlink physical channels, unless otherwise stated.

Table C.3.2-1: Downlink Physical Channels transmitted during a connection (FDD and TDD and Frame structure Type 3)

NOTE 1:A= B = 0 dB means no RS boosting.

NOTE 2:MBSFN RS and OCNG are not defined downlink physical channels in [4].

NOTE 3: Assuming PSS and SSS transmitted on a single antenna port.

NOTE 4: A, B, , and δ are test specific.

NOTE 5: Void.

NOTE 6: For Frame Structure Type 3, PBCH are not defined.

Table C.3.2-2: Power allocation for OFDM symbols and reference signals

## C.3.3Aggressor cell power allocation for Measurement of Performance Requirements when ABS is Configured

For the performance requirements and channel state information reporting when ABS is configured, the power allocation for the physical channels of the aggressor cell in non-ABS and ABS is listed in Table C.3.3-1.

Table C.3.3-1: Downlink physical channels transmitted in aggressor cell when ABS is configured in this cell

Table C.3.3-2: Downlink physical channels transmitted in aggressor cell when ABS is configured in this cell when the CRS assistance information is provided

## C.3.4Power Allocation for Measurement of Performance Requirements when Quasi Co-location Type B: same Cell ID

For the performance requirements related to quasi-colocation type B behaviour when transmission points share the same Cell ID, the power allocation for the physical channels of the serving cell is listed in Table C.3.4-1 and the power allocation for the physical channels of the cell transmitting PDSCH is listed in Table C.3.4-2

Table C.3.4-1: Downlink physical channels transmitted in the serving cell (TP1)

NOTE 1:A= B = 0 dB means no RS boosting.

NOTE 2: Assuming PSS and SSS transmitted on a single antenna port.

NOTE 3: A, B and  are test specific.

Table C.3.4-2: Downlink physical channels for the transmission point transmitting PDSCH (TP2)

## C.3.5Simplified CA testing method

For CA tests which require more than 16 independent faders, if a test system cannot support a throughput measurement with fading on all carriers simultaneously, the simplified CA testing method shall be used.

In the simplified CA testing method, the resulting propagation channel(s) shall be generated by considering a number of independent faders needed for one carrier and connecting them to the signal of randomly chosen carrier(s). The maximum number of channel faders on the test will be less than or equal to 16. The remaining carrier(s) shall be connected without a channel fader but with AWGN. The throughput is then collected only for the carrier(s) connected to channel faders.

In the simplified CA testing method, the test shall be repeated by choosing carrier(s) excluding already chosen carrier(s) until all the carrier(s) are tested under fading conditions. All the collected throughtputs from each carrier shall be compared against the reference value of the requirements.

All supported carriers shall be configured and activated during the test.

## C.3.6Measurement of Receiver Characteristics for Narrowband IoT

For the performance requiremens for Narrowband IoT, the power allocation for the physical channels is listed in Table C.3.6-1

Table C.3.6-1: Downlink Physical Channels transmitted during a connection

NOTE 1:Assuming NPSS and NSSS transmitted on one NRS antenna port.

Table C.3.6-2: Power allocation for OFDM symbols and reference signals

## Annex D (normative): Characteristics of the interfering signal

## D.1General

Unless otherwise stated, when the channel bandwidth is wider or equal to 5MHz, a modulated 5MHz full bandwidth E-UTRA downlink signal and CW signal are used as interfering signals when RF performance requirements for E-UTRA UE receiver are defined. For channel bandwidths below 5MHz, the bandwidth of modulated interferer should be equal to bandwidth of the received signal.

For Band 46, the bandwidth of interfering signal is 20MHz when RF performance requirements for E-UTRA UE receiver are defined.

## D.2Interference signals

Table D.2-1 describes the modulated interferer for different channel bandwidth options.

Table D.2-1: Description of modulated E-UTRA interferer

Table D.2-2 describes the modulated interferer setting 2 for different channel bandwidth options for Band 46.

Table D.2-2: Description of modulated E-UTRA interferer for Band 46

## Annex E (normative): Environmental conditions

## E.1General

This normative annex specifies the environmental requirements of the UE. Within these limits the requirements of the present documents shall be fulfilled.

## E.2Environmental

The requirements in this clause apply to all types of UE(s).

## E.2.1Temperature

The UE shall fulfil all the requirements in the full temperature range of:

Table E.2.1-1

Outside this temperature range the UE, if powered on, shall not make ineffective use of the radio frequency spectrum. In no case shall the UE exceed the transmitted levels as defined in clause 6.2 for extreme operation.

## E.2.2Voltage

The UE shall fulfil all the requirements in the full voltage range, i.e. the voltage range between the extreme voltages.

The manufacturer shall declare the lower and higher extreme voltages and the approximate shutdown voltage. For the equipment that can be operated from one or more of the power sources listed below, the lower extreme voltage shall not be higher, and the higher extreme voltage shall not be lower than that specified below.

Table E.2.2-1

Outside this voltage range the UE if powered on, shall not make ineffective use of the radio frequency spectrum. In no case shall the UE exceed the transmitted levels as defined in clause 6.2 for extreme operation. In particular, the UE shall inhibit all RF transmissions when the power supply voltage is below the manufacturer declared shutdown voltage.

## E.2.3Vibration

The UE shall fulfil all the requirements when vibrated at the following frequency/amplitudes.

Table E.2.3-1

Outside the specified frequency range the UE, if powered on, shall not make ineffective use of the radio frequency spectrum. In no case shall the UE exceed the transmitted levels as defined in TS 36.101 for extreme operation.

## Annex F (normative): Transmit modulation

## F.1Measurement Point

Figure F.1-1 shows the measurement point for the unwanted emission falling into non-allocated RB(s) and the EVM for the allocated RB(s).

DFT IFFT TX    Front--end Channel RF correction FFT Tx-Rx chain equalizer In-band emissions meas. EVM meas. 0 0 IDFT DUT  Test equipment      PUCCH and   DM-RS der test after the IDFT ispred to QPSK constellation points nal under test after the IDFT is not QPSK modulated in generalEVM meas. PUCCH and DM-RSTone  mapPUSCH modulated symbolsDFT IFFT TX    Front--end Channel RF correction FFT Tx-Rx chain equalizer In-band emissions meas. EVM meas. 0 0 IDFT DUT  Test equipment      PUCCH and   DM-RS der test after the IDFT ispred to QPSK constellation points nal under test after the IDFT is not QPSK modulated in generalEVM meas. PUCCH and DM-RSTone  mapPUSCH modulated symbols

Figure F.1-1: EVM measurement points

## F.2Basic Error Vector Magnitude measurement

The EVM is the difference between the ideal waveform and the measured waveform for the allocated RB(s)

,

where

is a set of  modulation symbols with the considered modulation scheme being active within the measurement period,

are the samples of the signal evaluated for the EVM,

is the ideal signal reconstructed by the measurement equipment, and

is the average power of the ideal signal. For normalized modulation symbols  is equal to 1.

The basic EVM measurement interval is defined over one slot in the time domain for PUCCH and PUSCH and over one preamble sequence for the PRACH.

## F.3Basic in-band emissions measurement

The in-band emissions are a measure of the interference falling into the non-allocated resources blocks. The in-band emission requirement is evaluated for PUCCH and PUSCH transmissions. The in-band emission requirement is not evaluated for PRACH transmissions.

The in-band emissions are measured as follows

,

where

is a set of SC-FDMA symbols with the considered modulation scheme being active within the measurement period,

is the starting frequency offset between the allocated RB and the measured non-allocated RB (e.g.  or  for the first adjacent RB),

(resp. ) is the lower (resp. upper) edge of the UL system BW,

and  are the lower and upper edge of the allocated BW, and

is the frequency domain signal evaluated for in-band emissions as defined in the subsection (ii)

The relative in-band emissions are, given by

where

is the number of allocated RBs

The basic in-band emissions measurement interval is defined over one slot in the time domain. When the PUSCH or PUCCH transmission slot is shortened due to multiplexing with SRS, the in-band emissions measurement interval is reduced by one SC-FDMA symbol, accordingly.

In the evaluation of in-band emissions, the timing is set according to , where sample time offsets  and  are defined in subclause F.4.

## F.4Modified signal under test

Implicit in the definition of EVM is an assumption that the receiver is able to compensate a number of transmitter impairments.

The PUSCH data or PRACH or Physical Sidelink Channel signal under test is modified and, in the case of PUSCH or Physical Sidelink Channel data signal, decoded according to:

where

is the time domain samples of the signal under test.

The PUCCH or PUSCH or Physical Sidelink Channel demodulation reference signal or PUCCH data signal under test is equalised and, in the case of PUCCH data signal decoded according to:

where

is the time domain samples of the signal under test.

To minimize the error, the signal under test should be modified with respect to a set of parameters following the procedure explained below.

Notation:

is the sample timing difference between the FFT processing window in relation to nominal timing of the ideal signal.

is the RF frequency offset.

is the phase response of the TX chain.

is the amplitude response of the TX chain.

In the following  represents the middle sample of the EVM window of length  (defined in the next subsections) or the last sample of the first window half if is even.

The EVM analyser shall

detect the start of each slot and estimate  and ,

determine  so that the EVM window of length  is centred

on the time interval determined by the measured cyclic prefix minus 16 samples of the considered OFDM symbol for symbol 0 for normal CP, i.e. the first 16 samples of the CP should not be taken into account for this step. In the determination of the number of excluded samples, a sampling rate of 30.72MHz was assumed. If a different sampling rate is used, the number of excluded samples is scaled linearly.

on the measured cyclic prefix of the considered OFDM symbol symbol for symbol 1 to 6 for normal CP and for symbol 0 to 5 for extended CP.

on the measured preamble cyclic prefix for the PRACH

To determine the other parameters a sample timing offset equal to  is corrected from the signal under test. The EVM analyser shall then

correct the RF frequency offset for each time slot, and

apply an FFT of appropriate size. The chosen FFT size shall ensure that in the case of an ideal signal under test, there is no measured inter-subcarrier interference.

The carrier leakage shall be removed from the evaluated signal before calculating the EVM and the in-band emissions; however, the removed relative carrier leakage power also has to satisfy the applicable requirement.

At this stage the allocated RBs shall be separated from the non-allocated RBs. In the case of PUCCH and PUSCH EVM, the signal on the non-allocated RB(s), , is used to evaluate the in-band emissions.

Moreover, the following procedure applies only to the signal on the allocated RB(s).

In the case of PUCCH and PUSCH and Physical Sidelink Channel, the UL EVM analyzer shall estimate the TX chain equalizer coefficients and  used by the ZF equalizer for all subcarriers by time averaging at each signal subcarrier of the amplitude and phase of the reference and data symbols. The time-averaging length is 1 slot. This process creates an average amplitude and phase for each signal subcarrier used by the ZF equalizer. The knowledge of data modulation symbols may be required in this step because the determination of symbols by demodulation is not reliable before signal equalization.

In the case of PRACH, the UL EVM analyzer shall estimate the TX chain coefficients and  used for phase and amplitude correction and are seleted so as to minimize the resulting EVM. The TX chain coefficients are not dependent on frequency, i.e.  and . The TX chain coefficient are chosen independently for each preamble transmission and for each .

At this stage estimates of , ,  and  are available.  is one of the extremities of the window , i.e. can be  or , where  if  is odd and  if is even. The EVM analyser shall then

calculate EVMl with  set to ,

calculate EVMh with  set to .

## F.5Window length

## F.5.1Timing offset

As a result of using a cyclic prefix, there is a range of, which, at least in the case of perfect Tx signal quality, would give close to minimum error vector magnitude. As a first order approximation, that range should be equal to the length of the cyclic prefix. Any time domain windowing or FIR pulse shaping applied by the transmitter reduces the  range within which the error vector is close to its minimum.

## F.5.2Window length

The window length  affects the measured EVM, and is expressed as a function of the configured cyclic prefix length. In the case where equalization is present, as with frequency domain EVM computation, the effect of FIR is reduced. This is because the equalization can correct most of the linear distortion introduced by the FIR. However, the time domain windowing effect can’t be removed.

## F.5.3Window length for normal CP

The table below specifies the EVM window length at channel bandwidths 1.4, 3, 5, 10, 15, 20 MHz, for normal CP. The nominal window length for 3 MHz is rounded down one sample to allow the window to be centered on the symbol.

Table F.5.3-1 EVM window length for normal CP

## F.5.4Window length for Extended CP

The table below specifies the EVM window length at channel bandwidths 1.4, 3, 5, 10, 15, 20 MHz, for extended CP. The nominal window lengths for 3 MHz and 15 MHz are rounded down one sample to allow the window to be centered on the symbol.

Table F.5.4-1 EVM window length for extended CP

## F.5.5Window length for PRACH

The table below specifies the EVM window length for PRACH preamble formats 0-4.

Table F.5.5-1 EVM window length for PRACH

## F.5.FWindow length for category NB1

The EVM window length, W, for NPUSCH is set to 1 (in FFT samples where the nominal FFT size is 128 for 15 kHz sub-carrier spacing and 512 for 3.75 kHz sub-carrier spacing).

The EVM window length, W, for NPRACH is set to 110 for preamble format 0 and to 494 for preamble format 1 (both in FFT samples where the nominal FFT size is 512).

## F.6Averaged EVM

The general EVM is averaged over basic EVM measurements for n slots in the time domain.

,

where n is

n = 20 for PUCCH, PUSCH, PSDCH, PSCCH, and PSSCH,

n = 48 for PBSCH.

The EVM requirements shall be tested against the maximum of the RMS average at the window W extremities of the EVM measurements:

Thus  is calculated using in the expressions above and is calculated using .

Thus we get:

The calculation of the EVM for the demodulation reference signal, , follows the same procedure as calculating the general EVM, with the exception that the modulation symbol set  defined in clause F.2 is restricted to symbols containing uplink demodulation reference signals.

The basic  measurements are first averaged over 20 slots in the time domain to obtain an intermediate average .

In the determination of each , the timing is set to  if , and it is set to  otherwise, where  and  are the general average EVM values calculated in the same 20 slots over which the intermediate average  is calculated. Note that in some cases, the general average EVM may be calculated only for the purpose of timing selection for the demodulation reference signal EVM.

Then the results are further averaged to get the EVM for the demodulation reference signal, ,

The PRACH EVM, , is averaged over two preamble sequence measurements for preamble formats 0, 1, 2, 3, and it is averaged over 10 preamble sequence measurements for preamble format 4.

The EVM requirements shall be tested against the maximum of the RMS average at the window W extremities of the EVM measurements:

Thus  is calculated using  and is calculated using .

Thus we get:

## F.6.FAveraged EVM for category NB1

The general EVM for category NB1 is calculated using the procedure defined in Annex F.6 with the exception that the general EVM is averaged over basic EVM measurements for 240/LCtone slots in the time domain, where LCtone = {1, 3, 6, 12} is the number of subcarriers for the transmission.

The calculation of the EVM for the demodulation reference symbols for category NB1 follows the procedure defined for DMRS in Annex F.6 with the exception that the basic EVM DMRS measurements are first averaged over 240/ LCtone slots to obtain the intermediate average EVM.

The calculation of the NPRACH EVM for both formats follows the procedure defined for PRACH in Annex F.6 with the exception that EVM PRACH is averaged over 64 preamble measurements.

## F.7Spectrum Flatness

The data shall be taken from FFT coded data symbols and the demodulation reference symbols of the allocated resource block.

## Annex G (informative): Reference sensitivity level in lower SNR

This annex contains information on typical receiver sensitivity when HARQ transmission is enabled allowing operation in lower SNR regions (HARQ is disabled in conformance testing), thus representing the configuration normally used in live network operation under noise-limited conditions.

## G.1General

The reference sensitivity power level PSENS with HARQ retransmission enabled (operation in lower SNR) is the minimum mean power applied to both the UE antenna ports at which the residual BLER after HARQ shall meet the requirements for the specified reference measurement channel. The residual BLER after HARQ transmission is defined as follows:

: Number of correctly decoded MAC PDUs

: Number of transmitted MAC PDUs (Retransmitted MAC PDUs are not counted)

## G.2Typical receiver sensitivity performance (QPSK)

The residual BLER after HARQ shall be lower than 1% for the reference measurement channels as specified in Annexes G.3 (with one sided dynamic OCNG Pattern OP.1 FDD/TDD for the DL-signal as described in Annex A.5.1.1/A.5.2.1) with parameters specified in Table G.2-1 and Table G.2-2

Table G.2-1: Reference sensitivity QPSK PSENS

Table G.2-2 specifies the minimum number of allocated uplink resource blocks for which the reference receive sensitivity requirement in lower SNR must be met.

Table G.2-2: Minimum uplink configuration for reference sensitivity

Unless given by Table G.2-3, the minimum requirements specified in Tables G.2-1 and G.2-2 shall be verified with the network signalling value NS_01 (Table 6.2.4-1) configured.

Table G.2-3: Network Signalling Value for reference sensitivity

## G.3Reference measurement channel for REFSENSE in lower SNR

Tables G.3-1 and G.3-2 are applicable for Annex G.2 (Reference sensitivity level in lower SNR).

Table G.3-1 Fixed Reference Channel for Receiver Requirements (FDD)

Table G.3-2 Fixed Reference Channel for Receiver Requirements (TDD)

## Annex H (normative): Modified MPR behavior

## H.1Indication of modified MPR behavior

This annex contains the definitions of the bits in the field modifiedMPRbehavior indicated in the IE UE Radio Access Capability [7] by a UE supporting an MPR or A-MPR modified in a later release of this specification.

Table H.1-1: Definitions of the bits in the field modifiedMPRbehavior

## Annex I (normative): Supported Post Antenna Gain

## I.1Declared Supported Post Antenna Gain for UE

For V2X service at band 47, some regional requirements (region 1) are defined per effective isotropic radiated power (EIRP), which is a combination of the transmitted power (or in some cases spectral density) and the effective antenna gain.

Due to large form factor, V2X UE can have external antenna placed far away from the chipset unit. In this case, the effective antenna gain is a UE specific condition. This effective antenna gain includes the feeding loss of all components after the chipset unit antenna connector and the peak directional gain of the external antenna and hence will be call the post connector gain Gpost connector.

The 3GPP specifications mandate UE manufacturer declarations of at least one supported value of the post connector gain Gpost connector as a way to accommodate the refered regional requirement without putting requirements on the UE specific condtion.

The possible values of declared supported post connector gains are: 0, 1, 2, 3, 4, 5, 6, 7 dBi. If no value is declared, or if external antenna is not used, the default value of 0dBi will be used.

The regional requirements in PEIRP in Subclauses 6.2.2G, 6.2.5G, 6.6.2.2.4, 6.6.3.2 and 7.9.1 will be converted to conducted requirements by subtracting Gpost connector as.

PConducted = PEIRP - Gpost connector.

## Annex J (informative): Change history

Table J.1: Change History
