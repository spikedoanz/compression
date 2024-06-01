window_sz       = 4096
lookahead_sz    = 15
min_match_len   = 4
compressed_path = "./compressed.bin"
source_path     = "./source.bin"
data_path       = "../enwik9/enwik9"

with open(data_path, "r") as f:
    data = f.read()[:10000]
    compressed = bytearray()
    curr = 0

    while curr < len(data):
        literal = data[curr].encode("utf-8")
        compressed += literal
        curr += 1

    with open(source_path, "wb") as f_0:
        f_0.write(data.encode("utf-8"))

    with open(compressed_path, "wb") as f_1:
        f_1.write(compressed)

    compression_ratio = len(data)/len(compressed)
    print(f"Source file size: {len(data)} bytes")
    print(f"Compressed file size: {len(compressed)} bytes")
    print(f"Compression ratio: {round(compression_ratio, 2)}")
    print(f"Compressed file saved to {compressed_path}")
