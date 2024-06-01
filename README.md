# Lossless Compression #

[Lossless compression](https://en.wikipedia.org/wiki/Lossless_compression) is a class of data compression that allows the original data to be perfectly reconstructed from the compressed data with no loss of information. 

This repo contains some implementations of popular compression algorithms, focused on correctness and readability. 

## Dataset

[enwiki9](http://prize.hutter1.net/) from the Hutter prize

## Various algos

- [ ] LZSS
- [ ] Huffman
- [ ] Arithmetic
- [ ] Dynamic Markov

## Rules

- python runtime is included
- compression ratio is source_size / (compressed + decode.py + model_weights)
- integrity is compared with diff

## Eval

```
./eval_sh <compression_algo_directory>
```

## Todo

- [ ] Detailed writeup on each algorithm
- [ ] Or provide some good sources
