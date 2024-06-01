# Lossless Compression #

# Dataset

[enwiki9.zip](http://prize.hutter1.net/)

# Various algos #

- [x] LZSS
- [ ] Huffman
- [ ] Arithmetic
- [ ] Dynamic Markov

# Rules #

- python runtime is included
- compression ratio is source_size / (compressed + decode.py + model_weights)
- integrity is compared with diff

# Eval #

```
./eval_sh <compression_algo_directory>
```
