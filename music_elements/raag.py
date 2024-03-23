from .note import Note
from .chord import Chord
from typing import List, Union

class Raag:
    """
    Represents a raag.

    Attributes:
        notes (Set['Note']): The set of Note objects that make up the raag.
    """
    
    def __init__(self, notes: List[Union[str, int, Note]], aroh: List[Union[str, int, Note]], avroh: List[Union[str, int, Note]]):
        """
        Initializes a Raag object with a set of notes.

        Args:
            notes (List[Union[str, int, Note]]): The list of Note objects, str, or int that make up the raag.
        """
        self.notes = sorted([Note(note) if isinstance(note, (str, int)) else note for note in notes])
        self.aroh = [Note(note) if isinstance(note, (str, int)) else note for note in aroh]
        self.avroh = [Note(note) if isinstance(note, (str, int)) else note for note in avroh]


    def is_note_in_raag(self, note: Note) -> bool:
        """
        Checks if a given note is in the raag.

        Args:
            note ('Note'): The Note object to check.

        Returns:
            bool: True if the note is in the raag, False otherwise.
        """
        return note.get_base_note() in self.notes
    
    
    def is_note_in_aroh(self, note: Note) -> bool:
        """
        Checks if a given note is in the aroh of the raag.

        Args:
            note ('Note'): The Note object to check.

        Returns:
            bool: True if the note is in the aroh, False otherwise.
        """
        return note.get_base_note() in self.aroh
    
    
    def is_note_in_avroh(self, note: Note) -> bool:
        """
        Checks if a given note is in the avroh of the raag.

        Args:
            note ('Note'): The Note object to check.

        Returns:
            bool: True if the note is in the avroh, False otherwise.
        """
        return note.get_base_note() in self.avroh


    def is_chord_in_raag(self, chord: Chord) -> bool:
        """
        Checks if a given chord is in the raag.

        Args:
            chord (Chord): The Chord object to check.

        Returns:
            bool: True if the chord is in the raag, False otherwise.
        """
        return all(note.get_base_note() in self.notes for note in chord.notes)
    
    
    def is_chord_in_aroh(self, chord: Chord) -> bool:
        """
        Checks if a given chord is in the aroh of the raag.

        Args:
            chord (Chord): The Chord object to check.

        Returns:
            bool: True if the chord is in the aroh, False otherwise.
        """
        return all(note.get_base_note() in self.aroh for note in chord.notes)
    
    
    def is_chord_in_avroh(self, chord: Chord) -> bool:
        """
        Checks if a given chord is in the avroh of the raag.

        Args:
            chord (Chord): The Chord object to check.

        Returns:
            bool: True if the chord is in the avroh, False otherwise.
        """
        return all(note.get_base_note() in self.avroh for note in chord.notes)