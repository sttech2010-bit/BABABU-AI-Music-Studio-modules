import gradio as gr
import torch
import torchaudio
from denoiser import pretrained
from denoiser.dsp import convert_audio

def polish_audio(audio_path):
    model = pretrained.demucs()
    wav, sr = torchaudio.load(audio_path)
    wav = convert_audio(wav, sr, model.sample_rate, model.channels)
    with torch.no_grad():
        denoised = model(wav[None])[0]
    output_path = "polished.wav"
    torchaudio.save(output_path, denoised, model.sample_rate)
    return output_path

# Frontend
with gr.Blocks(title="BABABU Polish") as demo:
    gr.Markdown("# ✨ BABABU Polish")
    gr.Markdown("Ordinary voice ko studio quality mein clean karo!")
    
    audio_input = gr.Audio(label="Upload Voice", type="filepath")
    polished_output = gr.Audio(label="Polished Audio", type="filepath")
    btn = gr.Button("Polish Now")
    
    btn.click(fn=polish_audio, inputs=audio_input, outputs=polished_output)

demo.launch()
