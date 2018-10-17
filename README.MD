# Music Aids

#### Winner of 'Best AI Hack' for iNTUition v5.0 Hackathon 2018 ([More info](https://intuitionv5.devpost.com/))

###### Music Aids Auto Music Generating Bot ([Devpost](https://devpost.com/software/musickeet))

### Tl;dr
1. Telegram bot that receives user (recorded) audio
2. Compose a music piece using [Magenta](https://github.com/tensorflow/magenta) models
3. Return it back to the user via telegram

## IMPORTANT
1. The files for pre-trained model is too big to be uploaded to GitHub. You have to download it manually [here]().
2. Bot is not multi-threaded so please be patient when using the bot.
3. We do not recommend deploying it on your end as it will take about 1 to 2 hours just installing the dependencies assuming no errors. Hopefully, we can try to set up a simple working server to run the telegram bot for you to test it out, no guarantees though.

## Getting Started

The project runs on Python 3.6. However, you need to install 32-bit Python 2.7 for it work correctly due to the multiple audio conversions. The full list of dependencies is listed below:

### Python Modules

You need to install the following Python modules:

###### Python 3.6.2 (64-bit)

* [Tensorflow](https://www.tensorflow.org/install/)
* [Magenta](https://github.com/tensorflow/magenta)
* Music21[ [Windows](http://web.mit.edu/music21/doc/installing/installWindows.html) , [Mac](http://web.mit.edu/music21/doc/installing/installMac.html), [Linux](http://web.mit.edu/music21/doc/installing/installLinux.html) ]
* [Pydub](https://pypi.org/project/pydub/)
* [Telepot](https://telepot.readthedocs.io/en/latest/)
* [MIDIUtil](https://pypi.org/project/MIDIUtil/)

###### Python 2.7 (32-bit)

* [Librosa](https://librosa.github.io/librosa/install.html)
* [Jams](https://pypi.org/project/jams/)
* [Vamp](https://pypi.org/project/vamp/)
* [Mido](https://pypi.org/project/mido/)
* [Numpy](https://scipy.org/install.html)
* [Audio-to-Melodia](http://www.justinsalamon.com/news/convert-audio-to-midi-melody-using-melodia)

### Softwares Required

* FFmpeg (Need to set your environment path to the \<path>/ffmpeg/bin for it to work)
* TiMidity++ (Need to set your environment path to the \<path>/TiMidity++-2.15.0 for it to work)
* SoundFont
* GeneralUser GS

For installation of dependencies, please
1. Set your environment path to the \<path>/ffmpeg/bin for the usage of FFmpeg
2. Then also refer to Instructions.docx for remaining steps in the root folder.
3. Install all the python dependencies for the corresponding python version.
4. Download the pre-trained models [here]() and copy the 'ckpt' folder in the unzipped folder into the root folder directly.
