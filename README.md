Ponifuse is an experimental project in applying the text-replacement rules of Ponify to file transparently as they are written and read.

So, about a month or so ago, one of my floormates, Derp called me "gay" for liking and watching My Little Pony, right? He was met with the full force of Love and Tolerance. eg:

>>him

>"Dude, it's a *[redacted]* girl's show, you are gay." &#3232;\_&#3232;

>>me 

>"Have you seen it? You shouldn't judge something by first appearances."
and he gave up from there (pro tip: love and tolerance beats all).

So, about a week ago *(from date of writing)*, I installed ponify on his browesr and completely hid it. Today he found out the magic. And I found out he thought the internet was broken, and he went over to my desktop and laptop to confirm this.  Oh, I should mention, I have ponify on both my boxes.  I verified to him that he was searching for "The Filly With The Dragon Cutie Mark", and not "The Girl With the Dragon Tattoo".  The look on his face as he had a lapse of sanity was *so* worth it.  

My next idea? Make Ponify modify files at load-time in the linux kernel (or possibly a FUSE module) to smartly ponify files at load-time by transparently mounting the ponifuse module at login.

This is the implementation of that idea, in the form of a fuse module. [](/ppfear "can people see this?")

---

Special thanks to stillunmaned on irc.ponychat.net for helping me get the basics of the replacement logic hammered down.



More to come.
