import os

# table_column = ["groundtruth","encodec_24k_3kbps","hifi-codec-2kbps","encodec_24k_1_5kbps","descript_codec_1_41kbps","semanticodec_1_43_kbps","descript_codec_0_71kbps","semanticodec_0_71_kbps","descript_codec_0_47kbps","semanticodec_0_35_kbps"]

models = ["groundtruth","Xcodec_nq=1","SpeachTokenzier_nq=1","Encodec_uniaudio_nq=1","Encodec_nq=1","DAC_16k_nq=1","Xcodec_nq=12","SpeachTokenzier_nq=8","Encodec_uniaudio_nq=8","Encodec_nq=8","DAC_16k_nq=12"]


# <tr> ... </tr>

# <td><audio controls="controls">
#     <source
#     src="audio/semanticodec_0_35_kbps/audioset_Y-xfgovG6-KU.wav"
#     autoplay />Your browser does not support the audio element.
# </audio></td>
html_string = ""

speech_filelist = [
    "3005_163389_000001_000000.wav",
    "3005_163389_000002_000000.wav",
    "3005_163389_000003_000000.wav",
    "3005_163389_000003_000001.wav",
    "3005_163389_000003_000002.wav",
    "3005_163389_000003_000003.wav",
    "3005_163389_000004_000000.wav",
    "3005_163389_000004_000001.wav",
    "3005_163389_000005_000000.wav",
    "3005_163389_000005_000001.wav"
]

music_filelist = [
    '[flu][cla]0346__1.wav',
    '[flu][cla]0346__2.wav', 
    '[flu][cla]0346__3.wav',
    '[flu][cla]0347__1.wav',
    '[flu][cla]0347__2.wav',
    '[flu][cla]0347__3.wav',
    '[flu][cla]0348__1.wav',
    '[flu][cla]0348__2.wav',
    '[flu][cla]0348__3.wav',
    '[flu][cla]0349__1.wav'
]

events_filelist = [
    '1-137-A-32.wav',
    '1-1791-A-26.wav',
    '1-4211-A-12.wav',
    '1-5996-A-6.wav',
    '1-7057-A-12.wav',
    '1-7456-A-13.wav',
    '1-7973-A-7.wav',
    '1-7974-A-49.wav',
    '1-7974-B-49.wav',
    '1-977-A-39.wav'
]

# count = 0
# for file in speech_filelist:
#     count += 1
#     html_string += "<tr>"
#     html_string += f'<td>{count}</td>'
#     for model in models:
#         html_string += f'<td><audio controls="controls"><source src="audio/{model}/speech/{file}" autoplay />Your browser does not support the audio element.</audio></td>'
#     html_string += "</tr>"
# print(html_string)

# count = 0
# for file in music_filelist:
#     count += 1
#     html_string += "<tr>"
#     html_string += f'<td>{count}</td>'
#     for model in models:
#         html_string += f'<td><audio controls="controls"><source src="audio/{model}/music/{file}" autoplay />Your browser does not support the audio element.</audio></td>'
#     html_string += "</tr>"
# print(html_string)

count = 0
for file in events_filelist:
    count += 1
    html_string += "<tr>"
    html_string += f'<td>{count}</td>'
    for model in models:
        html_string += f'<td><audio controls="controls"><source src="audio/{model}/events/{file}" autoplay />Your browser does not support the audio element.</audio></td>'
    html_string += "</tr>"
print(html_string)