def encrypt_line(line):
    shifted = ''.join(
        chr(ord(char) + 3) if char.isalpha() else char
        for char in line
    )

    reversed_line = shifted[::-1]

    mid = len(reversed_line) // 2
    result = reversed_line[:mid] + ''.join(
        chr(ord(char) - 1) for char in reversed_line[mid:]
    )

    return result


n = int(input().strip())

encrypted_lines = []
for _ in range(n):
    line = input().strip()
    encrypted_lines.append(encrypt_line(line))

print('\n'.join(encrypted_lines))
