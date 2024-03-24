from bidict import bidict
from typing import List, Union, Set

class Note:
    """
    Represents a musical note from indian classical music.

    Attributes:
        notes (bidict): A bidirectional dictionary mapping note values to note notations.
        note_value (int): The value of the note i.e. the distance of the note from the tonic note (Sa).
        base_value (int): The base note value obtained by taking the modulo of the note value with 12 (since there are 12 notes in the chromatic scale).
        saptak (int): The saptak (a.k.a. octave) value obtained by dividing the note value by the length of the notes dictionary.
        base_notation (str): The base notation of the note obtained from the notes dictionary using the base note value.
        notation (str): The complete notation of the note, including the base notation and any octave modifiers (+ or -).
    """
    
    notes: bidict[int, str]
    note_value: int
    base_value: int
    saptak: int
    base_notation: str
    notation: str
    
    notes: bidict = bidict({
        0 : 's' ,
        1 : 'r.',
        2 : 'r' ,
        3 : 'g.',
        4 : 'g' ,
        5 : 'm' ,
        6 : 'm*',
        7 : 'p' ,
        8 : 'd.',
        9 : 'd' ,
        10: 'n.',
        11: 'n' ,
    })
    
    def __init__(self, input: Union[int, str]) -> None:
        """
        Initializes a Note object.
        
        Args:
            input (Union[int, str]): The input can be either an integer representing the note value or a string representing the note notation.
        
        Raises:
            ValueError: If the input is neither an integer nor a string.
        """
        if isinstance(input, int):
            self.init_from_value(input)
        elif isinstance(input, str):
            self.init_from_notation(input)
        else:
            raise ValueError('Input must be an integer or a string.')
    
    
    def init_from_value(self, note_value: int) -> None:
        """
        Initializes a Note object from a note value.
        
        Args:
            note_value (int): The note value.
        """
        self.note_value: int = note_value
        self.base_value: int = self.note_value % len(self.notes)
        self.saptak: int = self.note_value // len(self.notes)
        self.base_notation: str = self.notes[self.base_value]
        self.notation: str = self.base_notation + ('+' * self.saptak) if self.saptak > 0 else self.base_notation + ('-' * abs(self.saptak))


    def init_from_notation(self, notation: str) -> None:
        """
        Initializes a Note object from a note notation.
        
        Args:
            notation (str): The note notation.
        """
        self.notation: str = notation
        self.base_notation: str = self.notation.replace('+', '').replace('-', '')
        self.saptak: int = self.notation.count('+') - self.notation.count('-')
        self.base_value: int = self.notes.inverse[self.base_notation]
        self.note_value: int = self.base_value + self.saptak * len(self.notes)
    
    
    def getattr(self, attr: str) -> Union[int, str]:
        """
        Gets the value of the specified attribute.
        
        Args:
            attr (str): The name of the attribute.
        
        Returns:
            Union[int, str]: The value of the specified attribute.
        """
        return getattr(self, attr)
    
    
    def __str__(self) -> str:
        """
        Returns the string representation of the Note object.
        
        Returns:
            str: The string representation of the Note object.
        """
        return self.notation

    
    def __repr__(self) -> str:
        """
        Returns the string representation of the Note object.
        
        Returns:
            str: The string representation of the Note object.
        """
        return self.notation
    
    
    def __add__(self, other: int) -> 'Note':
        """
        Adds an integer to the note value.
        
        Args:
            other (int): The integer to be added to the note value.
        
        Returns:
            Note: The resulting Note object.
        """
        return Note(self.note_value + other)
    
    
    def __sub__(self, other: int) -> 'Note':
        """
        Subtracts an integer from the note value.
        
        Args:
            other (int): The integer to be subtracted from the note value.
        
        Returns:
            Note: The resulting Note object.
        """
        return Note(self.note_value - other)
    
    
    def __eq__(self, other: 'Note') -> bool:
        """
        Checks if the note values are equal.
        
        Args:
            other (Note): The other Note object.
        
        Returns:
            bool: True if the note values are equal, False otherwise.
        """
        return self.note_value == other.note_value
    
    
    def __ne__(self, other: 'Note') -> bool:
        """
        Checks if the note values are not equal.
        
        Args:
            other (Note): The other Note object.
        
        Returns:
            bool: True if the note values are not equal, False otherwise.
        """
        return self.note_value != other.note_value
    
    
    def __lt__(self, other: 'Note') -> bool:
        """
        Checks if the note value is less than the other note value.
        
        Args:
            other (Note): The other Note object.
        
        Returns:
            bool: True if the note value is less than the other note value, False otherwise.
        """
        return self.note_value < other.note_value
    
    
    def __le__(self, other: 'Note') -> bool:
        """
        Checks if the note value is less than or equal to the other note value.
        
        Args:
            other (Note): The other Note object.
        
        Returns:
            bool: True if the note value is less than or equal to the other note value, False otherwise.
        """
        return self.note_value <= other.note_value
    
    
    def __gt__(self, other: 'Note') -> bool:
        """
        Checks if the note value is greater than the other note value.
        
        Args:
            other (Note): The other Note object.
        
        Returns:
            bool: True if the note value is greater than the other note value, False otherwise.
        """
        return self.note_value > other.note_value
    
    
    def __ge__(self, other: 'Note') -> bool:
        """
        Checks if the note value is greater than or equal to the other note value.
        
        Args:
            other (Note): The other Note object.
        
        Returns:
            bool: True if the note value is greater than or equal to the other note value, False otherwise.
        """
        return self.note_value >= other.note_value
    
    
    def __hash__(self) -> int:
        """
        Returns the hash value of the Note object.
        
        Returns:
            int: The hash value of the Note object.
        """
        return hash(self.note_value)
    
    
    def shift_saptak(self, n: int) -> 'Note':
        """
        Shifts the note by the specified number of saptaks.
        
        Args:
            n (int): The number of saptaks to shift the note.
        
        Returns:
            Note: The resulting Note object.
        """
        return Note(self.note_value + n * len(self.notes))
    
    
    def get_distance(self, other: 'Note') -> int:
        """
        Gets the distance between the note and another note.
        
        Args:
            other (Note): The other Note object.
        
        Returns:
            int: The distance between the note and the other note.
        """
        return abs(self.note_value - other.note_value)

    
    def get_base_note(self) -> 'Note':
        """
        Gets the base note of the note.
        
        Returns:
            Note: The base note of the note.
        """
        return Note(self.base_value)