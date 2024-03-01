from scamp import Session
import numpy as np
import utils

class Saaj:
    """
    A musical instrument class that allows playing notes and frequencies.
    
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
        Initializes a new instrument.
        
        Args:
            tempo (float, optional): The tempo of the session in beats per minute (default is 60).
            instrument (str, optional): The name of the instrument (default is 'Accordian').
            sa_note (int, optional): The MIDI note number of the 'sa' sur (default is 61).
        """
        self.session = Session(tempo)
        self.instrument = self.session.new_part(name=instrument)
        self.sa_note = sa_note
        self.sura = utils.load_sura()
        self.set_sa_note(self.sa_note)
    
    
    def set_sa_note(self, sa_note):
        """
        Sets the 'sa' sur note and updates the sur to note mapping accordingly.
        
        Args:
            sa_note (int): The MIDI note number of the 'sa' sur.
        """
        self.sa_note = sa_note
        self.sur_to_note = {}
        for i, sur in enumerate(self.sura.all_sura):
            sur_note = self.sa_note + i
            self.sur_to_note[sur] = sur_note
            self.sur_to_note[sur+self.sura.saptak.lower] = sur_note - len(self.sura.all_sura)
            self.sur_to_note[sur+self.sura.saptak.upper] = sur_note + len(self.sura.all_sura)
        self.sur_to_note[''] = None
    
    
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
    
    
    def play_notes(self, notes, volume=1.0, duration=1.0):
        """
        Plays a sequence of notes using the instrument.
        
        Args:
            notes (list): A list of notes to be played in sequence.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of each note in the sequence in seconds (default is 1.0).
        """
        for note in notes:
            self.play_note(note, volume, duration)
    
    
    def sura_to_notes(self, sura):
        """
        Converts a sequence of sura into notes.
        
        Args:
            sura (list): A list of sura to be converted into notes.
        
        Returns:
            list: A list of MIDI note numbers corresponding to the sura.
        """
        return [self.sur_to_note[sur] for sur in sura]
    
    
    def play_sura(self, sura, volume=1.0, duration=1.0):
        """
        Plays a sequence of sura using the instrument.
        
        Args:
            sura (list): A list of sura to be played in sequence.
            volume (float, optional): The volume of the note between 0 and 1 (default is 1.0).
            duration (float, optional): The duration of each sur in the sequence in seconds (default is 1.0).
        """
        notes = self.sura_to_notes(sura)
        self.play_notes(notes)