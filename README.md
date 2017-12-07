# HackTXAudio
#### Deep Learning with Audio

### Contributors:

* Michael Asper - michael@asperdx.com - University of Texas
* Kathryn Baldauf - kathrynbaldauf@utexas.edu - University of Texas
* Kristin Hamilton -  khamilt2@stedwards.edu - St. Edward's University
* Naseem Raad - nraad1@stedwards.edu - St. Edward's University
* David Green - david.green@utexas.edu - University of Texas


### Goal:

We started hackathon with a goal in mind: to train a computer to generate some sort of audio. This isn't particularly a new idea; however most previous attempts tend to rely on paino/classical music were the music is scored, and more likely to be trained on the sheet music itself rather than the audio or MIDI files which is a digital representation of sheet music for many genres of music. 

Our idea was to learn straight from the waves and frequency of the music and trained them as sequences. Sort of cutting up the song by 50 samples of frequencies and traing as a sequence.


### Results:

The competition start at **12:00pm** and the majority of the team fell asleep at **6:00am after very little breaks.** We were able to create a LSTM model that learned; however, our biggest defeators was training time and lack of sleep. After succesfully creating our model, our training time was 34000 seconds, roughy 9-10 hours. We did not have time to train it; however we were able to get ahold of a cloud server, but it took approximately 2 hours to get it running with our code. We did get it working and the training time down to an **astonishing 5-8 minutes.** If it wasn't due to time constraints of the event, we would of had a fully working model that could predict music as well.

I was very happy we decided on the LSTM model as I believed it was the right fit. If you would like to learn more about LSTM models, [read here](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

### Reflection:

Some things that would've been done differently is focusing on **mono** audio instead of **stereo** as that would've been easier to preprocess, train, and predict. Have a cloud computer prepared already instead of wasting time getting it running at 4am, and the last thing I felt like would've been helpful was a more organized way of keeping all the code clean and together instead of separated on laptops. (I cannot promise I found all of the code from this project as we were very distracted we didn't push to the repository as much as wanted).
