from .note import Note
from .chord import Chord

# imports scamp annd mutes warnings
import logging
logging.getLogger().setLevel(logging.ERROR)
from scamp import Session
logging.getLogger().setLevel(logging.WARNING)

class Instrument:
    """
    Represents a musical instrument player.

    Attributes:
        session (Session): The session object for managing the tempo and parts.
        part (Part): The instrument part for playing notes and chords.
        sa_midi_note (int): The MIDI note number of the 'sa' sur.
    """

    def __init__(self, tempo: float = 60, part: str = 'accordian', sa_midi_note: int = 61):
        """
        Initializes a new instrument.

        Args:
            tempo (float, optional): The tempo of the session in beats per minute (default is 60).
            part (str, optional): The name of the instrument (default is 'Accordian').
            sa_midi (int, optional): The MIDI note number of the 'sa' sur (default is 61).
        """
        self.session = Session(tempo)
        self.part = self.session.new_part(name=part)
        self.sa_midi_note = sa_midi_note


    def play_note(self, note: Note, volume: float = 1.0, duration: float = 1.0) -> None:
        """
        Plays a note using the specified instrument.

        Args:
            note (Note): The note to be played. If None, plays a blank note for the duration.
            volume (float, optional): The volume of the note. Defaults to 1.0.
            duration (float, optional): The duration of the note in seconds. Defaults to 1.0.
        """
        midi_note = None if note is None else self.sa_midi_note + note.note_value
        self.part.play_note(midi_note, volume, duration)


    def play_chord(self, chord: Chord, volume: float = 1.0, duration: float = 1.0) -> None:
        """
        Plays a chord using the specified instrument.

        Args:
            chord (Chord): The chord to be played.
            volume (float, optional): The volume of the chord. Defaults to 1.0.
            duration (float, optional): The duration of the chord in seconds. Defaults to 1.0.
        """
        midi_notes = [self.sa_midi_note + note.note_value for note in chord]
        self.part.play_chord(midi_notes, volume, duration)
