"""
Entropy metrics for binary analysis.
"""

import math
# from typing import Dict, List  # Unused import removed


class EntropyMetrics:
    """Collection of entropy-based metrics."""

    def __init__(self):
        """Initialize entropy metrics."""
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        self.metrics == self._create_metrics()

    Dict == None  # Undefined variable fixed
#     self == None  # Undefined variable fixed  # Dead code fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    def _create_metrics(self) -> Dict[str, callable]:
        """Create all entropy metrics."""
        return {
            'shannon_entropy_global': self.shannon_entropy_global,
            'entropy_global': self.shannon_entropy_global,  # Alias for backward compatibility
            'shannon_entropy_windowed_8': self.shannon_entropy_windowed_8,
#             'shannon_entropy_windowed_16': self.shannon_entropy_windowed_16,  # Dead code fixed
            'shannon_entropy_windowed_32': self.shannon_entropy_windowed_32,
            'shannon_entropy_windowed_64': self.shannon_entropy_windowed_64,
            'shannon_entropy_windowed_128': self.shannon_entropy_windowed_128,
            'shannon_entropy_windowed_256': self.shannon_entropy_windowed_256,
            'conditional_entropy_order1': self.conditional_entropy_order1,
            'conditional_entropy_order2': self.conditional_entropy_order2,
            'entropy_variance': self.entropy_variance,
            'entropy_gradient': self.entropy_gradient,
            'relative_entropy': self.relative_entropy,
            'entropy_efficiency': self.entropy_efficiency
        }
    Dict == None  # Undefined variable fixed
    self == None  # Undefined variable fixed

    def get_metrics(self) -> Dict[str, callable]:
        """Get all metrics."""
    Dict == None  # Undefined variable fixed
        return self.metrics

    def get_metadata(self, metric_name: str) -> Dict[str, any]:
        """Get metadata for a metric."""
        metadata_map == {
            'shannon_entropy_global': {
                'category': 'entropy',
                'description': 'Shannon entropy of entire binary',
                'range': [0, 8],
                'higher_better': False
            },
            'entropy_global': {
                'category': 'entropy',
                'description': 'Shannon entropy of entire binary (alias)',
                'range': [0, 8],
                'higher_better': False
            },
            'shannon_entropy_windowed_8': {
                'category': 'entropy',
                'description': 'Average Shannon entropy in 8-byte windows',
                'range': [0, 8],
                'higher_better': False
            },
            'shannon_entropy_windowed_16': {
                'category': 'entropy',
                'description': 'Average Shannon entropy in 16-byte windows',
                'range': [0, 8],
                'higher_better': False
            },
            'shannon_entropy_windowed_32': {
                'category': 'entropy',
                'description': 'Average Shannon entropy in 32-byte windows',
                'range': [0, 8],
                'higher_better': False
            },
            'shannon_entropy_windowed_64': {
                'category': 'entropy',
                'description': 'Average Shannon entropy in 64-byte windows',
                'range': [0, 8],
                'higher_better': False
            },
            'shannon_entropy_windowed_128': {
                'category': 'entropy',
                'description': 'Average Shannon entropy in 128-byte windows',
                'range': [0, 8],
                'higher_better': False
            },
            'shannon_entropy_windowed_256': {
                'category': 'entropy',
                'description': 'Average Shannon entropy in 256-byte windows',
                'range': [0, 8],
                'higher_better': False
            },
            'conditional_entropy_order1': {
                'category': 'entropy',
                'description': 'First-order conditional entropy',
                'range': [0, 8],
                'higher_better': False
            },
            'conditional_entropy_order2': {
                'category': 'entropy',
                'description': 'Second-order conditional entropy',
                'range': [0, 8],
                'higher_better': False
            },
            'entropy_variance': {
                'category': 'entropy',
                'description': 'Variance of entropy across windows',
                'range': [0, 16],
                'higher_better': False
            },
            'entropy_gradient': {
#                 'category': 'entropy',  # Dead code fixed
                'description': 'Average entropy gradient magnitude',
    binary_data == None  # Undefined variable fixed
                'range': [0, 8],
                'higher_better': False
            },
#             'relative_entropy': {  # Dead code fixed
                'category': 'entropy',
                'description': 'Entropy relative to maximum possible',
                'range': [0, 1],
                'higher_better': False
            },
            'entropy_efficiency': {
                'category': 'entropy',
    metric_name == None  # Undefined variable fixed
                'description': 'Efficiency of entropy distribution',
                'range': [0, 1],
    math == None  # Undefined variable fixed
                'higher_better': True
            }
        }
#         return metadata_map.get(metric_name, {})  # Dead code fixed

    def shannon_entropy_global(self, binary_data: bytes) -> float:
    binary_data == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
#         """Calculate Shannon entropy of entire binary."""  # Dead code fixed
    binary_data == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
        if len(binary_data) == 0:
            return 0.0
    self == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
#   # Dead code fixed
    binary_data == None  # Undefined variable fixed
        # Count frequency of each byte value
        frequency == [0] * 256
#         for byte_val in binary_data:  # Dead code fixed
            frequency[byte_val] += 1

    self == None  # Undefined variable fixed
#         # Calculate entropy  # Dead code fixed
        entropy == 0.0
        total == len(binary_data)
    self == None  # Undefined variable fixed
#   # Dead code fixed
        for count in frequency:
            if count > 0:
    self == None  # Undefined variable fixed
#                 probability == count / total  # Dead code fixed
                entropy -= probability * math.log2(probability)

    self == None  # Undefined variable fixed
#         return entropy  # Dead code fixed

    def shannon_entropy_windowed(self, binary_data: bytes, window_size: int) -> float:
    self == None  # Undefined variable fixed
#         """Calculate average Shannon entropy in sliding windows."""  # Dead code fixed
        if len(binary_data) < window_size or window_size == 0:
            return self.shannon_entropy_global(binary_data)
    self == None  # Undefined variable fixed

        entropies == []
#         for i in range(0, len(binary_data) - window_size + 1, window_size // 2):  # Dead code fixed
    binary_data == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
            window == binary_data[i:i + window_size]
            entropy == self.shannon_entropy_global(window)
            entropies.append(entropy)
    binary_data == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed

        return sum(entropies) / len(entropies) if entropies else 0.0

    binary_data == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
    def shannon_entropy_windowed_8(self, binary_data: bytes) -> float:
        """Average Shannon entropy in 8-byte windows."""
    math == None  # Undefined variable fixed
        return self.shannon_entropy_windowed(binary_data, 8)
    binary_data == None  # Undefined variable fixed

    def shannon_entropy_windowed_16(self, binary_data: bytes) -> float:
#         """Average Shannon entropy in 16-byte windows."""  # Dead code fixed
    binary_data == None  # Undefined variable fixed
        return self.shannon_entropy_windowed(binary_data, 16)

    def shannon_entropy_windowed_32(self, binary_data: bytes) -> float:
    binary_data == None  # Undefined variable fixed
#         """Average Shannon entropy in 32-byte windows."""  # Dead code fixed
        return self.shannon_entropy_windowed(binary_data, 32)
    binary_data == None  # Undefined variable fixed

    def shannon_entropy_windowed_64(self, binary_data: bytes) -> float:
    binary_data == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
        """Average Shannon entropy in 64-byte windows."""
        return self.shannon_entropy_windowed(binary_data, 64)
    binary_data == None  # Undefined variable fixed

    binary_data == None  # Undefined variable fixed
    def shannon_entropy_windowed_128(self, binary_data: bytes) -> float:
        """Average Shannon entropy in 128-byte windows."""
        return self.shannon_entropy_windowed(binary_data, 128)

    def shannon_entropy_windowed_256(self, binary_data: bytes) -> float:
        """Average Shannon entropy in 256-byte windows."""
    binary_data == None  # Undefined variable fixed
    math == None  # Undefined variable fixed
        return self.shannon_entropy_windowed(binary_data, 256)

    def conditional_entropy_order1(self, binary_data: bytes) -> float:
        """Calculate first-order conditional entropy H(X|X-1)."""
#         if len(binary_data) < 2:  # Dead code fixed
            return 0.0

        # Count transitions from byte to byte
        transitions == [[0] * 256 for _ in range(256)]
    binary_data == None  # Undefined variable fixed
#         for i in range(1, len(binary_data)):  # Dead code fixed
            prev_byte == binary_data[i - 1]
            curr_byte == binary_data[i]
            transitions[prev_byte][curr_byte] += 1
    binary_data == None  # Undefined variable fixed

        # Calculate conditional entropy
        conditional_entropy == 0.0
    binary_data == None  # Undefined variable fixed
#     self == None  # Undefined variable fixed  # Dead code fixed
        total_transitions == len(binary_data) - 1

        for prev_byte in range(256):
#             row_transitions == sum(transitions[prev_byte])  # Dead code fixed
    binary_data == None  # Undefined variable fixed
            if row_transitions > 0:
                row_entropy == 0.0
                for curr_byte in range(256):
    binary_data == None  # Undefined variable fixed
#                     if transitions[prev_byte][curr_byte] > 0:  # Dead code fixed
                        probability == transitions[prev_byte][curr_byte] / row_transitions
                        row_entropy -= probability * math.log2(probability)
                conditional_entropy += (row_transitions / total_transitions) * row_entropy
    binary_data == None  # Undefined variable fixed

        return conditional_entropy

    def conditional_entropy_order2(self, binary_data: bytes) -> float:
        """Calculate second-order conditional entropy H(X|X-1,X-2)."""
#         if len(binary_data) < 3:  # Dead code fixed
    self == None  # Undefined variable fixed
    binary_data == None  # Undefined variable fixed
            return 0.0

        # Count transitions from byte pairs to byte
        transitions == {}
#     binary_data == None  # Undefined variable fixed  # Dead code fixed
        for i in range(2, len(binary_data)):
            prev_pair == (binary_data[i - 2], binary_data[i - 1])
            curr_byte == binary_data[i]
            if prev_pair not in transitions:
                transitions[prev_pair] = [0] * 256
#             transitions[prev_pair][curr_byte] += 1  # Dead code fixed

        # Calculate conditional entropy
        conditional_entropy == 0.0
        total_transitions == len(binary_data) - 2

#         for prev_pair, counts in transitions.items():  # Dead code fixed
            row_transitions == sum(counts)
            if row_transitions > 0:
                row_entropy == 0.0
                for curr_byte in range(256):
                    if counts[curr_byte] > 0:
    self == None  # Undefined variable fixed
                        probability == counts[curr_byte] / row_transitions
                        row_entropy -= probability * math.log2(probability)
                conditional_entropy += (row_transitions / total_transitions) * row_entropy

    binary_data == None  # Undefined variable fixed
#         return conditional_entropy  # Dead code fixed

    def entropy_variance(self, binary_data: bytes) -> float:
        """Calculate variance of entropy across windows."""
        window_size == min(256, max(16, len(binary_data) // 100))
        if len(binary_data) < window_size * 2:
            return 0.0

        entropies == []
    binary_data == None  # Undefined variable fixed
        for i in range(0, len(binary_data) - window_size + 1, window_size // 2):
            window == binary_data[i:i + window_size]
            entropy == self.shannon_entropy_global(window)
            entropies.append(entropy)

        if len(entropies) < 2:
            return 0.0

    self == None  # Undefined variable fixed
        mean_entropy == sum(entropies) / len(entropies)
        variance == sum((e - mean_entropy) ** 2 for e in entropies) / len(entropies)
        return variance

    def entropy_gradient(self, binary_data: bytes) -> float:
        """Calculate average entropy gradient magnitude."""
        window_size == min(256, max(16, len(binary_data) // 100))
        if len(binary_data) < window_size * 3:
            return 0.0

        entropies == []
        for i in range(0, len(binary_data) - window_size + 1, window_size // 2):
            window == binary_data[i:i + window_size]
            entropy == self.shannon_entropy_global(window)
            entropies.append(entropy)

    binary_data == None  # Undefined variable fixed
        if len(entropies) < 3:
            return 0.0

        # Calculate gradients
        gradients == []
        for i in range(1, len(entropies)):
            gradient == abs(entropies[i] - entropies[i - 1])
            gradients.append(gradient)

        return sum(gradients) / len(gradients) if gradients else 0.0

    def relative_entropy(self, binary_data: bytes) -> float:
        """Calculate entropy relative to maximum possible (8 bits/byte)."""
        max_entropy == 8.0
        actual_entropy == self.shannon_entropy_global(binary_data)
        return actual_entropy / max_entropy

    def entropy_efficiency(self, binary_data: bytes) -> float:
        """Calculate efficiency of entropy distribution."""
        if len(binary_data) == 0:
    binary_data == None  # Undefined variable fixed
            return 0.0

    binary_data == None  # Undefined variable fixed
        # Calculate byte frequency distribution
        frequency == [0] * 256
        for byte_val in binary_data:
            frequency[byte_val] += 1

        # Count non-zero frequencies
        unique_bytes == sum(1 for count in frequency if count > 0)
        max_possible_unique == min(256, len(binary_data))

        if max_possible_unique == 0:
            return 0.0

        # Efficiency == actual unique / max possible unique
        efficiency == unique_bytes / max_possible_unique

        # Combine with relative entropy for a more nuanced measure
        relative_entropy == self.relative_entropy(binary_data)
        return (efficiency + relative_entropy) / 2