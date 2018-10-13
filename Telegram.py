import time
import telepot
from telepot.loop import MessageLoop
from pydub import AudioSegment
import miditools
import MIDI_to_generate
from os import listdir
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


# need to set the variables for ffmpeg to work

# pip install telepot
# pip install pydub
# pip install tensorflow
# pip install magenta
# pip install magenta-gpu
# pip install midiutil
# pip install jams

# For python2 (32 bit) (must be 32 bit)
# pip install librosa
# pip install vamp
# pip install midiutil
# pip install numpy

# Convert WAV to MIDI
# Input: audio_id (String)
# Output: MIDI (Dictionary)
def to_MIDI(audio_id):
    miditools.convert_mp3_to_midi(audio_id)
    midi_path = f'./Audio/{audio_id}.mid'
    # do what is needed
    return miditools.get_midi_info(audio_id), midi_path


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


# Process Audio
# Input: msg (Dictionary Object)
def process_audio(msg, content_type):
    audio_id, audio_type = download_audio(msg, content_type)

    while audio_id + '.' + audio_type not in listdir('./Audio'):
        time.sleep(1)

    print(listdir('./Audio'))

    to_WAV(audio_id, audio_type)

    while audio_id + '.wav' not in listdir('./Audio'):
        time.sleep(1)

    # Getting midi_file in dictionary form
    midi_dict, midi_path = to_MIDI(audio_id)
    print(midi_dict)

    # midi_file is dictionary format
    full_path, file_name = MIDI_to_generate.generate_audio(midi_dict, midi_path)

    miditools.convert_midi_to_mp3(full_path, file_name)

    return './telegram_generated/' + file_name + '.mp3'


# Telegram Bot Handle
def on_chat_message(msg):
    print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'audio' or content_type == 'voice':
        bot.sendMessage(chat_id, 'Step 3: Bot Composing Overtime without Pay :D')

        mp3_full_path = process_audio(msg, content_type)

        bot.sendAudio(chat_id, open(mp3_full_path, 'rb'), title=query_data)

    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Piano', callback_data='Piano')],
            [InlineKeyboardButton(text='Combine Piano', callback_data='Combine Piano')],
            [InlineKeyboardButton(text='Simple Drum', callback_data='Drum')],
            [InlineKeyboardButton(text='Combine Drum', callback_data='Combine Drum')],
            [InlineKeyboardButton(text='Melody', callback_data='Melody')],
            [InlineKeyboardButton(text='Trio', callback_data='Trio')],
        ])

        print(chat_id)
        print(msg)
        bot.sendMessage(chat_id, 'Step 1: Choose Your Style', reply_markup=keyboard)


def on_callback_query(msg):
    global query_data
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    bot.sendMessage(from_id, 'Step 2: Send an Audio or Recording')


bot = telepot.Bot("650714662:AAErwYcsJYNPnAw8Vpa9rEw9Q1w6D1vGV3c")

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

print('Listening ...')

while 1:
    time.sleep(10)
