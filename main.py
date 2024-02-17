import whisper

model = whisper.load_model("base")
result = model.transcribe("darkness.mp3")

with open("transcription.txt", "w") as f:
    f.write(result["text"])
