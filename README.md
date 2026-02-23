# Awesome TI Docs
A collection of awesome calculator documentation resources and tools from all over the web, all in one place. Contributions welcome.
| **Icon** | **Models** |
| -- | -- |
| 🎹 | <details><summary>Monochrome z80</summary> <ul><li>TI-82</li><li>TI-83</li><li>TI-83+</li><li>TI-84+</li></ul></details> |
| 🎨 | TI-84+CSE |
| 🌈 | <details><summary>Color ez80</summary> <ul><li>TI-84+CE (-T)</li><li>TI-83 PCE</li><li>Python variants of the above.</li><li>TI-82 AEP</li></ul></details> |
| 🎈 | TI-Nspire |

## Contents

- [I want to...](#i-want-to)
  - [...engage with the community](#engage-with-the-community)
  - [...run programs on my calculator](#run-programs-on-my-calculator)
  - [...learn TI-BASIC](#learn-ti-basic)
  - [...learn assembly for my calculator](#learn-assembly-for-my-calculator)
  - [...write programs in C for my calculator](#write-programs-in-c-for-my-calculator)
  - [...write and run programs on my computer](#write-and-run-programs-on-my-computer)
  - [...learn more about my calculator's hardware](#learn-more-about-my-calculators-hardware)
- [All Resources](#all-resources)
  - [ASM](#asm)
  - [TI-BASIC](#ti-basic)
  - [C/C++](#cc)
  - [Hardware](#hardware)
  - [Emulators](#emulators)
  - [Downloads](#downloads)
  - [Tools](#tools)
  - [Other](#other)

## I want to...

### ...engage with the community
*This list is specifically limited to communities with a strong TI focus. If an invite link breaks, [please make an issue](https://github.com/TI-Toolkit/awesome-ti-docs/issues/new).* 
- [Cemetech](https://cemetech.net) - [Forum](https://cemetech.net), On-site chat, [Discord](https://discord.gg/FqtkgRaupc) - **EN**  
  Cemetech is a forum for sharing hardware and software projects of all kinds, with a special emphasis on TI calculators. It has several on-site tools.
- [MyCalcs](https://my.calcs.quest)  
  Calculator enthusiasts should register their calcs on MyCalcs, a community site for cataloging and exploring the history of your calculators and their accessories.
- [TI-Planet](https://tiplanet.org) - [Forum](https://tiplanet.org), On-site chat, [Discord](https://discord.gg/67t9G5HkDA) - **FR, EN**  
  TI-Planet is a French forum dedicated to all calculators, especially TI models. It offers a variety of on-site tools and a large international community.
- [CE Programming Discord](https://discord.gg/z4zjNcr5Tt) - **EN**  
  For technical support regarding the (CEmu, C/C++ Toolchain for the CE), please visit the Discord or either of the forums above.
- [TI Toolkit Discord](https://discord.gg/VEzwDfZFVe) - **EN**  
  Please visit our Discord or either of the forums above for assistance with [our family of tools and libraries](https://github.com/TI-Toolkit). It is also a great place to start if you want to contribute to our projects.


### ...run programs on my calculator

- [arTIfiCE](https://yvantt.github.io/arTIfiCE/) - 🌈  
  If you have a newer 84+CE/83PCE (at least OS 5.5), arTIfiCE can be used to unlock the ability to run ASM programs.
- [TILP](https://github.com/debrouxl/tilp_and_gfm/) - 🎹 🎨 🌈 🎈  
  TILP can be used as an alternative to TI's official software for sending/receiving files to/from most calculators.
- [WebTILP](https://web.tilp.info/) - 🎹 🎨 🌈 🎈  
  WebTILP is a web version of TILP so you can do transfers etc. directly from your browser with no install required.
- [N-Link](https://lights0123.com/n-link/) - 🎈  
  N-Link can be used as an alternative to TI's official software for sending/receiving files to/from the Nspire.
- [Cemetech](https://www.cemetech.net/) - 🎹 🎨 🌈 🎈  
  Cemetech hosts a program archive and forum pertaining to calculators of all varieties.
- [ticalc](https://www.ticalc.org/) - 🎹 🎨 🌈 🎈  
  ticalc is the go-to site to download calculator programs or upload your own.
- [TI-Planet](https://tiplanet.org/forum/portal.php) - 🎹 🎨 🌈 🎈  
  TI-Planet hosts a program archive and forum with many online tools and a large international userbase.

### ...learn TI-BASIC

- [TI-Basic Starter Kit](http://tibasicdev.wikidot.com/starter-kit) - 🎹 🎨 🌈 🎈  
  TI-Basic Developer's Starter Kit is a fantastic community-developed guide through the fundamentals of TI-BASIC, with culminating sample programs to test your understanding.
- [TI-BASIC Programming Guide](https://education.ti.com/-/media/377A0772C3B04D83B83D2A4E51029D08) - 🌈  
  TI also provides an extensive and pedagogically-rich TI-BASIC tutorial.
- [Code Fragments and Useful Routines](https://www.cemetech.net/forum/viewtopic.php?t=1642) - 🎹 🎨 🌈  
  This community collection of optimized idioms and routines is essential for writing concise and effective TI-BASIC code.
- [84+CE Catalog](https://education.ti.com/html/webhelp/EG_TI84PlusCE/EN/Subsystems/e-guide_ref84plus_en/content/m_appxa/aa_appxalpha.HTML) & [83PCE Catalog](https://education.ti.com/html/webhelp/EG_TI83PremCE/FR/Subsystems/e-guide_83prem_ce_fr/content/m_appxa/aa_appxalpha.HTML) - 🌈  
  TI provides documentation for every token on the calculator's built-in catalog, which you can also view online.

### ...learn assembly for my calculator

- [Learn TI-83+ Assembly in 28 Days](https://taricorp.gitlab.io/83pa28d/index.html) (modernized version) &bull; Original version: [on ticalc.org](https://www.ticalc.org/archives/files/fileinfo/268/26877.html), and [web-hosted](https://tutorials.eeems.ca/ASMin28Days/welcome.html). - 🎹  
  Assembly in 28 Days is the go-to tutorial for learning Z80 ASM; if you want to learn eZ80 as well, this guide is an essential starting point. <sup><sub>There is some work being done to create a replacement specifically for the eZ80 (i.e. the CE and variants) at https://ezce.github.io/ez80-docs/ but this is a work in progress.</sub></sub>
- [Z80 Opcode Table](https://clrhome.org/table/) (🎹) or [eZ80 Opcode Table](https://ez80.abeck.pw/) (🌈)  
  The opcode tables are great for learning ASM and reading hex code from others.
- [Z80 User Manual](https://www.zilog.com/docs/z80/um0080.pdf) (🎹) or [eZ80 User Manual](https://www.zilog.com/docs/um0077.pdf) (🌈)  
  Zilog, the makers of the (e)Z80, provide official documentation for their chips and ASM instructions.
- [TI-83+ Developer's SDK](https://education.ti.com/en/guidebook/details/en/830D08FF31804AEAA2F03B8F5E89AD14/83psdk) ([mirror](https://github.com/TI-Toolkit/awesome-ti-docs/tree/docs/sdk)) - 🎹  
  Official TI-83+ assembly documentation by TI. Many things apply to other calculators as well.
- [WikiTI](https://wikiti.brandonw.net/index.php?title=Calculator_Documentation) - 🎹 🎨 🌈  
  WikiTI hosts community-sourced documentation on TI-OS and how to interface with it in assembly.

### ...write programs in C for my calculator

- [CE Toolchain](https://ce-programming.github.io/toolchain/index.html) - 🌈  
  The CE toolchain provides the compiler and libraries necessary for writing C/C++ code for your calculator.
- [CEmu](https://ce-programming.github.io/CEmu/) - 🌈  
  The CEmu emulator is great for testing and debugging your code, as large errors can crash the calculator and clear your RAM.
- [Git Guide](https://www.cemetech.net/forum/viewtopic.php?t=16330) - 🌈  
  This guide provides all you need to know to use Git and GitHub to share and release your toolchain project.

### ...write and run programs on my computer

- [Wabbitemu](https://github.com/sputt/wabbitemu) (🎹), [jsTIfied](https://www.cemetech.net/projects/jstified/) (🎹 🎨), or [CEmu](https://ce-programming.github.io/CEmu/) (🌈)  
  These emulators for the 83+ series of calculators allow you to run programs on your computer using a copy of your calculator's ROM.
- [Firebird](https://github.com/nspire-emus/firebird) - 🎈  
  Nspire owners can find an emulator for their calculators in Firebird.
- [SourceCoder 3](https://www.cemetech.net/sc/) - 🎹 🎨 🌈  
  SourceCoder is an online IDE for TI-BASIC, ASM, and C/C++.
- [Project Builder](https://tiplanet.org/pb/) - 🌈  
  TI Planet's Project Builder is an online IDE for TI-BASIC, C/C++, and Python.
- [TokenIDE](https://www.cemetech.net/downloads/files/515/x515) - 🎹 🎨 🌈  
  If you'd like to go offline, TokenIDE is an IDE for TI-BASIC that supports libraries like DCS and xLibC.

### ...learn more about my calculator's hardware

- [WikiTI](https://wikiti.brandonw.net/index.php?title=Calculator_Documentation) - 🎹 🎨 🌈  
  WikiTI hosts community-sourced hardware documentation for the 83+ series of calculators.
- [Hardware Revisions](https://docs.google.com/spreadsheets/d/1N_2tBusqjVzefKb4impi-VwdM-RgOSIMmXBemJymxA0/edit#gid=0) - 🎹 🎨 🌈 🎈  
  This spreadsheet details every known version of hardware found in TI calculators, including prototype revisions.

## All Resources

### ASM

- [asm-docs](https://github.com/CE-Programming/asm-docs) - 🌈  
  ASM documentation, tutorials, and examples assembled by the CE toolchain team.
- [CE Versions](https://wiki.tiplanet.org/Versions_CE/en) - 🌈  
  Boot and OS versions for the TI-84+CE(-T) and TI-83PCE.
- [DCS Developer's SDK](https://dcs.cemetech.net/index.php?title=Developers%27_SDK) - 🎹 🎨  
  Documentation for Doors CS related assembly routines and formatting.
- [Direct USB](https://brandonw.net/calcstuff/DirectUSB.txt) - 🎹  
  Partial analysis of the USB protocol on the TI-84+.
- [eZ80 Docs](https://ezce.github.io/ez80-docs/) - 🌈  
  General documentation for assembly on the TI-84+CE (WIP).
- [eZ80 Opcode Table](https://ez80.abeck.pw/) - 🌈  
  Table of every eZ80 opcode.
- [eZ80 User Manual](https://www.zilog.com/docs/um0077.pdf) - 🌈  
  Official Zilog documentation of the eZ80 CPU.
- [Floating Point Hacks](https://www.cemetech.net/forum/viewtopic.php?p=274411) - 🎹 🎨 🌈  
  Trick to get real variables to point to places they shouldn't. 
- [Learn TI-83+ Assembly in 28 Days](https://taricorp.gitlab.io/83pa28d/index.html) (modernized version) &bull; Original version: [on ticalc.org](https://www.ticalc.org/archives/files/fileinfo/268/26877.html), and [web-hosted](https://tutorials.eeems.ca/ASMin28Days/welcome.html). - 🎹  
  Guide to learning assembly on the TI-83+; a useful starting point for writing assembly for other models.
- [Link Guide](http://merthsoft.com/linkguide/ti83+/) ([mirror](https://debrouxl.github.io/tilp-linkguide/)) - 🎹  
  Link protocol documentation for TI-83+/84+ calculators. Also contains useful documentation for variable formats.
- [TI-83+ Developer's SDK](https://education.ti.com/en/guidebook/details/en/830D08FF31804AEAA2F03B8F5E89AD14/83psdk) ([mirror](https://github.com/TI-Toolkit/awesome-ti-docs/tree/docs/sdk)) - 🎹  
  Official TI-83+ assembly documentation by TI. Many things apply to other calculators as well.
- [tilibs](https://github.com/debrouxl/tilibs) - 🎹 🎨 🌈 🎈  
  Libraries utilized by TiLP and other software to transfer and convert files between calculators.
- [WikiTI](https://wikiti.brandonw.net/index.php?title=Calculator_Documentation) - 🎹 🎨 🌈  
  Contains most of the documented system calls, along with other useful information pertaining to calculator software/hardware.
- [Z80 IDE](https://clrhome.org/asm/) - 🎹  
  Online IDE for Z80 ASM.
- [Z80 Opcode Table](https://clrhome.org/table/) - 🎹  
  Table of every Z80 opcode.
- [Z80 Optimized Routines](https://github.com/Zeda/Z80-Optimized-Routines) - 🎹  
  Expertly-crafted optimized routines for common algorithms, graphics, and mathematical operations (among other things).
- [Z80 User Manual](https://www.zilog.com/docs/z80/um0080.pdf) - 🎹  
  Official Zilog documentation of the Z80 CPU.

### TI-BASIC

- [84+CE Catalog (English)](https://education.ti.com/html/webhelp/EG_TI84PlusCE/EN/Subsystems/e-guide_ref84plus_en/content/m_appxa/aa_appxalpha.HTML) / [83PCE Catalog (French)](https://education.ti.com/html/webhelp/EG_TI83PremCE/FR/Subsystems/e-guide_83prem_ce_fr/content/m_appxa/aa_appxalpha.HTML) - 🌈  
  A copy of the Catalog for the TI-84+CE/TI-83PCE.
- Assembly Hex Codes for the [83+/84+](http://tibasicdev.wikidot.com/hexcodes) (🎹), [84+CSE](http://tibasicdev.wikidot.com/84cse:hexcodes) (🎨), and [84+CE](http://tibasicdev.wikidot.com/84ce:hexcodes) (🌈)  
  Short assembly snippets that can be called from TI-BASIC using the `AsmPrgm` commands.
- [binomcdf( Shenanigans](https://www.cemetech.net/forum/viewtopic.php?t=17286) - 🎹 🎨 🌈  
  Exploration of a bug in the `binomcdf(` implementation between OS 1.03 and 5.6.1 that produces corrupted floats.
- [Celtic CE Documentation](https://roccoloxprograms.github.io/CelticCE) - 🌈  
  Documentation of the third-party TI-BASIC library Celtic CE.
- [Code Fragments and Useful Routines](https://www.cemetech.net/forum/viewtopic.php?t=1642) - 🎹 🎨 🌈  
  Various useful routines for TI-BASIC programs.
- [DCS Developer's SDK](https://dcs.cemetech.net/index.php?title=Developers%27_SDK) - 🎹 🎨  
  Documentation of third-party TI-BASIC libraries included in Doors CS/CSE.
- [Error Messages](https://education.ti.com/html/webhelp/EG_TI84PlusCE/UK/Subsystems/eg_ti84plusce_ref/content/m_errors/em_errormessages.HTML) - 🎹 🎨 🌈  
  TI's reference for the possible error types and messages on the CE.
- [For( Documentation](https://github.com/TI-Toolkit/awesome-ti-docs/blob/docs/for_documentation.md) - 🎹 🎨 🌈  
  Documentation of strange behavior of the `For(` command.
- [A Guide to Code Golf in TI-BASIC](https://gist.github.com/tkwa/f0c82e04e159d83e2321a736c95630f3) - 🎹 🎨 🌈  
  Replete guide with tips and tricks for TI-BASIC code golfing.
- [TEXTLIB](https://www.cemetech.net/downloads/files/1340/x1340) - 🎨 🌈  
  TI-BASIC library to enhance homescreen and graphscreen drawing capabilities.
- [TI-Basic Developer](http://tibasicdev.wikidot.com/) ([mirror](https://tibasicdev.github.io/)) - 🎹 🎨 🌈 🎈  
  Documentation and tutorials for TI-BASIC programming.
- [TI-Basic Programming Guide for the TI-84+CE](https://education.ti.com/html/eguides/graphing/84PlusCEPy/EN/content/eg_84prgm/m_splashpage/ti-progguide_ce.HTML) - 🌈  
  TI's own guide and command reference for programming in TI-BASIC. The eGuide also includes reference for other CE features and apps.
- [TI-BASIC Useful Routines](https://learn.cemetech.net/index.php?title=TI-BASIC:Useful_Routines) - 🎹 🎨 🌈  
  Useful routines for TI-BASIC programs.
- [tiopt](https://www.club.cc.cmu.edu/~ajo/ti/tiopt.html) - 🎹 🎨 🌈  
  Tool to perform simple optimizations of TI-BASIC programs.
- [QR Code Generator](https://tiplanet.org/scripts/qrcode/) - 🌈  
  QR code generator for use with TI-BASIC. Requires the accompanying [rendering program](https://tiplanet.org/forum/archives_voir.php?id=324393).
- [zText](https://tiplanet.org/scripts/zText/) - 🎹 🎨 🌈  
  Simple program generator for displaying text on the graphscreen.

### C/C++

- [CE Toolchain](https://ce-programming.github.io/toolchain/index.html) - 🌈  
  Documentation for the CE C/C++ toolchain. Includes all the information you need to start programming in C and C++ on the TI-84+CE.
- [Git Guide](https://www.cemetech.net/forum/viewtopic.php?t=16330) - 🌈  
  A short guide on using Git and GitHub angled toward projects which use the CE toolchain.

### Hardware

- [Hardware Revisions](https://docs.google.com/spreadsheets/d/1N_2tBusqjVzefKb4impi-VwdM-RgOSIMmXBemJymxA0/edit#gid=0) - 🎹 🎨 🌈 🎈  
  Documented hardware revisions, motherboards, and codenames for calculators and accessories.
- [Packaging Codes](https://docs.google.com/spreadsheets/d/1GumHduVgHWHIiJPKUKDZEtlZmMOOxRv2RqHLKyzRKos/edit#gid=0) - 🎹 🎨 🌈 🎈  
  Documented serial numbers and packaging codes.
- [Silver Link RE](https://www.cemetech.net/forum/viewtopic.php?p=302980) - 🎹 🎨 🌈  
  Documentation and schematics for the TI USB Graph Silver Link cable.
- [WikiTI](https://wikiti.brandonw.net/index.php?title=Calculator_Documentation) - 🎹 🎨 🌈  
  Contains hardware documentation for some TI (e)Z80 calculators.

### Emulators

- [CEmu](https://ce-programming.github.io/CEmu/) - 🌈  
  TI-84+CE emulator for Linux, macOS, and Windows.
- [Firebird](https://github.com/nspire-emus/firebird) - 🎈  
  TI-Nspire emulator for Android, iOS, Linux, macOS, and Windows.
- [jsTIfied](https://www.cemetech.net/projects/jstified/) - 🎹 🎨  
  Online calculator emulator for Z80 TI-83+/84+ calculators.
- [TilEm](http://lpg.ticalc.org/prj_tilem/) - 🎹  
  TI Z80 emulator and debugger for Linux, macOS, Windows, and other platforms that support GTK+.
- [Wabbitemu](https://github.com/sputt/wabbitemu) - 🎹  
  TI Z80 emulator for Android, Linux, macOS, and Windows.

### Downloads

- [Cemetech](https://www.cemetech.net/) - 🎹 🎨 🌈 🎈  
  Archive and forum site hosting discussion pertaining to calculators and other projects.
- [TI-Basic Developer](http://tibasicdev.wikidot.com/home) - 🎹 🎨 🌈 🎈  
  Archive and forum site with a focus on TI-BASIC.
- [ticalc](https://www.ticalc.org/) - 🎹 🎨 🌈 🎈  
  Replete archive of calculator programs and other files.
- [TI-Planet](https://tiplanet.org/forum/portal.php) - 🎹 🎨 🌈 🎈  
  Archive and forum site tailored to TI calculators with a large international community.

### Tools

- [1555 Color Picker](https://roccoloxprograms.github.io/1555ColorPicker/) - 🎨 🌈  
  Color picker which can use 1555 or 565 color mode, which can be useful for C/ASM and hybrid TI-BASIC on color calculators.
- [arTIfiCE](https://yvantt.github.io/arTIfiCE/) - 🌈  
  "Jailbreak" for the TI-84+CE/83PCE calculators necessary for running ASM programs on OS versions 5.5 and above.
- [FactoRoms](https://tiplanet.org/forum/factoroms.php) - 🎹 🎨 🌈 🎈  
  Online console ROM to calculator file conversion tool (requires TI Planet log-in).
- [fasmg manual](https://flatassembler.net/docs.php?article=fasmg_manual) - 🎹 🎨 🌈  
  Documentation and basic examples of flat assembler g language.
- [img2calc](https://tiplanet.org/forum/img2calc.php) - 🌈 🎈  
  Image converter for a number of calculator image file types.
- [mViewer GX Creator](https://tiplanet.org/gx) - 🎹 🎨 🌈 🎈  
  Online PDF/Image to calculator file conversion tool (requires TI Planet log-in).
- [nCreator](https://tiplanet.org/forum/edittns.php) - 🎈  
  Online rich text (Nspire Notes app) creation tool (requires TI Planet log-in).
- [N-Link](https://lights0123.com/n-link/) - 🎈  
  Free and open-source TI-Nspire transfer software for Linux, macOS, and Windows (no license required).
- [Project Builder](https://tiplanet.org/pb/) - 🌈  
  Online C/C++, TI-BASIC, and Python IDE for TI-84+CE/83PCE calculators.
- [SourceCoder 3](https://www.cemetech.net/sc/) - 🎹 🎨 🌈  
  Online IDE for TI-BASIC, (e)Z80 ASM, and C programs.
- [TILP](https://github.com/debrouxl/tilp_and_gfm/) - 🎹 🎨 🌈 🎈  
  Open-source calculator transfer software for most calculators and link cables.
- [WebTILP](https://web.tilp.info/) - 🎹 🎨 🌈 🎈  
  WebTILP is a web version of TILP so you can do transfers etc. directly from your browser with no install required.
- [tivars_lib_cpp](https://github.com/adriweb/tivars_lib_cpp)/[tivars_lib_py](https://github.com/TI-Toolkit/tivars_lib_py) - 🎹 🎨 🌈  
  Libraries for C++/Python to read and write var files used by TI-(e)Z80 calculators.
- [TokenIDE](https://www.cemetech.net/downloads/files/515/x515) - 🎹 🎨 🌈  
  Offline IDE for TI-BASIC with DCS and xLibC support.
- [xLibC Color Picker](https://roccoloxprograms.github.io/XlibcColorPicker/) - 🎨 🌈  
  Color picker which uses the xLibC palette, which can be useful for C/ASM and hybrid TI-BASIC on color calculators. You can upload a custom palette as well.

### Other

- [AXE Commands](https://axe.eeems.ca/Commands.html) - 🎹  
  Table of commands for the TI-83+/84+ programming language AXE, created by Kevin Horowitz.
- [AXE Documentation](https://axe.eeems.ca/Documentation.pdf) - 🎹  
  General documentation for AXE in PDF form.
- [ICE Documentation](http://petertillema.github.io/ICE/) - 🌈  
  Documentation for the TI-84+CE programming language ICE, created by Peter Tillema. Note: ICE is no longer in active development.
