Z80 Software Development Kit (SDK) for the TI-73 Explorer and TI-83 Plus
***************************************************************

Welcome to Z80 SDK (Build 29) for the TI-73 Explorer and TI-83 Plus.

This document describes the SDK for the TI-83 Plus. The software and 
documentation are provided to you in accordance with your license agreement.

For the latest information, see our web page at:
http://education.ti.com/developer/83/high/hilight.html

Contents

1. Introduction
2. System Requirements
3. Installation
4. Documentation Errata
5. Known Issues
6. Key Features
7. Tips for Best Use
8. Technical Support and Reporting Feedback

1. Introduction

The TI-73 Explorer/TI-83 Plus SDK consists of a software simulator/debugger and 
a Developer Guide. This SDK is for developers interested in learning 
about TI-73 Explorer/TI-83 Plus programming capabilities and developing applications 
or programs for the TI-73 Explorer and TI83 Plus.


2. System Requirements

TI-83 Plus Flash Debugger:
- Microsoft Windows* 98, ME, 2000, or XP.  
- IBM*-compatible (486 or higher)
- 32 MB of RAM or greater (64 MB recommended)
- 5 MB of available hard disk space (simulator only)
- VGA monitor with 800x600 resolution (or better)
- Adobe Acrobat Reader* 3.01 or higher installed
*All other brands and names are property of their respective owners. 

Wappsign:
- Microsoft Windows* 98, ME, 2000, or XP.  
- IBM*-compatible (486 or higher)
- 32 MB of RAM or greater (64 MB recommended)
- 5 MB of available hard disk space (simulator only)
- VGA monitor with 800x600 resolution (or better)
- Adobe Acrobat Reader* 3.01 or higher installed
*All other brands and names are property of their respective owners. 

3. Installation

   Double click on the self extracting file setup.exe.

4. Documentation Errata

- At this time, we provide limited information regarding application development for the TI-73.  There are several differences between TI-73 and TI-83 Plus that will be documented at a later time.  

    Updating Software

To get the latest update, check the following Internet address:
http://education.ti.com/developer/83/download/download.html


5. Known Issues

- While loading your application (*.hex file), make sure it is not being modified
  by any other program.
- Please make sure your application has a proper header.  The calculator assumes any 
  application with no/incorrect header to be the Operating System (OS).
- The debugger tends to use a lot of resources when running.  To ensure optimal system performance, make sure you halt the debugger before trying to use other applications.
- Wappsign is not supported on Windows 95 or Windows NT 4.0.  If you run either of these operating systems, you will need to use the appsign.bat file to sign your applications.
- The debugger includes support for USB communication.  Windows 95 and NT 4.0 do not support USB.

6. Key Features
- User Definable Key board interface.  The default mapping for the keyboard is in file 
  83pkeymap.cfg.  This file can be edited to map the keys as per convenience.
  The F5 key of the calculator is not mapped because this key is used by the simulator.
  (Note: The numeric keypad in laptops might be mapped differently)
- Ability to load 'asm' programs and other data types (eg. Lists).
- TI-83 Plus Silver Edition support.
- TI-73 support.
- Trace capability.
- Symbolic Debug Capability.
- Loading of Multiple applications is supported.
- Multi-paged applications are supported.
- Ability to read and generate .8xk and .73k files (developer key required to create .73k).

*New for Build 29:
- Floating point stack view shows values current pushed on the floating point stack.
- New skin for the TI-73 Explorer

*New for Build 28:
- USB interface
- OP Table View allows you to easily determine the contents of the OP1-OP6 RAM registers.
- Windows appsigning utility (Wappsign) replaces appsign.bat and supporting .exe files.  Appsign.bat is still provided for Windows 95/NT4.0 users.

*New for Build 24:
Debug Menu:
	- I/O tracing records data sent/recieved during link I/O.  Option to save to a text 	  file.
	- Address Watch Points allow you to stop the debugger when an address (either in 	  Flash or   RAM) has been read from, written to, or either.
	- Add delay.
View Menu:
	- Flash/RAM monitors - informs you when a location in either Flash or RAM has been 	  accessed.  If a location has not been accessed, it will contain 00, once it has 	  been accessed its contents will change to FF.  Selecting Clear RAM (or Flash) 	  Monitor sets all to 00.
	- RAM/Flash view windows have changed.  Now has physical and logic modes and ASCII 	  is in the same window.  Address field reflects the position of the cursor.  In  	  logic mode, addresses  are represented with page-offset.  For example OP1 in 	  	  logical RAM is page 1, offset 8478, so you would enter 18478 to view that address 	  (or you could enter OP1).  To view Flash page 15, you would enter 154000.  Right 	  click in the window to toggle between physical and logic modes.
	- I/O log shows you the bytes sent/recieved if Link I/O was enabled.
	- Symbol table - keeps track of variables.
Tools Menu:
	- Keypress recording/playback.  Ability to record a sequence of keypresses and play 	  them back at a specified rate (seconds between keypresses).
	- Save/Display/compare calculator screens.
	- This menu also available by right-clicking on the calculator window.
Link Menu:
	- Link I/O: ability to send/recieve data to external device (calculator, CBL, CBL2, 	  etc.)  via TI GRAPH LINK cable.

7. Tips for Use

- Close other applications while running the simulator.
- A faster PC will give better response on key presses and screen displays.

 
8. Technical Support and Reporting Feedback

If you wish to submit any issues, please use the Problem Report Form:
http://education.ti.com/global/forms/sdkproblemreport.html

If have other feedback please use the Feedback form:
http://education.ti.com/global/forms/sdkfeedback.html

Copyright 2003, Texas Instruments Inc.

