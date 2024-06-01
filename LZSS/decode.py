compressed_path = "./compressed.bin"
decompressed_path = "./decompressed.bin"

def decode_ref_token(token):
    combined_bits = format(int.from_bytes(token, byteorder='big'), '024b')
    ref_bits = combined_bits[:12]
    len_bits = combined_bits[12:]
    ref = int(ref_bits, 2)
    match_len = int(len_bits, 2)
    return ref, match_len

with open(compressed_path, "rb") as f:
    compressed = f.read()
    decompressed = bytearray()
    curr = 0

    while curr < len(compressed):
        if compressed[curr] == 0xFF:
            ref, match_len = decode_ref_token(compressed[curr+1:curr+4])
            start = len(decompressed) - ref
            end = start + match_len
            decompressed.extend(decompressed[start:end])
            curr += 4
        else:
            decompressed.append(compressed[curr])
            curr += 1

    decompressed_text = decompressed.decode("utf-8")

    with open(decompressed_path, "w") as f:
        f.write(decompressed_text)

    print(f"Decompressed file saved to {decompressed_path}")
