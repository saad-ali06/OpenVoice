from pydub import AudioSegment

def adjust_audio_speed_and_pitch(input_file, output_file, target_duration_ms):
    """
    Adjusts the audio length by speeding up or slowing down, and optionally changes the pitch.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to save the modified audio file.
    - target_duration_ms (int): Target duration in milliseconds.
    - pitch_semitones (int): Change in pitch in semitones (positive for higher pitch, negative for lower pitch).
    """
    # Load the audio file
    audio = AudioSegment.from_file(input_file)
    current_duration = len(audio)

    # Calculate the speed factor for length adjustment
    speed_factor =  current_duration / target_duration_ms 
    
    print(f"Speed Factor:{speed_factor}\nCurrent Audio length:{current_duration}\nTarget Audio length:{target_duration_ms}")

    if speed_factor > 1:
        # Speed up the audio
        adjusted_audio = audio.speedup(playback_speed=speed_factor)
    else:
        # Slow down the audio (stretching)
        playback_speed = speed_factor if speed_factor > 0 else 0.1  # Avoid 0 or negative values
        adjusted_audio = audio._spawn(audio.raw_data, overrides={
            "frame_rate": int(audio.frame_rate * playback_speed)
        }).set_frame_rate(audio.frame_rate)

    # Save the adjusted audio file
    adjusted_audio.export(output_file, format="wav")
    print(f"Adjusted audio saved to {output_file}")

# Example usage:
input_path = "change_output/2.wav"  # Replace with your input audio file
output_path = "change_output/output_audio_01.wav"  # Replace with your desired output file name
target_duration = 14000  # Target duration in milliseconds (e.g., 30 seconds)

adjust_audio_speed_and_pitch(input_path, output_path, target_duration)
