# Hardware for 4th year project

This document contains short descriptions and hardware suggestions for optics project.



## Interfaces

* JESD204B - standard interface between ADCs/DACs and FPGAs/ASICs up to 12.5Gbps
* JESD204C - updated standard up to 32Gbps, compatable with JESD204B
* Parallel LVDS (also sometimes used for high performance ADCs/DACs, also uses FMC connector)
* FMC - (FPGA Mezzanine Card) a physical connection, comes in LPC and HPC (Low/High pin count), up to 10Gbps
* FMC+ - faster version of FMC, up to 28Gbps
* Samtech BullsEye - physical analogue connector (similar to SMC except array of 6 to 32 pins and up to 70GHz)
* Z-Ray - 28Gbps low profile connector

Most common is JESD204B with FMC/FMC+ connectors, therefore we're looking FPGA with two of these connectors or builtin ADC/DAC.

## ADCs/DACs

Analog Devices Boards:

 * [Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/AD9174.pdf)
 * 16Bit
 * 12.6GPS

TI DAC38RF82EMV DAC Board:
 * [Page](https://www.ti.com/tool/DAC38RF82EVM)
 * JESD204B
 * 14Bit
 * 9GSPS

TI ADC12DJ5200RFEVM ADC Board:
 * [Page](https://www.ti.com/tool/ADC12DJ5200RFEVM)
 * JESD204B/C
 * 12Bit
 * 10.4GSPS

Analog Devices EVAL-AD916X DAC:
 * [Page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD916X.html)
 * [Datasheet/Userguide](https://www.analog.com/media/en/technical-documentation/user-guides/AD9161-9162-9163-9164-UG-1526.pdf)
 * JESD204B
 * 16Bit
 * 12GSPS

Abaco FMC172:
 * [Page](https://www.abaco.com/products/fmc172-fpga-mezzanine-card)
 * Has both builtin ADC and DAC
 * 6.4GBPS ADC
 * 6GBPS DAC
 * 10Bit
 * LVDS interface
 * Supported IPs

Hitech 12ADC-16DAC
 * [Page](http://www.hitechglobal.com/FMCModules/12-bitADC_10Gsps.htm)
 * Has both ADC and DAC
 * 12bit 10.25GSPS ADC
 * 16bit 12.6GSPS DAC (dual)
 * FMC+ JESD204B interface
 * Supported IPs

### Useful links:
 * [Xilinx FMC cards](https://www.xilinx.com/products/boards-and-kits/fmc-cards.html)
 * [Abaco FMC cards](https://www.abaco.com/products/fpga-mezzanine-cards-fmc)
 * [Hitech FMC cards](www.hitechglobal.com/Accessories/FMC_Modules.htm)

## FPGAs

Intel Arria 10 family:
 * [Page](https://www.intel.com/content/www/us/en/products/programmable/fpga/arria-10.html)
 * Number of boards
 * DDR4 memory
 * Floating Point DSPs


Xilinx ZCU102:
  * [Page](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html)
  * [User Guide](https://www.xilinx.com/support/documentation/boards_and_kits/zcu102/ug1182-zcu102-eval-bd.pdf)
  * 2X FMC, 8GTH each (GTH transeiver has max performance of 16.3Gbps)
  * Most commonly used in relavent papers
  * DDR4 memory
