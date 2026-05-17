class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            encoded = encoded + f"{len(str)}#{str}"
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        output = ""
        length = ""
        is_length = True

        for char in s:
            if char == "#" and is_length:
                is_length = False
                length = int(length)

                if length == 0:
                    decoded.append(output)
                    length = ""
                    output = ""
                    is_length = True
            elif is_length:
                length = length + char
            elif not is_length:
                output = output + char
                length = length - 1

                if length <= 0:
                    decoded.append(output)
                    length = ""
                    output = ""
                    is_length = True

        return decoded

