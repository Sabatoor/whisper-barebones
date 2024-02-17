import whisper
import nltk

# Download the Punkt tokenizer models if it's the first time
nltk.download('punkt')

def insert_newlines(text):
    # Use NLTK's sentence tokenizer
    sentences = nltk.tokenize.sent_tokenize(text)
    return '\n'.join(sentences)

# Load the Whisper model
model = whisper.load_model("base")
result = model.transcribe("TheBet.mp3")

# Insert newlines between sentences in the transcribed text
formatted_text = insert_newlines(result["text"])

# Open or create the file and append the new segment
with open("the-bet-transcription.txt", "a") as f:  # Change "w" to "a" to append instead of overwrite
    f.write("\n\nnew segment\n\n")  # Add two new lines, then "new segment", then two more new lines
    f.write(formatted_text)  # Append the formatted text
