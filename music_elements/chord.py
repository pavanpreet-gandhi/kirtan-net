from .note import Note
from typing import List, Union

class Chord:
    """
    Represents a musical chord.

    Attributes:
        notes (List[Note]): The list of Note objects that make up the chord.
        root_note (Note): The root Note object of the chord.
        intervals (List[int]): The list of intervals that make up the chord.
    """
    
    def __init__(self, notes: Union[List[Note], Note], intervals: List[int] = None):
        """
        Initializes a Chord object with a list of notes or a single note and a list of chord intervals.

        Args:
            notes (Union[List[Note], Note]): The list of Note objects that make up the chord or a single Note object.
            intervals (List[int], optional): The list of chord intervals. Defaults to None.
        """
        if isinstance(notes, list):
            self.notes = sorted(notes)
            self.root_note = self.notes[0]
            self.intervals = [note.note_value - notes[0].note_value for note in notes]
        else:
            self.root_note = notes
            self.notes = [self.root_note + interval for interval in intervals]
            self.intervals = intervals


    def __repr__(self) -> str:
        """
        Returns a string representation of the Chord object.

        Returns:
            str: The string representation of the Chord object.
        """
        return f"Chord({self.notes})"


    def __str__(self) -> str:
        """
        Returns a string representation of the Chord object.

        Returns:
            str: The string representation of the Chord object.
        """
        return f"Chord({self.notes})"
    
    
    def __iter__(self):
        """
        Returns an iterator for the Chord object.

        Returns:
            Iterator: An iterator for the Chord object.
        """
        return iter(self.notes)
    
    
    def __len__(self) -> int:
        """
        Returns the length of the Chord object.

        Returns:
            int: The length of the Chord object.
        """
        return len(self.notes)
    
    
    def __getitem__(self, index: int) -> Note:
        """
        Gets the Note object at the specified index.

        Args:
            index (int): The index of the Note object.

        Returns:
            Note: The Note object at the specified index.
        """
        return self.notes[index]
    
    
    def __eq__(self, other: 'Chord') -> bool:
        """
        Checks if the Chord objects are equal.

        Args:
            other (Chord): The other Chord object.

        Returns:
            bool: True if the Chord objects are equal, False otherwise.
        """
        return self.notes == other.notes
    
    
    def __gt__(self, other: 'Chord') -> bool:
        """
        Checks if the Chord object is greater than the other Chord object.

        Args:
            other (Chord): The other Chord object.

        Returns:
            bool: True if the Chord object is greater than the other Chord object, False otherwise.
        """
        return self.notes[::-1] > other.notes[::-1]
    
    
    def __ge__(self, other: 'Chord') -> bool:
        """
        Checks if the Chord object is greater than or equal to the other Chord object.

        Args:
            other (Chord): The other Chord object.

        Returns:
            bool: True if the Chord object is greater than or equal to the other Chord object, False otherwise.
        """
        return self.notes[::-1] >= other.notes[::-1]
    
    
    def __le__(self, other: 'Chord') -> bool:
        """
        Checks if the Chord object is less than or equal to the other Chord object.

        Args:
            other (Chord): The other Chord object.

        Returns:
            bool: True if the Chord object is less than or equal to the other Chord object, False otherwise.
        """
        return self.notes[::-1] <= other.notes[::-1]
    
    
    def __lt__(self, other: 'Chord') -> bool:
        """
        Checks if the Chord object is less than the other Chord object.

        Args:
            other (Chord): The other Chord object.

        Returns:
            bool: True if the Chord object is less than the other Chord object, False otherwise.
        """
        return self.notes[::-1] < other.notes[::-1]
    
    
    def __hash__(self) -> int:
        """
        Returns the hash value of the Chord object.

        Returns:
            int: The hash value of the Chord object.
        """
        return hash(tuple(self.notes))
    
    
    @staticmethod
    def invert_intervals(intervals: List[int]) -> List[int]:
        """
        Inverts the list of intervals.

        Args:
            intervals (List[int]): The list of intervals.

        Returns:
            List[int]: The inverted list of intervals.
        """
        new_intervals = intervals[1:] + [intervals[0]+len(Note.notes)] # e.g. [0, 4, 7] -> [4, 7, 12]
        new_intervals = [interval - intervals[1] for interval in new_intervals] # e.g. [4, 7, 12] -> [0, 3, 8]
        return new_intervals
    
    
    def invert(self, n: int = 1) -> 'Chord':
        """
        Inverts the chord by n times.

        Args:
            n (int, optional): The number of times to invert the chord. Defaults to 1.

        Returns:
            Chord: The inverted Chord object.
        """
        new_intervals = self.intervals
        for _ in range(n):
            new_intervals = self.invert_intervals(new_intervals)
        return Chord(self.root_note, new_intervals)
    