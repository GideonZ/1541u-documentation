Interview RetroMagazine
-----------------------

*Interview with Gideon Zweijtzer, creator of the 1541 Ultimate series of expansion cartridges and the Commodore 64 FPGA-based motherboard Ultimate64 - July 2018*


Hi, Gideon and thank you so much for accepting my invitation for an interview. All the readers and the editorial staff of RetroMagazine are very excited to have the opportunity to ask you some questions about your experience in designing one of the most (if not the most) famous cartridge/expansion for the C64: the 1541 Ultimate. During 2017, according to your web site, the final steps of the Ultimate64 design have been completed, so the long-awaited board has finally got into production and the first batches have been shipped to the final users earlier this year.

Most of the Commodore 64 fans out there are well-aware of your fantastic products, but I’m pretty sure they don’t know how it all began. So let's start from the beginning.


**Can you please shortly introduce yourself and tell us something about your own story (ie. where you are born, growing up, your education, your personal interests, etc.)?**

Hi David, thanks for the invitation! Talking about myself? Sure... I was born in Amsterdam in 1974, in a quite stable family with one older brother. I have always been interested in technicalities. Before the home computers came, I was always with my technical Lego, although I also loved to race around on my bike through the neighborhood. I often played with circuits made from switches, motors and light bulbs, but unfortunately I did not have anyone in my surroundings with knowledge of electronics. From the secondary school, I went to the university TU Delft, where I studied Electronic Engineering.


**I guess you have always been a computer fan and user since when you were a kid. What started you on the path of computing and what was your first experience with a computer? Was the Commodore 64 your fist computer?**

I was pretty young when we got an Atari 2600 game console. It was actually my brother who had started with the whole computer thing and he started to investigate the possibilities for programming. There was a basic interpreter for the A2600 at that time, but in the end he bought a ZX81. I was not really allowed to touch it, but sometimes I sneaked into his room and tried a few things, but as a kid without any help, I didn’t get that far. Later, my brother got a Commodore 64 and this got big. It was so popular in that time! Computer clubs, meetings, copying games and programs! My brother infected me with his curiosity about programming and although he didn’t want me to bother him, I could sit on the floor in between his massive desk and the old color TV that was on top of another table in front of that. As long as he didn’t hear me, I could just watch what he was doing. I saw basic, assembler, etc. At a certain point I could tell him from behind the desk that he forgot a statement... It was not until I reached the age of 11 that I got my own Commodore 64.


**How did you get started working on a C64, beyond playing games? Did you quickly find interest in programming and discovering how the machine intimately work?**

I never really played a lot of games, actually. There are some exceptions, like Giana Sisters. But in general, I did not spend a lot of time on games altogether. As my brother focused a lot on the software, my interest in the hardware grew. At a certain point I made a simple thermometer, using an NTC thermistor on the paddle port of the C64. I needed my older brother again for his math skills to figure out the conversion curve. At the computer club in Amsterdam, I usually spent my time around the repair stand, where I could see how some guys were de-soldering and replacing chips in broken C64’s. According to my mother, I had the full schematic of the C64 hanging from the wall in my small bedroom. But in all honesty, I don’t remember that.


**After the C64, did you get your first PC and still keep the C64 on your desk? Did you ever use one of the many SD2IEC devices on the market before starting to design the 1541 Ultimate?**

No, I haven’t. In fact, I think you’re now skipping quite a few years. My interest in the C64 faded as the Amiga 500 came, and later the PC. Actually my first PC was a Pentium 120 MHz, so you can imagine that I have resisted PCs for quite some time... The love for the C64 never really went away, I just never used it. Neither have I ever been part of a demo- or game coder group, or the “scene” in general... So there was basically never a need for an SD2IEC or any other C64 peripheral.


**What inspired you to design the first version of the 1541 Ultimate and when did you start?**

The first version of the 1541 Ultimate was made in 2007. It all started with some implementations of the 6502 as I was learning and getting more experience with FPGA design using VHDL. That was back in 2001 or so. There were a lot of things going on back then. For instance, Jeri Ellsworth was working on her C-One, which later became the DTV, if I am not mistaken. In any case, I had already done a lot of the C64 in FPGA at that time, but I didn’t see the point of being a “me-too” player. So I thought I’d do the floppy drive instead. On one of the club meetings that we have in Maarssen, I demoed the very first prototype on a Xilinx Spartan 3 board. You needed a laptop or PC to download a floppy image over Ethernet into its memory, after which the board acted as a floppy drive. No menu, no other emulations, only the drive.  Later, in a conversation with one of my colleagues at work, the idea arose to build it into a cartridge, such that the VIC could be used to display a user-interface. This idea crystalized in 2007.


**Did you design the hardware and the software/firmware for the 1541 Ultimate all by yourself?**

Yes, basically. There have been some important contributions from others over the years, though. But in essence, the hardware design, the FPGA design and the firmware design and framework are made by me.


**What was your computer system setup that you used to develop and test the early project of the cartridge?**

Just a PC and one Commodore 64... And yes, that did not include a 1541 drive! Later it showed that this was not enough, but I did not have more hardware, so I visited some friends from the Commodore club that had impressive collections of machines to test the compatibility with. In fact, there I found out that the very first prototype of the 1541 Ultimate as a cartridge was not very compatible, which caused some design changes before the board went into production.


**Did you take any computer courses to start you in the field of electronics? And if so, what were they and how much time did you invest? Or, like many designers/programmers of the early Eighties, were you a self-taught techie?**

Many things were self-taught, although studying at Delft University of Technology has made me understand many more things. But to be fair, I think that I learned most at the job after my studies. I started to work as a junior designer at Technolution B.V., and there I learned most of the practical knowledge that I have today, in terms of electronics design. Interestingly, I brought knowledge about FPGA design back as I was one of the founders of this discipline within the company. 


**What was your development process like? Did you use to sketch out concepts, design the mainboard and the firmware, etc.? Do you still take on the design process the same way?**

Oww, that’s quite a difficult question. Because I have always seen these activities as a hobby, I mostly just let it happen. I am the kind of designer that does a lot of design work ‘as a background process’. I am not a very structured, method-following, step-by-step kind of engineer. (I made quite a few project-managers pull their hairs out, as they didn’t see me work on new tasks they assigned to me in the first weeks...)

I work with iterations, basically. But mostly just in my mind. Sometimes under the shower, or while driving. Once it ‘feels right’, I start to do some implementation. And sometimes after an implementation I realize it doesn’t feel as right anymore. I am not afraid of just throwing some work away and start anew. Of course, always taking into account the lessons learned in the previous step.


**Talking about your biggest projects (the 1541 Ultimate cartridge and the new Ultimate64 mainboard), what technical challenge gave you the biggest feeling of accomplishment?**

Ok, when I need to limit it to ‘technical challenges’, it would definitely be the solving of very hard-to-find bugs... You know, those nasty ones that make others quit on their project... Those!
On a second place, it is when I power up a new board and everything works right away. (And that’s not uncommon in my case... [smug face]).


**What was the biggest tech/programming obstacle that you ever overcome while designing/producing/testing/selling the 1541 Ultimate or the Ultimate64?**

Obstacles... [thinking]… It depends a bit on how you define the obstacles. Most things are just time consuming tasks. But yet, I think there are several ‘obstacles’. I think in case of the 1541 Ultimate, it must have been creating an easy to use user interface without having access to any framework; building everything from scratch. On an embedded platform, which the Ultimate clearly is, you can't use standard frameworks like the ones commonly used in Java and C#, so you have to make one of your own.  

Hmm, another obstacle was the development of a factory test system for the Ultimate-II+. That took quite some time. But then, I do think it saves me a lot of time. 

Another one was the move to a web-shop system, rather than just taking orders and processing them manually. 


**What was/is your favorite game for the C64? Do you still find some time to play?**

Giana Sisters... err.. no time to play!


**I imagine that you do own a collection of stock C64s (i.e. all versions: from C64 “breadbin” with all the ASSY board revisions, to C64c, C64g and C128) for testing purpose. Are you a collectionist of retrocomputers as well, not only Commodore branded?**

My wife would kill me, if I were actually collecting more. I only have working C64 mainboards, of which I use mainly just one in a C64C case. This has been the same machine as I used to test over 3000 ultimate’s over the years. The power switch and cartridge port are a bit sad now. I do have a C128 and a C128D, but I never use them. I do have several floppy drives, too. 


**Can you even think about calculating how many hours you spent designing and working on the several versions of the 1541 Ultimate cartridge? What about the Ultimate64?**

It is very difficult. As I said, many design activities take place as a background task. If I would count only the hours that I spend on the PC it might give a falsely low figure. What I can tell, tho, is that hardware designs, board layouts and such, usually don’t take that much time. I think I created the U64 board design in about 3 weeks’ time, but then of course only in the evenings and weekends. The schematics took a similar amount of time. Most time spent on technicalities goes into FPGA design, implementation and debug and firmware implementation.

From your question I sense that you focus a lot on the technical aspects, but I can tell you that the administrative tasks, including shipping orders and answering e-mails takes up most of my time, unfortunately.


**Have you ever worked or are you planning to work on other projects involving the C64 or even different 8/16-bit machines?**  

Nope... :-)


**How many people currently work at Gideon Lab on producing, testing and selling the two main products? Did you ever work in a team or simply get consulted with other electronics/software experts in order to achieve a particular result or to solve a bug?**

Production is outsourced to a number of companies. (Production-) testing of the Ultimate-II+ is also performed in the factory. Production test for the U64 doesn’t exist yet as of today, but that will be the next step in order to accelerate the process. When we talk about assembling the U2+ into plastic cases, that’s often done by my wife, ... when she feels like it. She also plays an important role in packing orders. The other things are done by me; there are no employees at this point. Whether this can continue like this, is questionable. I think I do need external help for the quantity of U64’s that are currently on order.

On the technical aspect, I sometimes talk with my colleagues about certain bugs, and of course I use the feedback and input from the community. There are some pretty smart guys out there that help me solve bugs sometimes. In order to achieve a particular result, I often apply patterns that I quietly pick up or learn from other projects.


**Looking back to where you started it all, is there something that you regret about the PCB design or any other detail? Would you do something in a different way now if you could?**

I mostly regret not taking the C64 FPGA code that I had made years before the U64 to a production level. I actually demoed a complete C64 in FPGA already back in 2011. I thought nobody would be interested in buying an FPGA-based C64 motherboard, since original C64 machines could be picked up for almost nothing, or else people would use an emulator anyway.

Regrets about other aspects: well, in retrospect many things could be regretted. But I think it is not fair to look at things like that, because as a person and as an engineer, you learn while you do it. Once you think things have to change, there is always the freedom to do so. I think that is one of the very cool things about having your own product. But I guess this principle applies to many things in life, doesn’t it..?


**I’m pretty sure that you worked very hard on both your projects during the last few years but also that you had so much fun doing it. What is the most funny/weird moment or story that you’ve been through while developing your products?**

Oh, I absolutely had much fun doing it! Technically speaking, I have the most fun doing the FPGA code, second the hardware itself, and third the firmware.

I think one funny moment was the moment I realized how naive I can be. In the whole process of creating the 1541 Ultimate, I *never* thought of actually making a sellable product out of it. Or let’s say, that was not my goal; it had always been pure hobby until then. It was actually a Swedish scener, TwoFlower, who happened to visit the Commodore Club in Maarssen just when I was giving the demo of a cartridge with an embedded floppy drive. He said I should have it produced, but I was hesitant and thought that it was not even feasible to do so. He asked me how many needed to be produced, and I stammered, “maybe 40 or 50?” He smiled and said: “Just do it... I’ll make sure you’ll sell all 40 of them in Sweden alone!” And that’s how it all started!


**Gideon, thank you very much for your time. This interesting interview ends here. Would you like to add anything, or say anything to our readers?**

There is one important thing to mention.. I would like express a huge 'thank you' to the Commodore loving community. One of the most rewarding aspects of this project is the great feedback, the positive words I receive. In short: without you guys, I would never have been able to do all this. Thank you.



Interviewer: David La Monaca (aka Cercamon)

RetroMagazine Facebook Group - https://www.facebook.com/RetroMagazine-2005584959715273

Website - http://www.retromagazine.net


*Interview made in May-June, 2018
© 2018 David La Monaca, Gideon Zweijtzer and RetroMagazine*
