from py_youtube import Data
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import Formatter, TextFormatter
from deepmultilingualpunctuation import PunctuationModel

# Get the transcript for a video
# 1. Get the video
# 2. Retrieve the video ID
# 3. Get the transcript for the video
# 4. Format the transcript
# 5. Save the transcript to a file

def get_video():
    """
    Get the video link from the user
    Return: video id, video title
    """
    # Get the video link
    video = input('Enter the video link: ')
    # Get the video ID
    video = Data(video).data()
    video_id = video['id']
    # Get the video title
    video_title = video['title']
    return video_id, video_title

def get_transcript(video_id):
    """
    Get the transcript for the video
    Return: transcript
    """
    # Get the transcript for the video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Format the transcript
    model = PunctuationModel()
    formatter = TextFormatter()
    text_format = formatter.format_transcript(transcript)
    text_format = model.restore_punctuation(text_format)
    return text_format

def save_to_file(video_title, transcript):
    """
    Save the transcript to a file
    Return: Docx File
    """
    filename = f'{video_title}.docx'
    with open(filename, 'w') as file:
        file.write(f"Transcript for '{video_title}' \n\n")
        file.write(transcript)
    print(f"Transcript saved to '{filename}'")



if __name__ == '__main__':
    # Get the video
    video_id, video_title = get_video()
    # Get the transcript for the video
    transcript = get_transcript(video_id)
    # Save the transcript to a file
    save_to_file(video_title, transcript)
#video = 'https://youtu.be/d-yXXMarULk?si=wk4Um0WimqpB4IKk'
