# Needleman-Wunsch Algorithm

This project implements the Needleman-Wunsch algorithm for global sequence alignment. The Needleman-Wunsch algorithm is a dynamic programming technique used in bioinformatics to align protein or DNA sequences. It was one of the first applications of dynamic programming to compare biological sequences, published in 1970 by Saul B. Needleman and Christian D. Wunsch.

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)

## Overview

The Needleman-Wunsch algorithm uses a scoring matrix to find the best global alignment between two sequences. Each cell in the matrix represents the best alignment score for the subsequences of the two sequences that end at that cell. The algorithm fills the matrix recursively, starting from the upper left corner and moving to the lower right corner, calculating scores based on matches, mismatches, and gaps.

After filling the matrix, the best alignment can be determined by tracing back from the lower right corner to the upper left corner.

## Features

- **Matrix Initialization**: Initializes the scoring matrix based on the input sequences and gap penalties.
- **Score Calculation**: Computes the alignment scores using match, mismatch, and gap penalties.
- **Traceback**: Retrieves the aligned sequences and the path taken to achieve the alignment.
- **Matrix Visualization**: Prints the scoring matrix for better understanding of the alignment process.

## Usage

To use the algorithm, run the script and provide the required inputs. The program will prompt you to enter two sequences along with the scoring parameters.

### Example

```python
# Run the script and follow the prompts
Enter sequence A: HEAGAWGHEE
Enter sequence B: PAWHEAE
Enter match score: 1
Enter mismatch penalty: -1
Enter gap penalty: -2
```

The output will display the aligned sequences, the alignment score, the scoring matrix, and the traceback path.

## Scoring Parameters

The algorithm uses several scoring parameters to determine the best alignment:

- **Match Score**: Points awarded for aligning identical characters.
- **Mismatch Penalty**: Points deducted for aligning different characters.
- **Gap Penalty**: Points deducted for introducing gaps in the alignment.

The choice of scoring parameters can significantly impact the resulting alignment.

## Significance of the Alignment

The significance of an alignment can be assessed by calculating the probability of obtaining a match score greater than the observed value, assuming a null model where the sequences are unrelated. One approach to assess significance is to use the extreme value distribution (EVD).

## Deriving Score Parameters

Scoring parameters can be derived from alignment data using various techniques. Common methods include:

- **PAM Matrices**: Derived from alignments between very similar proteins.
- **BLOSUM Matrices**: Derived from alignments of ungapped regions from protein families.

## Additional Considerations

- The Needleman-Wunsch algorithm is a **global** alignment algorithm, meaning it attempts to align the entire sequences.
- The algorithm has a time complexity of **O(nm)**, where n and m are the lengths of the sequences.
- Various **heuristics** can be used to speed up the alignment process, such as BLAST and FASTA.

## Further Reading

- Durbin, R., Eddy, S. R., Krogh, A., & Mitchison, G. (1998). Biological Sequence Analysis: Probabilistic Models of Proteins and Nucleic Acids. Cambridge University Press.
- Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. Journal of Molecular Biology, 48(3), 443-453.
## License.

[![License](https://img.shields.io/github/license/vncsmnl/guiadoprogramador?style=flat&logo=github&color=blue)](/LICENSE)

```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```