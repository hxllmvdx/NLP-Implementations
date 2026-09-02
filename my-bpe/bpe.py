import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _(defaultdict):
    class MyBpe:
        def __init__(self):
            self._rules: dict[tuple[int, int], int] = {}
            self._vocab: dict[int, bytes] = {i: bytes([i]) for i in range(256)}

        @staticmethod
        def _get_freqs(tokens: list[int]) -> defaultdict:
            freqs = defaultdict(int)

            for i in range(1, len(tokens)):
                freqs[(tokens[i - 1], tokens[i])] += 1

            return freqs

        @staticmethod
        def _merge(tokens: list[int], pair: tuple[int, int], new_token: int) -> list[int]:
            new_tokens = []
            i = 0
            n = len(tokens)

            while i < n:
                if i < n -1 and tokens[i] == pair[0] and tokens[i + 1] == pair[1]:
                    new_tokens.append(new_token)
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1

            return new_tokens

        def train(self, data: str, epochs: int) -> None:
            tokens = list(data.encode("utf-8"))

            for step in range(epochs):
                freqs = self._get_freqs(tokens)
                if not freqs:
                    break

                best_pair = max(freqs, key=freqs.get)
                new_id = 256 + step

                new_tokens = []
                i = 0
                n = len(tokens)
            
                self._rules[best_pair] = new_id
                self._vocab[new_id] = self._vocab[best_pair[0]] + self._vocab[best_pair[1]]

                tokens = self._merge(tokens, best_pair, new_id)

        def encode(self, text: str) -> list[int]:
            tokens = list(text.encode("utf-8"))

            pairs = sorted(self._rules, key=self._rules.get)
            for pair in pairs:
                new_tokens = self._merge(tokens, pair, self._rules[pair])
            
                if new_tokens == tokens:
                    break
                
                tokens = new_tokens

            return tokens

        def decode(self, tokens: list[int]) -> str:
            res = bytes()

            for token in tokens:
                res += self._vocab[token]

            return res.decode("utf-8")

    return (MyBpe,)


@app.cell
def _(MyBpe):
    bpe = MyBpe()
    bpe.train("abracadabra", 3)
    return (bpe,)


@app.cell
def _(bpe):
    bpe.encode("abracadabra")
    return


@app.cell
def _(bpe):
    cadabra = bpe.encode("cadabra")
    cadabra
    return (cadabra,)


@app.cell
def _(bpe, cadabra):
    bpe.decode(cadabra)
    return


@app.cell(hide_code=True)
def _():
    from tqdm import tqdm
    from collections import defaultdict

    return (defaultdict,)


if __name__ == "__main__":
    app.run()
