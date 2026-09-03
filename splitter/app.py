import gradio as gr
import subprocess
import os

def split_audio(audio_path):
    output_dir = "separated"
    os.makedirs(output_dir, exist_ok=True)
    subprocess.run(f"demucs --two-stems=vocals \"{audio_path}\" -o {output_dir}", shell=True)
    
    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    stem_folder = os.path.join(output_dir, "htdemucs", base_name)
    
    vocals_path = os.path.join(stem_folder, "vocals.wav")
    no_vocals_path = os.path.join(stem_folder, "no_vocals.wav")
    
    return vocals_path, no_vocals_path

# Frontend
with gr.Blocks(title="BABABU Splitter") as demo:
    gr.Markdown("# 🎧 BABABU Splitter")
    gr.Markdown("Upload karo, Split karo, Download karo!")
    
    with gr.Row():
        audio_input = gr.Audio(label="Upload Song (MP3/WAV)", type="filepath")
        split_btn = gr.Button("⚡ Split Now")
    
    with gr.Row():
        vocals_out = gr.Audio(label="Vocals", type="filepath")
        no_vocals_out = gr.Audio(label="Instrumental", type="filepath")
    
    split_btn.click(fn=split_audio, inputs=audio_input, outputs=[vocals_out, no_vocals_out])

demo.launch()
