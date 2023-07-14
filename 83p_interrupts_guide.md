# The Guide to 83+ interrupts

By Joe Pemberton
Email: joe@joepnet.com
Revision 3
(C) 2000 Do not modify

If you are reading this, then you must be interested about those strange things
called interrupts that everyone talks about and use. I was too, and I couldn’t
find a good tutorial about interrupts, so I wrote one. This guide is designed
for the 83+, but parts of it can be adapted for other z80 calculators.

***WARNING* The interrupts are not a thing for newbies to ASM. Thus, if you are
a newbie you will most likely understand none of this. And probably crash your
calculator.**

Which reminds me… if by following this guide you crash your calculator (and you
most likely will at least once or twice) I am NOT responsible. You use this
guide at your own risk. I recommend backing up your calculator if you are going
to use it to test your interrupt programs. Or you could use VTI, either one
works.

Every 1/200 of a second, an interrupt is triggered by a piece of hardware. The
interrupt forces the CPU to stop whatever it's doing and run another routine.
Right before the CPU does this, though, it pushes the PC (program counter) onto
the stack so it can return to the exact same place it was at when the interrupt
occured. (NOTE: TI says the interrupt is triggered every 1/200 of a second. In
reality, it is somewhat closer to every 1/140 of a second.) In other words, it
"call"s the interrupt routine.

There are 3 different interrupt modes on the calculator- mode 0, mode 1 and mode
2. These modes are set by the commands IM 0, IM 1 and IM 2.

- Mode 0 - This mode can't be used on the calculator. What happens in mode 0 is
the CPU reads whatever instruction is on the data bus and executes it. Since
we can niether determine what is on the data bus nor provide an instruction
for the data bus, it is unusable.
- Mode 1 - This mode is the default interrupt mode. When an interrupt occurs,
code (located at $0038) is run. This code controls background things such as
decrementing the APD counter, reading keypresses from the keypad and checking
for link activity.
- Mode 2 - This is the mode that is really cool. In this mode, we can create our
own interrupt routine that is run every 1/140th of a second. This is the mode
that this guide will cover.
-Interrupt mode 2-

So what is so important about being able to run code every 1/140th of a second?
Lots. You could write an interrupt routine that handles grayscale. Or maybe you
want to be able to increment the score for your game every 1/4 of a second, no
matter how fast or slow your game might be running. Or you could make an
interrupt routine that checks to see if a key was pressed and if it was, turn
the calculator off (like a teacher key). You could even write an interrupt
routing that adds items to a queue in different intervals.

OK. So now you're eager to create your own interrupt routine. But it's not as
simple as just doing `IM 2`. To know why, some explaning is required.

*(Note: Throughout this guide, I will use the value $99 and $9A but these can be
whatever you want as long as they don't mess with the calculator's ROM)*

When an interrupt occurs and mode 2 is set, the CPU stops what it is doing and
fetches an address to jump to in the memory of the calculator. The MSB (most
significant byte) of this address is the I register. The LSB is a random number,
gotten from the data bus. So say you loaded $99 into the I register (note: you
can't simply do `ld I,$99`. You have to load $99 into A then load A into I).
When an interrupt occurs, the calculator will look at $99xx for the address.
Wait a minute... if the LSB is random, how the hell do you know where the
calculator will look? The answer to this is simple. You must make a table of 257
bytes beginning at $9900 and ending at $99FF that is filled with the same byte
(i.e. $9A) So when the calculator looks at $99xx, it gets a 2 byte address that
will always be the same. Then it calls this address.

Why the hell is that?

Say the LSB is $45. The calculator will look at $9945, right? Then it will get
the 2 byte address from $9945. The 2 byte address will always be $9A9A because
the entire table is filled with $9A!! Say the LSB is $8F. The calculator jumps
to $998F, gets the 2 byte address (which again will be $9A9A) and calls $9A9A!
Amazing, huh?

*(NOTE: The reason you need a 257 byte table instead of 256 bytes is because
every now and the the calculator will try to get an address from $99ff, in which
case the MSB of the address will be at $9a00. So the table must span from $9900
to $9a00, inclusive.)*

So the first part of setting up a mode 2 interrupt routine is to create a 257
byte table filled with the same byte. The second part is installing your
interrupt routine into $9A9A so that when the calculator calls $9A9A it actually
executes your interrupt routine =).

-WRITING AN INTERRUPT-
As soon as an interrupt starts, it MUST save all the registers. This is usually
done with the instructions `exx` and `ex af,af'`. These instructions swap the
registers with their shadow registers. Why do you have to do this? Well, think
about it. If the interrupt is called in the middle of your game and the
registers aren't saved, the registers in your game will be changed every 1/140th
of a second to something you don't want them to be. That is bad. At the end of
the routine you also have to swap the shadow registers back with the original
registers.

*(NOTE: Many common routines, such as ionfastcopy and ionlargesprite, use the
shadow registers while executing. Because of this, they must disable the
interrupts since interrupt routines use `exx`/`ex af,af'` to save the
registers.)*

The following is an example of an interrupt routine:

```
interrupt_start:
	exx			;swap bc, de, hl with their shadow registers
	ex	af,af'		;swap af with it's shadow register (af')
	
	push	hl		;\
	inc	hl		; | interrupt code
	dec	hl		; |
	pop	hl		;/
	
	ex	af,af'		;swap the original af back
	exx			;swap the original bc, de, hl back
	reti			;return from interrupt
interrupt_end:
```
This has got to be one of the most inane interrupts ever, but it demonstrates
the basic interrupt format. It swaps the registers at the beginning, goes
through the interrupt code, swaps the registers back, and returns from the
interrupt.

So now you know how to write a dumb little interrupt routine. Here comes the fun
part... actually using it!

The following is code that will install our interrupt routine:
```
	di				;disable interrupts (don't want an interrupt before we're ready)
	ld	hl,$9900		;start of interrupt table
	ld	de,$9901		;start of interrupt table +1
	ld	bc,256			;257 - 1 bytes to copy
	ld	(hl),$9a		;load $9a into (hl)
	ldir				;ld (hl) into (de), inc hl and de, ld (hl) into (de)...

	;now you have a 257 byte table starting at $9900 filled with $9a

	ld	hl,interrupt_start			;\
	ld	de,$9a9a				; | copy interrupt routine to $9a9a
	ld	bc,interrupt_end-interrupt_start	; |
	ldir						;/
	ld	a,$99
	ld	i,a			;load $99 into I
	im	2			;switch to mode 2
	ei				;enable interrupts
	
	bcall(_homeup)
	ld	hl,text
	bcall(_puts)
loop:	ld	a,$ff
	out	(1),a
	ld	a,$fd
	out	(1),a			;enable group 2
	in	a,(1)			;read keyboard
	cp	191			;was clear pressed?
	jr	nz,loop
	
	im	1			;at end of prog switch back to mode 1 (TI-OS needs mode 1)
	ret
text:
	.db "Mode 2!!",0

interrupt_start:
	exx
	ex	af,af'
	push	hl
	inc	hl
	dec	hl
	pop	hl
	ex	af,af'
	exx
	reti
interrupt_end:
```
You should understand all this by now. This program will install our little
interrupt routine that doesn't really do anything, wait for a key press, and
then quit. Later on I will give you a much more interesting routine. Right now
I'm going to teach you something kinda cool and usefull.

What do you think would happen if we changed the `reti` at the end of our
routine to `jp $0038`? At the end of our routine, instead of returning from the
interrupt, it will go to the calculators normal interrupt.

```
interrupt_start:
	exx
	ex	af,af'
	push	hl
	inc	hl
	dec	hl
	pop	hl
	
	ex	af,af'
	exx
	jp	$0038
interrupt_end:
```
This is usefull if you want your own interrupt but still want the apd to work
and routines such as `_getkey` and `_getcsc` to work properly. It is also very
usefull in creating an interrupt routine that stays in the calculator's memory
even after the program is done executing. Hmm... that gives me an idea... with
this, you could create an interrupt that runs while you are doing normal things
like graphing an equation or entering "4+3" in the homescreen. You could make a
routine that runs in the background and swears at you every time you press enter
or something =). With that, I give you an interrupt routine that I wrote that
turns off the LCD when you press LN and turns it back on when you press LOG
(for when the teacher comes by and you are playing a game)

```
Group7		.equ 0BFh

interrupt_start:
	exx				;swap registers...
	ex	af,af'			;swap registers...

	ld	a,$ff			;\
	out	(1),a			; |
	ld	a,$df			; |hopefully you understand direct input
	out	(1),a			; |
	in	a,(1)			;/

	bit	2,a			;if bit 2 is zero, then LN was pressed
	jr	nz,interrupt_done	;if it wasn't pressed, go to interrupt_done

	di				;disable interrupts
	ld	a,02
	out	($10),a			;turn off LCD
loop:
	ld	a,$ff
	out	(1),a
	ld	a,$df
	out	(1),a
	in	a,(1)

	bit	3,a			;if bit 3 is zero, LOG was pressed
	jr	nz,loop
	ld	a,03
	out	($10),a			;turn LCD back on
interrupt_done:
	exx				;swap registers back
	ex	af,af'			;swap registers back
	jp	$0038			;go to normal interrupt routine
interrupt_end:
```
btw when you install an interrupt routine that is to stay in memory, switch to
im 2 and don't switch back at the end of your installer program.

Hopefully you understood all that. And hopefully you now know more about z80
interrupts. Oh! And before I forget, here is a list of safe ram areas in which
you can install an interrupt.

$86EC - 768 bytes of free ram that is only used if the calculator powers down
through an APD (bad for routines that stay in memory unless you disable the apd)

$8A3A - 531 bytes of ram that is only used to compute statistics. If you use
this, don't compute statistics in your prog! (bad for routines that stay in
memory)

$9872 - 768 bytes or free ram that is intended to be used by applications and
asm programs (GOOD for routines that stay in memory, as long as other programs
don't use it)

Thank you for downloading my guide to the interrupts. If you have any questions,
comments, criticism (good or bad) or corrections, please email me at
joe@joepnet.com

-Joe Pemberton