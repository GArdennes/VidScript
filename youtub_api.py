from py_youtube import Data
from docx import Document
# from google import genai
from youtube_transcript_api import YouTubeTranscriptApi
from deepmultilingualpunctuation import PunctuationModel
import re
import streamlit as st
import io

# Get the transcript for a video
# 1. Get the video
# 2. Retrieve the video ID
# 3. Get the transcript for the video
# 4. Format the transcript
# 5. Save the transcript to a file

def get_video(video_link):
    """
    Get the video id and title from a link
    Return: video id, video title
    """
    video = Data(video_link).data()
    video_id = video['id']
    video_title = video['title']
    return video_id, video_title

def get_transcript(video_id):
    """
    Get the transcript for the video
    Return: transcript
    """
    # Get the transcript for the video
    yyt = YouTubeTranscriptApi()
    transcript_1 = yyt.fetch(video_id)

    # Extract text from transcript list of dicts
    transcript_2 = ' '.join(snippet.text for snippet in transcript_1)

    # Format the transcript
    model = PunctuationModel()
    text_format = model.restore_punctuation(transcript_2)
    # return text_format
    return text_format

def format_title(title):
    """
    Format the title to be used as a filename safe for MS Word/Windows:
    - Replace invalid characters <>:"/\\|?* and control chars with '_'
    - Strip leading/trailing whitespace and trailing dots
    - Truncate to a safe length
    - Avoid reserved device names (CON, PRN, AUX, NUL, COM1..COM9, LPT1..LPT9)
    """

    if not title:
        return "document"

    # Replace invalid characters (including control chars)
    sanitized = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', title)

    # Trim whitespace and trailing dots/spaces
    sanitized = sanitized.strip()
    sanitized = sanitized.rstrip('. ')

    # Truncate to leave room for an extension (e.g., .docx)
    max_length = 200
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length].rstrip()

    if not sanitized:
        sanitized = "document"

    # Avoid reserved device names
    reserved = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
    root = sanitized.split('.')[0].upper()
    if root in reserved:
        sanitized = f"_{sanitized}"

    return sanitized

def save_to_file(video_title, transcript):
    """
    Save the transcript to a BytesIO file for download
    Return: BytesIO object, filename
    """
    document = Document()
    document.add_heading(video_title, level=0)
    document.add_paragraph(transcript)
    filename = f"{format_title(video_title)}.docx"
    file_stream = io.BytesIO()
    document.save(file_stream)
    file_stream.seek(0)
    return file_stream, filename




# Streamlit UI
st.title("YouTube Transcript to DOCX")
st.write("Enter a YouTube video link to generate and download its transcript.")

video_link = st.text_input("YouTube Video Link", "")
generate = st.button("Generate Transcript")

if generate and video_link:
    with st.spinner("Processing video..."):
        try:
            video_id, video_title = get_video(video_link)
            transcript = get_transcript(video_id)
            st.subheader("Video Title:")
            st.write(video_title)
            st.subheader("Transcript:")
            st.write(transcript)
            file_stream, filename = save_to_file(video_title, transcript)
            st.download_button(
                label="Download Transcript as DOCX",
                data=file_stream,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        except Exception as e:
            st.error(f"Error: {e}")
