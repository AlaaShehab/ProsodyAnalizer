from parselmouth.praat import run_file
import os


def get_features(praat_source, wav_file_path, textgrid_save):
    try:
        extracted_data = run_file(praat_source, -20, 2, 0.3, "yes", wav_file_path, textgrid_save, 80, 400, 0.01,
                                  capture_output=True)
        features_values = str(extracted_data[1]).strip().split()
        features = {"number_ of_syllables": features_values[0], "number_of_pauses": features_values[1],
                    "rate_of_speech": features_values[2],
                    "articulation_rate": features_values[3], "speaking_duration": features_values[4],
                    "original_duration": features_values[5], "balance": features_values[6],
                    "f0_mean": features_values[7], "f0_std": features_values[8],
                    "f0_median": features_values[9], "f0_min": features_values[10], "f0_max": features_values[11],
                    "f0_quantile25": features_values[12], "f0_quan75": features_values[13]}
        print(features)
        return features

    except Exception as e:
        print("Try again the sound of the audio was not clear")
        print(e)
    return
