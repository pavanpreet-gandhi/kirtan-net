from scamp import Session
import numpy as np
import utils

class Saaj:
    """
    A musical instrument class that allows playing notes in accordance with the notation.
    
    Attributes:
        notation (dict): The notation information loaded from the configuration file.
    """
    notation = utils.load_yaml('./configuration/notation.yml')
    
    def __init__(self, tempo=60, instrument='accordian', sa_midi=61):
        """
        Initializes a new instrument.
        
        Args:
            tempo (float, optional): The tempo of the session in beats per minute (default is 60).
            instrument (str, optional): The name of the instrument (default is 'Accordian').
            sa_midi (int, optional): The MIDI note number of the 'sa' sur (default is 61).
        """
        self.session = Session(tempo)
        self.instrument = self.session.new_part(name=instrument)
        self.sa_midi = sa_midi
    
    
    @staticmethod
    def frequency_to_midi(frequency):
        """
        Converts a frequency to its corresponding MIDI note number.
        
        Args:
            frequency (float): The input frequency in Hertz.
        
        Returns:
            float: The MIDI note number corresponding to the input frequency.
        """
        return 12 * np.log2(frequency/440) + 69
    
    
    @staticmethod
    def midi_to_frequency(midi):
        """
        Converts a MIDI note number to its corresponding frequency.
        
        Args:
            midi (float): The MIDI note number.
        
        Returns:
            float: The frequency in Hertz corresponding to the input MIDI note.
        """
        return 440 * 2**(midi-69)/12
    
    
    def sur_to_midi(self, sur):
        """
        Converts a sur to its corresponding MIDI note number.
        
        Args:
            sur (str): The sur in accordinace with the notation configuration file.
        
        Returns:
            float: The MIDI note number corresponding to the sur frequency.
        """
        if sur=='':
            midi_note = None
        else:
            midi_note = self.sa_midi + self.notation.sur_to_interval[sur]
        return midi_note
    
    
    def play_note(self, note, volume=1.0, duration=1.0, mode='sur'):
        """
        Plays a single note using the instrument. Valid representations of a note include:
            1. Sur in accordance with the notation configuration file.
            2. MIDI note number.
            3. Frequency in Hertz.
        
        Args:
            note (str or float): The note to be played represented as a sur, midi note number, or frequency.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of the note in seconds (default is 1.0).
            mode (str, optional): Valid options are 'sur', 'midi', or 'freq' (default is 'sur').
        """
        if mode=='sur':
            midi_note = self.sur_to_midi(note)
        elif mode=='midi':
            midi_note = note
        elif mode=='freq':
            midi_note = self.frequency_to_midi(note)
        else:
            return
        self.instrument.play_note(midi_note, volume, duration)
    
    
    def play_chord(self, chord, volume=1.0, duration=1.0, mode='sur'):
        """
        Plays a chord (simultanious notes) using the instrument. Valid representations of a chord include a list of:
            1. Sur in accordance with the notation configuration file.
            2. MIDI note number.
            3. Frequency in Hertz.
        
        Args:
            chord (list): The chord to be played represented as a list of sur, midi note number, or frequency.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of the note in seconds (default is 1.0).
            mode (str, optional): Valid options are 'sur', 'midi', or 'freq' (default is 'sur').
        """
        if mode=='sur':
            midi_notes = [self.sur_to_midi(sur) for sur in chord]
        elif mode=='midi':
            midi_notes = chord
        elif mode=='freq':
            midi_notes = [self.frequency_to_midi(freq) for freq in chord]
        else:
            return
        self.instrument.play_chord(midi_notes, volume, duration)