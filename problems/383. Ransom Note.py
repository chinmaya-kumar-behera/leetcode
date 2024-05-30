from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in ransomNote and magazine
        ransom_note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        # Check if for each character in ransomNote, magazine has enough characters
        for char, count in ransom_note_count.items():
            if magazine_count[char] < count:
                return False
        
        return True
