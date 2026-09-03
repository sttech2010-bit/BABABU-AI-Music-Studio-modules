import gradio as gr
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import pretty_midi

def audio_to_midi(audio_path):
    model_output, midi_data, note_events = predict(audio_path)
    
    # MIDI file ko save karna
    midi_path = "output.mid"
    midi_data.write(midi_path)
    
    return midi_path

# Frontend
with gr.Blocks(title="BABABU MIDI Lab") as demo:
    gr.Markdown("# 🎹 BABABU MIDI Lab")
    gr.Markdown("Humming ya kisi bhi instrument ko MIDI mein convert karo!")
    
    audio_input = gr.Audio(label="Upload Audio", type="filepath")
    midi_output = gr.File(label="Download MIDI")
    btn = gr.Button("Convert to MIDI")
    
    btn.click(fn=audio_to_midi, inputs=audio_input, outputs=midi_output)

demo.launch()
