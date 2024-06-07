class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort the dictionary to ensure shorter roots are checked first
        dictionary.sort(key=len)
        
        # Split the sentence into individual words
        words = sentence.split()
        
        # Create a set from the dictionary for quick lookup
        root_set = set(dictionary)
        
        def find_root(word: str) -> str:
            # Try to find the shortest root for the given word
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]
            return word
        
        # Replace each word in the sentence with its shortest root if it exists
        replaced_words = [find_root(word) for word in words]
        
        # Join the replaced words into a single string and return
        return " ".join(replaced_words)
