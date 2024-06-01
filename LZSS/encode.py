window_sz       = 4096
lookahead_sz    = 15
min_match_len   = 4
compressed_path = "./compressed.bin"
source_path     = "./source.bin"
data_path       = "../enwik9/enwik9"

def ref_tokenize(match_pos, curr, match_len):
    ref_bits = format(curr-match_pos, f'012b')
    len_bits = format(match_len, f'012b')
    combined_bits = ref_bits + len_bits
    combined_bytes = int(combined_bits, 2).to_bytes(3, byteorder='big')
    return b'\xFF' + combined_bytes

with open(data_path, "r") as f:
    data = f.read()[:10024]
    compressed = bytearray()
    curr = 0
    while curr < len(data):
        match_len = 0
        match_pos = 0
        
        window_sz = window_sz - 1 if curr + window_sz == len(data) else window_sz
        for i in range(max(0, curr - window_sz), curr):
            length = 0
            while (curr + length < len(data) 
                    and length < lookahead_sz
                    and data[i + length] == data[curr+length]):
                    length += 1

            if length > match_len:
                match_len = length
                match_pos = i

        if match_len >= min_match_len and curr < len(data) - window_sz:
            ref_token = ref_tokenize(match_pos, curr, match_len)
            compressed += ref_token
            curr += match_len

        else:
            literal = data[curr].encode("utf-8")
            compressed += literal
            curr += 1

    with open(source_path, "wb") as f_0:
        f_0.write(data.encode("utf-8"))

    with open(compressed_path, "wb") as f_1:
        f_1.write(compressed)

    compression_ratio = len(data)/len(compressed)
    print(f"Source file size: {len(data)}")
    print(f"Compressed file size: {len(compressed)}")
    print(f"Compression ratio: {round(compression_ratio, 2)}")
    print(f"Compressed file saved to {compressed_path}")
