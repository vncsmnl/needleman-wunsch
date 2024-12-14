class Alignment:
    def __init__(self, match_score, mismatch_penalty, gap_penalty):
        self.match_score = match_score
        self.mismatch_penalty = mismatch_penalty
        self.gap_penalty = gap_penalty
        self.matrix = []
        self.score = 0

    def initialize_matrix(self, seq_a, seq_b):
        height = len(seq_a) + 1
        width = len(seq_b) + 1
        self.matrix = [[0] * width for _ in range(height)]

        # Initialize left upper corner
        self.matrix[0][0] = 0

        # Initialize left matrix border
        for i in range(1, height):
            self.matrix[i][0] = self.matrix[i - 1][0] + self.gap_penalty

        # Initialize upper matrix border
        for j in range(1, width):
            self.matrix[0][j] = self.matrix[0][j - 1] + self.gap_penalty

    def compute_matrix_and_score(self, seq_a, seq_b):
        for i in range(1, len(seq_a) + 1):
            for j in range(1, len(seq_b) + 1):
                a_char = seq_a[i - 1]
                b_char = seq_b[j - 1]
                score = self.match_score if a_char == b_char else self.mismatch_penalty
                self.matrix[i][j] = self.recursion_function(
                    self.matrix[i - 1][j - 1] + score,  # diagonal
                    self.matrix[i - 1][j] + self.gap_penalty,  # up
                    self.matrix[i][j - 1] + self.gap_penalty   # left
                )
        self.score = self.matrix[len(seq_a)][len(seq_b)]

    def recursion_function(self, diagonal_value, up_value, left_value):
        return max(diagonal_value, up_value, left_value)

    def compute_traceback(self, seq_a, seq_b):
        i, j = len(seq_a), len(seq_b)
        alignment_a, alignment_b = [], []
        traceback_path = []

        while i > 0 and j > 0:
            current_score = self.matrix[i][j]
            diagonal_score = self.matrix[i - 1][j - 1]
            up_score = self.matrix[i - 1][j]
            left_score = self.matrix[i][j - 1]

            if current_score == diagonal_score + (self.match_score if seq_a[i - 1] == seq_b[j - 1] else self.mismatch_penalty):
                alignment_a.append(seq_a[i - 1])
                alignment_b.append(seq_b[j - 1])
                traceback_path.append((i, j))
                i -= 1
                j -= 1
            elif current_score == up_score + self.gap_penalty:
                alignment_a.append(seq_a[i - 1])
                alignment_b.append('-')
                traceback_path.append((i, j))
                i -= 1
            else:
                alignment_a.append('-')
                alignment_b.append(seq_b[j - 1])
                traceback_path.append((i, j))
                j -= 1

        while i > 0:
            alignment_a.append(seq_a[i - 1])
            alignment_b.append('-')
            traceback_path.append((i, 0))
            i -= 1

        while j > 0:
            alignment_a.append('-')
            alignment_b.append(seq_b[j - 1])
            traceback_path.append((0, j))
            j -= 1

        return ''.join(reversed(alignment_a)), ''.join(reversed(alignment_b)), traceback_path

    def print_matrix(self, seq_a, seq_b):
        print("\nAlignment Matrix:")

        cell_width = max(len(str(val)) for row in self.matrix for val in row) + 2

        print("  " * cell_width, end="")
        for b in seq_b:
            print(f" {b:>{cell_width - 1}}", end="")
        print()

        print("-" * (len(seq_b) * cell_width + cell_width))

        for i in range(len(seq_a) + 1):
            if i == 0:
                print(f"{' ':{cell_width}}", end="")
            else:
                print(f"{seq_a[i - 1]:>{cell_width}}", end="")

            for j in range(len(seq_b) + 1):
                print(f"{self.matrix[i][j]:>{cell_width}}", end="")
            print()

    def print_traceback(self, traceback_path):
        print("\nTraceback Path:")
        for (i, j) in traceback_path:
            print(f"({i}, {j})", end=" -> ")
        print("END")


def main():
    # Input from user
    seq_a = input("Enter sequence A: ")
    seq_b = input("Enter sequence B: ")
    match_score = int(input("Enter match score: "))
    mismatch_penalty = int(input("Enter mismatch penalty: "))
    gap_penalty = int(input("Enter gap penalty: "))

    alignment = Alignment(match_score, mismatch_penalty, gap_penalty)
    alignment.initialize_matrix(seq_a, seq_b)
    alignment.compute_matrix_and_score(seq_a, seq_b)

    # Get the aligned sequences and the traceback path
    alignment_a, alignment_b, traceback_path = alignment.compute_traceback(seq_a, seq_b)

    # Print the results
    print(f"\nAligned Sequence A: {alignment_a}")
    print(f"Aligned Sequence B: {alignment_b}")
    print(f"Alignment Score: {alignment.score}")  # Print the alignment score
    alignment.print_matrix(seq_a, seq_b)  # Print the matrix with sequences A and B
    alignment.print_traceback(traceback_path)


# Run the main function
if __name__ == "__main__":
    main()
