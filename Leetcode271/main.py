from typing import List
import time

class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = "<E/>".join(strs)
        if not strs:
            return "<None/>"
        return ret

    def decode(self, s: str) -> List[str]:
        if s == "<None/>":
            return []
        return s.split("<E/>")

# Driver code
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ["Hello", "World"],
        [""],
        ["Hello", "World", "!"],
        [],
    ]
    
    for i, strs in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print(f"Original: {strs}")
        
        # Encode
        start_time = time.perf_counter()
        encoded = sol.encode(strs)
        encode_time = time.perf_counter() - start_time
        print(f"Encoded: {encoded}")
        print(f"Encode time: {encode_time:.6f} seconds")
        
        # Decode
        start_time = time.perf_counter()
        decoded = sol.decode(encoded)
        decode_time = time.perf_counter() - start_time
        print(f"Decoded: {decoded}")
        print(f"Decode time: {decode_time:.6f} seconds")
        
        # Verify
        assert strs == decoded, f"Test case {i + 1} failed: original and decoded lists don't match"
    
    print("\nAll test cases passed successfully!")