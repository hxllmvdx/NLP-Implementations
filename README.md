# NLP Implementations

## Contents

- [About](#about)
  - [Limitations](#limitations)
  - [Discussions](#discussions)
- [Environment](#environment)
- [Interacting with project](#interacting-with-project)
- [Byte-Level BPE](#byte-level-bpe)

## About

In this repo I tried to implement some widely used NLP algorithms. The goal is not to compete with well-known libraries, but to provide clear, minimal implementations that help understand concepts such as Byte-Level BPE or Decoder-only architecture.

### Limitations

My implementations may be incomplete, lacking in usability, or slower/less optimized than production-grade libraries. They are meant for learning and exploration, not for production use.

### Discussions

You are welcome to use this repo as you wish. If you have questions, feedback, or ideas, feel free to leave them in the [Discussions](../../discussions) section.

## Environment

This project uses `uv` (just because I like it), so you can create your own `.venv` by running

```bash
uv sync
```

If you haven't heard of it and want to learn more, check out the [official documentation](https://docs.astral.sh/uv/).

Instead of the usual Jupyter Notebook, I use **marimo** — a modern notebook editor. For exploring my work, you don't need to know its specific features: you can use it just like a regular Jupyter Notebook by running every cell from top to bottom with `Shift+Enter` or by clicking the `Run` button. If you want to learn more, check out the [official documentation](https://docs.marimo.io/).

Other libraries can be found in `pyproject.toml`.

## Interacting with project

To interact with the notebooks, run

```bash
uv run marimo edit .
```

After running it, `marimo` will open a page in your browser, where you'll be able to interact with files and folders by clicking the corresponding icons in the **Workspace** section at the bottom of the screen.

## Byte-Level BPE

In the `my-bpe` directory, I implemented a basic version of Byte-Level BPE (BBPE). It follows the same core logic as the original algorithm, but without pre-tokenization and other optimizations found in production implementations. It's pure Python, simple, and works as expected: it takes each pair of bytes, computes their frequencies, merges the most frequent pair into a new token (ID), and repeats this process as many times as needed.
