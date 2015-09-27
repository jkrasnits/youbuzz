"""Read lines from a file, feed them into the markov generator, and then
generate a few lines.

Usage:
  python from_file.py <input_filename> <num_lines_to_generate>
"""
import sys

import sujmarkov


def extract_sentences(input_file):
    # Each line is a sentence.
    #
    for raw_line in input_file:
        line = raw_line.lower().strip()

        # For now, ignore punctuation.
        #
        line = line.replace(",", "").replace("-", "").replace('"', '')

        for sub_line in line.split("."):
            raw_sentence = sub_line.split(" ")

            sentence = [word for word in raw_sentence if word and word.strip() != ""]
            if sentence:
                yield sentence


if __name__ == "__main__":
    m = sujmarkov.Markov(n=2)

    with open(sys.argv[1], "r") as input_file:
        for sentence in extract_sentences(input_file):
            m.add(sentence)

    num_required = int(sys.argv[2])
    num_done = 0

    while num_done < num_required:
        generated_sentence = " ".join(m.generate())
        print generated_sentence
        num_done += 1
