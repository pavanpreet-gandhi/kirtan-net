from typing import List
from .note import Note
from .chord import Chord

class Raag:
    """
    Represents a raag.

    Attributes:
        notes (Set['Note']): The set of Note objects that make up the raag.
    """
    
    def __init__(self, notes: List[Note], aroh: List[Note], avroh: List[Note]):
        """
        Initializes a Raag object with a set of notes.

        Args:
            notes (Set['Note']): The set of Note objects that make up the raag.
        """
        self.notes = sorted(notes)
        self.aroh = sorted(aroh)
        self.avroh = sorted(avroh)


    def is_note_in_raag(self, note: Note) -> bool:
        """
        Checks if a given note is in the raag.

        Args:
            note ('Note'): The Note object to check.

        Returns:
            bool: True if the note is in the raag, False otherwise.
        """
        return note in self.notes
    
    
    def is_note_in_aroh(self, note: Note) -> bool:
        """
        Checks if a given note is in the aroh of the raag.

        Args:
            note ('Note'): The Note object to check.

        Returns:
            bool: True if the note is in the aroh, False otherwise.
        """
        return note in self.aroh
    
    
    def is_note_in_avroh(self, note: Note) -> bool:
        """
        Checks if a given note is in the avroh of the raag.

        Args:
            note ('Note'): The Note object to check.

        Returns:
            bool: True if the note is in the avroh, False otherwise.
        """
        return note in self.avroh


    def is_chord_in_raag(self, chord: Chord) -> bool:
        """
        Checks if a given chord is in the raag.

        Args:
            chord (Chord): The Chord object to check.

        Returns:
            bool: True if the chord is in the raag, False otherwise.
        """
        return all(note in self.notes for note in chord.notes)
    
    
    def is_chord_in_aroh(self, chord: Chord) -> bool:
        """
        Checks if a given chord is in the aroh of the raag.

        Args:
            chord (Chord): The Chord object to check.

        Returns:
            bool: True if the chord is in the aroh, False otherwise.
        """
        return all(note in self.aroh for note in chord.notes)
    
    
    def is_chord_in_avroh(self, chord: Chord) -> bool:
        """
        Checks if a given chord is in the avroh of the raag.

        Args:
            chord (Chord): The Chord object to check.

        Returns:
            bool: True if the chord is in the avroh, False otherwise.
        """
        return all(note in self.avroh for note in chord.notes)