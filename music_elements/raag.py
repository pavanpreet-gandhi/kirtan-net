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


    def __contains__(self, item: Union[Note, Chord]) -> bool:
        """
        Checks if a given Note or Chord object is in the raag.

        Args:
            item (Union[Note, Chord]): The Note or Chord object to check.

        Returns:
            bool: True if the Note or Chord object is in the raag, False otherwise.
        """
        if isinstance(item, Note):
            return item.get_base_note() in self.notes
        elif isinstance(item, Chord):
            return all(note.get_base_note() in self.notes for note in item.notes)
        else:
            return False
    
    
    def aroh_contains(self, item: Union[Note, Chord]) -> bool:
        """
        Checks if a given Note or Chord object is in the aroh of the raag.

        Args:
            item (Union[Note, Chord]): The Note or Chord object to check.

        Returns:
            bool: True if the Note or Chord object is in the aroh of the raag, False otherwise.
        """
        if isinstance(item, Note):
            return item.get_base_note() in self.aroh
        elif isinstance(item, Chord):
            return all(note.get_base_note() in self.aroh for note in item.notes)
        else:
            return False
    
    
    def avroh_contains(self, item: Union[Note, Chord]) -> bool:
        """
        Checks if a given Note or Chord object is in the avroh of the raag.

        Args:
            item (Union[Note, Chord]): The Note or Chord object to check.

        Returns:
            bool: True if the Note or Chord object is in the avroh of the raag, False otherwise.
        """
        if isinstance(item, Note):
            return item.get_base_note() in self.avroh
        elif isinstance(item, Chord):
            return all(note.get_base_note() in self.avroh for note in item.notes)
        else:
            return False