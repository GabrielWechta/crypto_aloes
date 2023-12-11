import matplotlib.pyplot as plt
import numpy as np
import sys

# Set up the plots
fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 1]})
x = np.arange(65, 91)  # ASCII values for capital letters
bars = ax1.bar(x, np.zeros(26))
english_capital_letter_frequencies = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92,
    'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
    'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
}
sorted_capital_letters = [letter for letter, _ in sorted(english_capital_letter_frequencies.items(), key=lambda x: x[1], reverse=True)]
letters = sorted_capital_letters
frequencies = [english_capital_letter_frequencies[letter] for letter in sorted_capital_letters]

# Set up the plot labels and title for the interactive plot
ax1.set_xticks(x)
ax1.set_xticklabels([chr(i) for i in x])
ax1.set_ylim(0, 101)  # Initial y-axis limit in percentage
ax2.set_ylim(0, 1.1 * np.max(english_capital_letter_frequencies["E"]))
bars_constant = ax2.bar(letters, np.array(frequencies), color='gray', alpha=0.5)
plt.ion()  # Turn on interactive mode

# Initialize cumulative counts and max_count
cumulative_counts = np.zeros(26)
max_count = 10  # Initial maximum count (you can adjust this based on your input)

# Function to update the plot with given letter counts
def update_plot(letter_counts):
    global max_count
    global cumulative_counts

    # Update cumulative counts
    cumulative_counts += letter_counts

    # Update max_count based on the maximum count observed
    max_count = max(max_count, np.max(cumulative_counts))

    # Sort x-axis based on counts and then alphabetically
    sorted_indices = np.lexsort((x, -cumulative_counts))

    # Update the interactive plot data with sorted counts
    for bar, index in zip(bars, sorted_indices):
        bar.set_height((cumulative_counts[index] / np.sum(cumulative_counts)) * 100)

    # Dynamically set y-axis limit to accommodate the maximum count in percentage
    ax1.set_ylim(0, max_count / np.sum(cumulative_counts) * 100 + 1)

    # Update x-axis labels based on sorted indices
    ax1.set_xticklabels([chr(x[i]) for i in sorted_indices])

    # Calculate and display shift value in the legend
    most_frequent_letter_ascii = sorted_indices[0] + 65
    shift_value = most_frequent_letter_ascii - ord('E')
    ax1.legend([f'K={shift_value}'])

    # Redraw the interactive plot
    plt.draw()
    plt.pause(0.1)

# Read input from stdin in chunks of 10 characters
while True:
    try:
        user_input = sys.stdin.read(10)
        if not user_input:
            break  # Break the loop if no more input
    except KeyboardInterrupt:
        break  # Handle Ctrl+C to exit gracefully

    # Count the occurrences of capital letters in the current chunk
    letter_counts = np.zeros(26)
    for char in user_input:
        if 'A' <= char <= 'Z':
            letter_counts[ord(char) - 65] += 1

    # Update the interactive plot with the current chunk of letter counts
    update_plot(letter_counts)

# Turn off interactive mode at the end
plt.ioff()
plt.show()
