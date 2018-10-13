import time
import telepot
from telepot.loop import MessageLoop
from pydub import AudioSegment
import miditools
import MIDI_to_generate
from os import listdir

# need to set the variables for ffmpeg to work
# https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg

# pip install telepot
# pip install pydub
# pip install tensorflow
# pip install magenta
# pip install magenta-gpu
# pip install vamp  
# pip install midiutil
# pip install jams

# Convert WAV to MIDI
# Input: audio_id (String)
# Output: MIDI (Dictionary)
def to_MIDI(audio_id):
    # do what is needed
    return miditools.get_midi_info(audio_id)


# Convert All Audio to WAV
# Input: audio_id (String), audio_type (String)
# Output: audio_file_path (String)
def to_WAV(audio_id, audio_type):
    print(audio_id, audio_type)
    if audio_type.lower() != "wav":
        raw_audio = AudioSegment.from_file('./Audio/' + str(audio_id) + '.' + str(audio_type), format=audio_type)
        raw_audio.export('./Audio/' + str(audio_id) + '.wav', format="wav")


# Download Audio to Directory
# Input: msg (Dictionary Object), content_type (String/Key)
# Output: audio_id (String), audio_type (String), audio_path (String)
def download_audio(msg, content_type):
    audio_id = msg[content_type]["file_id"]
    audio_type = msg[content_type]["mime_type"][-3::]
    bot.download_file(audio_id, './Audio/' + str(audio_id) + '.' + str(audio_type))

    print(audio_id, audio_type)
    return audio_id, audio_type


# Telegram Bot Handle
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    # Will need to find a way to stream line this part
    if content_type != 'audio' and content_type != 'voice':
        bot.sendMessage(chat_id, 'Please Send An Audio File')
        return

    # Handle audio/voice file
    audio_id, audio_type = download_audio(msg, content_type)
    while not listdir('./Audio'):
        time.sleep(1)
    to_WAV(audio_id, audio_type)
    # Getting midi_file in dictionary form
    midi_file = to_MIDI(audio_id)
    print(midi_file)

    # midi_file is dictionary format
    MIDI_to_generate.generate_audio(midi_file)


bot = telepot.Bot("650714662:AAErwYcsJYNPnAw8Vpa9rEw9Q1w6D1vGV3c")

MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
