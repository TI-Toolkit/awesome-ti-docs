Cellsheet uses small font 0x24 (`$` in small font, `⁴` in large) as its `$` instead of 0xF2 `$`.

Small font 0x06 ` ` (4-pixel space on mono, 8-pixels on color) is used in the status bar on the CE.

On monochrome calculators the only use of font character 0xDE `))` is in the `Logistic` interface to fit the entire equation ` y=c/(1+ae^(~bx))` on a single line.  Despite the screen being wider, color screen models continue to use 0xDE in this interface.

TI Connect CE supports no fewer than five different characters for the `theta` token usable in program or list names: U+03B8, U+0398, U+03D1, U+03F4, U+1DBF

Due to an OS bug, starting an Appvar name with lowercase `r` (_font_ 0x72) hides it from the memory menu because it hits the OS filtering to hide the Ans variable (_token_ 0x72)

`SortA(` and `SortD(` are substantially faster after 5.1.0
