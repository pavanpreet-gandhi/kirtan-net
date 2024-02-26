from scamp import Session
import numpy as np
import yaml

class Waja:
    """
    A musical instrument class that allows playing notes, frequencies, and chords.
    
    Args:
        tempo (float, optional): The tempo of the session in beats per minute (default is 60).
        instrument (str, optional): The name of the instrument (default is 'Accordian').
    
    Attributes:
        session (Session): A Scamp session for managing musical parts.
        instrument (Part): The musical part associated with the instrument.
        sa_note (int): The MIDI note number of the 'sa' sur.
        sur_to_note (dict): A dictionary mapping each sur to its corresponding MIDI note number.
    """
    
    def __init__(self, tempo=60, instrument='Accordian', sa_note=61):
        """
        Initializes a new Waja instrument.
        
        Args:
            tempo (float, optional): The tempo of the session in beats per minute (default is 60).
            instrument (str, optional): The name of the instrument (default is 'Accordian').
            sa_note (int, optional): The MIDI note number of the 'sa' sur (default is 61).
        """
        self.session = Session(tempo)
        self.instrument = self.session.new_part(name=instrument)
        self.sa_note = sa_note
        
        with open('raag_sur_mapping.yml', 'r') as file:
            raag_sur_mapping = yaml.safe_load(file)
            self.all_sura = raag_sur_mapping['all_sura']
            self.saptak = raag_sur_mapping['saptak']
        
        self.set_sa_note(self.sa_note)
        
    def set_sa_note(self, sa_note):
        """
        Sets the 'sa' sur note and updates the sur to note mapping accordingly.
        
        Args:
            sa_note (int): The MIDI note number of the 'sa' sur.
        """
        self.sa_note = sa_note
        self.sur_to_note = {}
        for i, sur in enumerate(self.all_sura):
            sur_note = self.sa_note + i
            self.sur_to_note[sur] = sur_note
            self.sur_to_note[sur+self.saptak['lower']] = sur_note - len(self.all_sura)
            self.sur_to_note[sur+self.saptak['upper']] = sur_note + len(self.all_sura)
    
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
    def midi_to_frequency(note):
        """
        Converts a MIDI note number to its corresponding frequency.
        
        Args:
            note (float): The MIDI note number.
        
        Returns:
            float: The frequency in Hertz corresponding to the input MIDI note.
        """
        return 440 * 2**(note-69)/12
    
    def play_note(self, note, volume=1.0, duration=1.0):
        """
        Plays a single note using the instrument.
        
        Args:
            note (float): The MIDI note number of the desired note.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of the note in seconds (default is 1.0).
        """
        self.instrument.play_note(note, volume, duration)
    
    def play_frequency(self, frequency, volume=1.0, duration=1.0):
        """
        Plays a note at a specific frequency using the instrument.
        
        Args:
            frequency (float): The desired frequency in Hertz.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of the note in seconds (default is 1.0).
        """
        note = self.frequency_to_midi(frequency)
        self.instrument.play_note(note, volume, duration)
    
    def play_sur(self, sur, volume=1.0, duration=1.0):
        """
        Plays a sur using the instrument.
        
        Args:
            sur (str): The sur to be played.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of the note in seconds (default is 1.0).
        """
        note = self.sur_to_note[sur]
        self.play_note(note, volume, duration)
    
    def play_chord(self, chord, volume=1.0, duration=1.0, type='sur'):
        """
        Plays a chord using the instrument.
        
        Args:
            chord (list): A list of MIDI note numbers or frequencies or sura representing the chord.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of the chord in seconds (default is 1.0).
            type (str, optional): The type of the elements in the chord list. It can be 'sur', 'frequency', or 'note' (default is 'sur').
        """
        if type=='sur':
            chord_notes = [self.sur_to_note[sur] for sur in chord]
        elif type=='frequency':
            chord_notes = [self.frequency_to_midi(freq) for freq in chord]
        else:
            chord_notes = chord
        self.instrument.play_chord(chord_notes, volume, duration)
    
    def play_sur_sequence(self, sur_sequence, volume=1.0, duration=1.0):
        """
        Plays a sequence of sura using the instrument.
        
        Args:
            sur_sequence (list): A list of sura to be played in sequence.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of each sur in the sequence in seconds (default is 1.0).
        """
        for sur in sur_sequence:
            self.play_sur(sur, volume, duration)