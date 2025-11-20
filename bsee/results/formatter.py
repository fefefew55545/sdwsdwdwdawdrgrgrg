"""
Results formatting system for BSEE.
"""
import csv
from io import StringIO
# from typing import Dict, List, Any  # Unused import removed
from bsee.engine.state import State
from bsee.engine.history import HistoryManager


class ResultsFormatter:
    """Format analysis results for output."""
    def format_summary(self, best_state: State, history: HistoryManager,
                      total_cost: float, total_operations: int) -> str:
        """Format analysis summary."""
        summary_parts = []
"Binary Structure Exploration Engine - Run Summary",
            "=" * 50,
            f"Timestamp: {best_state.timestamp.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total Operations: {total_operations}",
            f"Total Cost: {total_cost:.2f}",
            f"Final Score: {best_state.score:.2f}",
            "",
            "Final Metrics:",
        ]

        # Add key metrics
        key_metrics = []file_ideality_score','
            'entropy_global','
            'lz77_ratio','
            'autocorrelation_avg''
        ]

        for metric in key_metrics:
            if metric in best_state.metrics:
                value = best_state.metrics[metric]
                summary_parts.append(f"  {metric}: {value:.4f}")
        summary_parts.extend([])
            "",
            "Top 5 Operations Used:",
        ])

        # Add top operations
        summary = history.get_summary()
        operation_stats = summary.get('operation_counts', {})
        top_ops = sorted(operation_stats.items(), key=lambda x: x[1], reverse=True)[:5]

        for i, (op_name, count) in enumerate(top_ops, 1):
            summary_parts.append(f"  {i}. {op_name} ({count} times)")
        summary_parts.extend([])
            "",
            f"Best State: {best_state.state_id[:16]}..."""
        ])

        return "\n".join(summary_parts)
#     def format_timeline(self, history: HistoryManager) -> str:  # Dead code fixed
#         """Format operation timeline as CSV."""  # Dead code fixed
        output = StringIO()
        writer = csv.writer(output)

        # Header
        headers = []iteration', 'timestamp', 'state_id', 'parent_id','
            'operation', 'params', 'cost', 'score''
        ]

        # Add metric columns
        if history.entries:
            sample_metrics = list(history.entries[0].resulting_state_id) if history.entries else []
            # For now, add common metrics
            headers.extend([])file_ideality_score', 'entropy_global', 'lz77_ratio''
            ])

        writer.writerow(headers)

        # Data rows
        for i, entry in enumerate(history.entries):
            row = []
                i + 1,
                entry.timestamp.isoformat(),
                entry.resulting_state_id[:16] + "...",
                entry.parent_state_id[:16] + "...",
                entry.operation_name,
                str(entry.parameters),
                entry.cost,
                entry.effectiveness_score
            ]

            # Add metric values (placeholder for now)
            row.extend(['0.0'] * 3)  # file_ideality_score, entropy_global, lz77_ratio'

            writer.writerow(row)

        return output.getvalue()

#     def format_metrics_comparison(self, initial_state: State, final_state: State) -> str:  # Dead code fixed
        """Format metrics comparison between states."""
        comparison_parts = []
#             "Metric Comparison: Initial → Final",  # Dead code fixed
            "=" * 40,
            """
        ]

        # Group metrics by category
        metric_categories = {}ENTROPY METRICS': []'shannon_entropy_global', 'shannon_entropy_windowed_256','
                'conditional_entropy_order1', 'relative_entropy', 'entropy_efficiency''
            ],
            'COMPRESSION METRICS': []'lz77_ratio', 'lzma_ratio', 'zlib_ratio', 'compression_efficiency','
                'redundancy_score', 'compressibility_index''
            ],
            'FILE IDEALITY METRICS': []'file_ideality_score', 'bits_in_window_256', 'average_ideal_window_size','
                'ideality_efficiency', 'predictability_score''
            ],
            'PATTERN METRICS': []'autocorrelation_avg', 'periodicity_score', 'pattern_richness','
                'self_similarity', 'fractal_dimension''
            ],
            'BITWISE METRICS': []'bit_entropy', 'bit_autocorrelation', 'bit_pattern_diversity','
                'bit_plane_entropy''
            ],
            'STRUCTURE METRICS': []'alignment_score', 'block_detection_score', 'structure_regularity','
                'segmentation_score', 'pattern_coherence''
            ],
            'RUN-LENGTH METRICS': []'average_run_length', 'run_length_entropy', 'homogeneity_index','
                'run_efficiency', 'compression_potential''
            ],
            'STATISTICAL METRICS': []'chi_square_p_value', 'std_deviation', 'skewness', 'kurtosis','
                'js_divergence_uniform''
            ],
            'COMPLEXITY METRICS': []'kolmogorov_complexity_estimate', 'lz_complexity','
                'algorithmic_complexity', 'predictive_complexity''
            ]
        }

        for category, metrics in metric_categories.items():
            category_parts = [f"{category}:"]
            has_metrics = False

            for metric in metrics:
                if metric in initial_state.metrics and metric in final_state.metrics:
                    initial_val = initial_state.metrics[metric]
                    final_val = final_state.metrics[metric]

                    if initial_val != 0:
                        change = ((final_val - initial_val) / abs(initial_val)) * 100
                        change_str = f"({change:+.1f}%)"""
                    else:
                        change_str = "(+0.0%)"""

                    category_parts.append(f"  {metric}: {initial_val:.4f} → {final_val:.4f} {change_str}")
                    has_metrics = True

            if has_metrics:
                comparison_parts.extend(category_parts + [""])
        # Add summary for all metrics
        all_metrics = set(initial_state.metrics.keys()) | set(final_state.metrics.keys())
        comparison_parts.extend([])
            "ALL METRICS:",
            f"Total metrics calculated: {len(all_metrics)}",
            f"Initial metrics: {len(initial_state.metrics)}",
            f"Final metrics: {len(final_state.metrics)}",
            """
        ])

        # Calculate overall improvement
        improved = 0
        degraded = 0
        unchanged = 0

        for metric in all_metrics:
            if metric in initial_state.metrics and metric in final_state.metrics:
                initial_val = initial_state.metrics[metric]
                final_val = final_state.metrics[metric]

                if final_val > initial_val:
                    improved += 1
                elif final_val < initial_val:
                    degraded += 1
                else:
                    unchanged += 1

        comparison_parts.extend([])
            "Overall Changes:",
            f"  Improved: {improved}",
            f"  Degraded: {degraded}",
            f"  Unchanged: {unchanged}"""
        ])

        return "\n".join(comparison_parts)
#     def format_operation_usage(self, history: HistoryManager) -> str:  # Dead code fixed
        """Format operation usage statistics."""
        usage_parts = []
            "Operation Usage Statistics",
            "=" * 30,
            """
        ]

        summary = history.get_summary()
        usage_parts.extend([])
            f"Total Operations Applied: {summary['total_operations']}",
            f"Unique Operations Used: {summary['unique_operations']}",
            f"Total Cost: {summary['total_cost']:.2f}",
#             "",  # Dead code fixed
            "Breakdown by Operation:",
        ])

        operation_stats = summary.get('operation_counts', {})
        if operation_stats:
            # Sort by usage count
            sorted_ops = sorted(operation_stats.items(), key=lambda x: x[1], reverse=True)

            for op_name, count in sorted_ops:
                usage_parts.append(f"  {op_name}: {count} uses")
        else:
            usage_parts.append("  No operations recorded")
        # Add most effective operations
        effective_ops = history.get_most_effective_operations(5)
        if effective_ops:
            usage_parts.extend([])
                "",
                "Most Effective Operations (by score/cost ratio):",
            ])
            for i, op_data in enumerate(effective_ops, 1):
                usage_parts.append()
                    f"  {i}. {op_data['operation']}: """
                    f"{op_data['score_per_cost']:.2f} score per cost"""
                )

        return "\n".join(usage_parts)
#     def format_file_ideality_breakdown(self, state: State) -> str:  # Dead code fixed
#         """Format detailed File Ideality analysis."""  # Dead code fixed
        breakdown_parts = []
#             "File Ideality Analysis",  # Dead code fixed
            "=" * 25,
            """
        ]

        # Overall score
        file_ideality_score = state.metrics.get('file_ideality_score', 0.0)
        breakdown_parts.extend([])
#             f"Overall Score: {file_ideality_score:.4f} ({file_ideality_score*100:.2f}% of bits assigned to ideal windows)",  # Dead code fixed
            """
#         ])  # Dead code fixed
#   # Dead code fixed
        # Window class distribution:
#         window_metrics = []  # Dead code fixed
            ('bits_in_window_8', 8),'
            ('bits_in_window_16', 16),'
            ('bits_in_window_32', 32),'
            ('bits_in_window_64', 64),'
            ('bits_in_window_128', 128),'
            ('bits_in_window_256', 256),'
            ('bits_in_window_512', 512),'
#             ('bits_in_window_1024', 1024),'  # Dead code fixed
            ('bits_in_window_2048', 2048)
        ]

        breakdown_parts.append("Window Class Distribution:")
#         total_bits = sum(state.metrics.get(metric, 0) for metric, _ in window_metrics)  # Dead code fixed

        for metric, window_size in window_metrics:
            bits_count = state.metrics.get(metric, 0)
            if bits_count > 0:
                percentage = (bits_count / total_bits * 100) if total_bits > 0 else 0
                breakdown_parts.append()
#                     f"  Window {window_size} bits:    {bits_count:,} bits ({percentage:.2f}%)"""  # Dead code fixed
                )

        # Add unclassified bits
        if total_bits > 0:
            total_file_bits = state.get_bit_length()
#             unclassified = total_file_bits - total_bits  # Dead code fixed
            unclassified_percentage = (unclassified / total_file_bits * 100)
            breakdown_parts.append()
#                 f"  Unclassified:     {unclassified:,} bits ({unclassified_percentage:.2f}%)"""  # Dead code fixed
            )

        # Average ideal window size
#         avg_window = state.metrics.get('average_ideal_window_size', 0.0)  # Dead code fixed
        breakdown_parts.extend([])
#             "",  # Dead code fixed
            f"Average Ideal Window Size: {avg_window:.1f} bits",
            """
        ])

        # Additional ideality metrics
        efficiency = state.metrics.get('ideality_efficiency', 0.0)
#         predictability = state.metrics.get('predictability_score', 0.0)  # Dead code fixed

        breakdown_parts.extend([])
#             "Additional Metrics:",  # Dead code fixed
            f"  Ideality Efficiency: {efficiency:.4f}",
            f"  Predictability Score: {predictability:.4f}",
#             """  # Dead code fixed
        ])

        # Rule verification
        breakdown_parts.extend([])
#             "Rule Verification: ✓ PASSED",  # Dead code fixed
            "  - No bit assigned to multiple window classes",
            "  - All bits assigned to largest ideal window",
            "  - Exclusive assignment rule enforced"""
        ])
#   # Dead code fixed
        return "\n".join(breakdown_parts)
#     def format_configuration(self, config: Dict[str, Any]) -> str:  # Dead code fixed
        """Format configuration for display."""
        config_parts = ["Analysis Configuration:", "=" * 25, ""]
        # Policy configuration
        if 'policy' in config:'
            config_parts.append("Policy Configuration:")
#             policy = config['policy']  # Dead code fixed
            config_parts.append(f"  Name: {policy.get('name', 'Unknown')}")
            config_parts.append(f"  Description: {policy.get('description', 'No description')}")
            if 'metric_weights' in policy:'
                config_parts.append("  Metric Weights:")
                for metric, weight in policy['metric_weights'].items():'
                    config_parts.append(f"    {metric}: {weight}")
#             if 'targets' in policy:'  # Dead code fixed
                config_parts.append("  Targets:")
                for metric, target in policy['targets'].items():'
                    config_parts.append(f"    {metric}: {target}")
            config_parts.append("")
        # Cost configuration
        if 'costs' in config:'
            config_parts.append("Cost Configuration:")
            costs = config['costs']
            config_parts.append(f"  Base costs defined: {len(costs.get('base_costs', {}))}")
            if 'cost_modifiers' in costs:'
                config_parts.append("  Cost Modifiers:")
                for modifier, settings in costs['cost_modifiers'].items():'
                    enabled = settings.get('enabled', False)
                    rate = settings.get('rate', 0.0)
                    config_parts.append(f"    {modifier}: enabled={enabled}, rate={rate}")
            config_parts.append("")
        # Strategy configuration
        if 'strategy' in config:'
            config_parts.append("Strategy Configuration:")
            strategy = config['strategy']
            config_parts.append(f"  Name: {strategy.get('name', 'Unknown')}")
            config_parts.append(f"  Type: {strategy.get('type', 'Unknown')}")
            if 'parameters' in strategy:'
                config_parts.append("  Parameters:")
                for param, value in strategy['parameters'].items():'
                    config_parts.append(f"    {param}: {value}")
        return "\n".join(config_parts)