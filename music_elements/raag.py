from typing import Set
from .note import Note
from .chord import Chord

class Raag:
    """
    Represents a raag.

    Attributes:
        notes (Set['Note']): The set of Note objects that make up the raag.
    """
    
    def __init__(self, notes: Set[Note]):
        """
        Initializes a Raag object with a set of notes.

        Args:
            notes (Set['Note']): The set of Note objects that make up the raag.
        """
        self.notes = notes


    def is_note_in_raag(self, note: Note) -> bool:
        """
        Checks if a given note is in the raag.

        Args:
            note ('Note'): The Note object to check.

        Returns:
            bool: True if the note is in the raag, False otherwise.
        """
        return note in self.notes


    def is_chord_in_raag(self, chord: Chord) -> bool:
        """
        Checks if a given chord is in the raag.

        Args:
            chord (Chord): The Chord object to check.

        Returns:
            bool: True if the chord is in the raag, False otherwise.
        """
        return all(note in self.notes for note in chord.notes)