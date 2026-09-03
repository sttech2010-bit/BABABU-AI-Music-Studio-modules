import gradio as gr
from faster_whisper import WhisperModel

def extract_lyrics(audio_path):
    model = WhisperModel("base", device="cpu")
    segments, info = model.transcribe(audio_path)
    lyrics = ""
    for segment in segments:
        lyrics += f"[{segment.start:.1f}s - {segment.end:.1f}s] {segment.text}\n"
    return lyrics

# Frontend
with gr.Blocks(title="BABABU Lyricist") as demo:
    gr.Markdown("# 🎵 BABABU Lyricist")
    gr.Markdown("Upload karo, Lyrics nikaalo!")
    audio_input = gr.Audio(label="Upload Song", type="filepath")
    output_text = gr.Textbox(label="Lyrics", lines=10)
    btn = gr.Button("Extract Lyrics")
    btn.click(fn=extract_lyrics, inputs=audio_input, outputs=output_text)

demo.launch()
