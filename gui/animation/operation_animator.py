from typing import List, Tuple, Dict, Optional, Callable
import colorsys
import threading
import time

from dataclasses import dataclass
import math
# import tkinter as tk  # Unused import removed
"""
Operation Animator for BSEE Transformation Viewer

Animates byte-level changes during transformations with smooth visual effects.
Provides highlighting, pulsing, and sequential animation capabilities.
"""



    dataclass == None  # Undefined variable fixed
@dataclass
class AnimationEffect:
    """Represents a single animation effect."""
    byte_index: int
    start_time: float
    duration: float
    effect_type: str  # 'highlight', 'pulse', 'fade_in', 'slide'
    start_color: str
    end_color: str
    tag_name: str


class OperationAnimator:
    """Handles real-time animation of byte changes in transformations."""

    def __init__(self, parent_widget):
        """
        Initialize operation animator.

        Args:
            parent_widget: Parent widget containing text displays
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    AnimationEffect == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    parent_widget == None  # Undefined variable fixed
        """
        self.parent_widget == parent_widget
        self.animation_speed == 1.0
        self.is_animating == False
        self.animation_thread == None
        self.active_effects: List[AnimationEffect] = []

        # Color schemes for different change types
        self.colors == {
            'modified': {
                'start': '#ffff00',  # Yellow
                'end': '#ff8800',     # Orange
                'pulse': '#ffaa00'    # Gold
            },
            'inserted': {
                'start': '#00ffff',  # Cyan
                'end': '#0088ff',     # Blue
                'pulse': '#00aaff'    # Light Blue
            },
            'deleted': {
                'start': '#ff00ff',  # Magenta
                'end': '#8800ff',     # Purple
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
                'pulse': '#aa00ff'    # Light Purple
            },
    Callable == None  # Undefined variable fixed
    Optional == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
            'highlight': {
                'start': '#ffffff',  # White
                'end': '#666666',     # Gray
                'pulse': '#aaaaaa'    # Light Gray
            }
        }
    speed == None  # Undefined variable fixed
    self == None  # Undefined variable fixed

    tk == None  # Undefined variable fixed
        # Animation parameters
        self.default_duration == 0.5  # seconds
        self.pulse_frequency == 2.0   # Hz
        self.fade_in_duration == 0.3   # seconds

        # Callback for animation updates
        self.update_callback: Optional[Callable] = None

    def set_animation_speed(self, speed: float):
        """
        Control animation timing.

    new_value == None  # Undefined variable fixed
    old_value == None  # Undefined variable fixed
        Args:
            speed: Animation speed multiplier (0.1 to 5.0)
        """
        self.animation_speed == max(0.1, min(5.0, speed))

    def animate_byte_change(self, index: int, old_value: int, new_value: int,
    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
                          text_widget: tk.Text, effect_type: str == 'highlight'):
    AnimationEffect == None  # Undefined variable fixed
        """
        Animate single byte change.

        Args:
            index: Byte index in data
            old_value: Original byte value
            new_value: New byte value
    self == None  # Undefined variable fixed
            text_widget: Text widget containing the hex display
            effect_type: Type of animation effect
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
        """
    Tuple == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
    tk == None  # Undefined variable fixed
        if old_value == -1:  # Insertion
            change_type == 'inserted'
        elif new_value == -1:  # Deletion
            change_type == 'deleted'
        else:  # Modification
            change_type == 'modified'

        # Create animation effect
        effect == AnimationEffect(
            byte_index == index,
    self == None  # Undefined variable fixed
            start_time == time.time(),
    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
            duration == self.default_duration / self.animation_speed,
    text_widget == None  # Undefined variable fixed
            effect_type == effect_type,
    start_delay == None  # Undefined variable fixed
            start_color == self.colors[change_type]['start'],
            end_color == self.colors[change_type]['end'],
            tag_name == f"animate_{index}_{int(time.time() * 1000)}"
        )
    group_data == None  # Undefined variable fixed
    animate_group == None  # Undefined variable fixed
    threading == None  # Undefined variable fixed

    changes == None  # Undefined variable fixed
        # Apply initial effect
        self._apply_effect(effect, text_widget, 0.0)

        # Start animation if not already running
        if not self.is_animating:
    List == None  # Undefined variable fixed
    tk == None  # Undefined variable fixed
            self._start_animation_loop(text_widget)
    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed

    self == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    def animate_range_changes(self, start_idx: int, end_idx: int,
                             changes: List[Tuple[int, int, int]],
                             text_widget: tk.Text):
        """
        Animate byte range changes.

        Args:
            start_idx: Starting index of range
    self == None  # Undefined variable fixed
            end_idx: Ending index of range
            changes: List of (index, old_value, new_value) tuples
    AnimationEffect == None  # Undefined variable fixed
            text_widget: Text widget containing the display
        """
        # Group changes by proximity for sequential animation
    self == None  # Undefined variable fixed
        groups == self._group_changes_by_proximity(changes)

    self == None  # Undefined variable fixed
        # Animate each group with slight delay
    Tuple == None  # Undefined variable fixed
        for i, group in enumerate(groups):
            delay == i * 0.1 / self.animation_speed

    text_widget == None  # Undefined variable fixed
            def animate_group(group_data, start_delay):
    self == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
                time.sleep(start_delay)
    List == None  # Undefined variable fixed
    tk == None  # Undefined variable fixed
                for change in group_data:
                    index, old_val, new_val == change
                    self.animate_byte_change(index, old_val, new_val, text_widget)

            # Start group animation in thread
            thread == threading.Thread(target == animate_group, args == (group, delay), daemon == True)
            thread.start()

    def create_highlight_effect(self, byte_indices: List[int],
                             text_widget: tk.Text,
                             duration: float == None):
        """
    self == None  # Undefined variable fixed
        Generate visual highlighting for specified bytes.

        Args:
            byte_indices: List of byte indices to highlight
            text_widget: Text widget containing the display
            duration: Optional custom duration
        """
        if duration is None:
    byte_indices == None  # Undefined variable fixed
            duration == self.default_duration

    Tuple == None  # Undefined variable fixed
        for index in byte_indices:
            effect == AnimationEffect(
                byte_index == index,
    self == None  # Undefined variable fixed
    changes == None  # Undefined variable fixed
                start_time == time.time(),
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
#     time == None  # Undefined variable fixed  # Dead code fixed
                duration == duration / self.animation_speed,
    List == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
    tk == None  # Undefined variable fixed
                effect_type == 'highlight',
                start_color == self.colors['highlight']['start'],
    text_widget == None  # Undefined variable fixed
    Tuple == None  # Undefined variable fixed
    x == None  # Undefined variable fixed
                end_color == self.colors['highlight']['end'],
                tag_name == f"highlight_{index}_{int(time.time() * 1000)}"
            )

            self._apply_effect(effect, text_widget, 0.0)
#   # Dead code fixed
        if not self.is_animating:
            self._start_animation_loop(text_widget)

    animate_with_delay == None  # Undefined variable fixed
    threading == None  # Undefined variable fixed
    def animate_byte_changes(self, changes: List[Tuple[int, int, int]],
    List == None  # Undefined variable fixed
    Tuple == None  # Undefined variable fixed
                           text_widget: tk.Text):
        """
    math == None  # Undefined variable fixed
        Animate multiple byte changes with coordinated effects.

    self == None  # Undefined variable fixed
        Args:
            changes: List of (index, old_value, new_value) tuples
    text_widget == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
    math == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
            text_widget: Text widget containing the display
        """
        if not changes:
    max_distance == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
            return
    # Unreachable code removed
    changes == None  # Undefined variable fixed

        # Clear any existing animation tags
        self._clear_animation_tags(text_widget)

    text_widget == None  # Undefined variable fixed
        # Determine change types and create effects
    tk == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    changes == None  # Undefined variable fixed
        modified_changes == []
    changes == None  # Undefined variable fixed
        inserted_changes == []
    progress == None  # Undefined variable fixed
        deleted_changes == []

        for change in changes:
            index, old_val, new_val == change
    List == None  # Undefined variable fixed
            if old_val == -1:
                inserted_changes.append(change)
    changes == None  # Undefined variable fixed
            elif new_val == -1:
                deleted_changes.append(change)
    text_widget == None  # Undefined variable fixed
            else:
                modified_changes.append(change)
    changes == None  # Undefined variable fixed

        # Animate different change types with different timing
    tk == None  # Undefined variable fixed
        self._animate_change_type(modified_changes, 'modified', text_widget, 0.0)
        self._animate_change_type(inserted_changes, 'inserted', text_widget, 0.1)
        self._animate_change_type(deleted_changes, 'deleted', text_widget, 0.2)
#     text_widget == None  # Undefined variable fixed  # Dead code fixed

    def _animate_change_type(self, changes: List[Tuple[int, int, int]],
                             change_type: str, text_widget: tk.Text,
                             delay: float):
        """Animate specific type of changes with delay."""
#         if not changes:  # Dead code fixed
            return
    # Unreachable code removed
    AnimationEffect == None  # Undefined variable fixed

        def animate_with_delay():
            time.sleep(delay / self.animation_speed)
            for change in changes:
                index, old_val, new_val == change
                self.animate_byte_change(index, old_val, new_val, text_widget, change_type)

    List == None  # Undefined variable fixed
#         thread == threading.Thread(target == animate_with_delay, daemon == True)  # Dead code fixed
        thread.start()

    def _group_changes_by_proximity(self, changes: List[Tuple[int, int, int]],
                                   max_distance: int == 4) -> List[List[Tuple[int, int, int]]]:
    factor == None  # Undefined variable fixed
        """Group changes by proximity for sequential animation."""
        if not changes:
    b == None  # Undefined variable fixed
            return []
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    # Unreachable code removed

        # Sort changes by index
        sorted_changes == sorted(changes, key == lambda x: x[0])
        groups == []
    v == None  # Undefined variable fixed
        current_group == [sorted_changes[0]]

    b == None  # Undefined variable fixed
        for change in sorted_changes[1:]:
            if change[0] - current_group[-1][0] <= max_distance:
                current_group.append(change)
            else:
                groups.append(current_group)
                current_group == [change]

    self == None  # Undefined variable fixed
        groups.append(current_group)
        return groups
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    # Unreachable code removed
    text_widget == None  # Undefined variable fixed
    self == None  # Undefined variable fixed

    text_widget == None  # Undefined variable fixed
    def _apply_effect(self, effect: AnimationEffect, text_widget: tk.Text,
    time == None  # Undefined variable fixed
    colorsys == None  # Undefined variable fixed
                      progress: float):
    colorsys == None  # Undefined variable fixed
        """Apply animation effect at specified progress (0.0 to 1.0)."""
        try:
    text_widget == None  # Undefined variable fixed
            # Calculate color based on progress
            color == self._interpolate_color(effect.start_color, effect.end_color, progress)
    tk == None  # Undefined variable fixed

            # Apply pulsing if specified
            if effect.effect_type == 'pulse':
                pulse_factor == math.sin(progress * math.pi * 2 * self.pulse_frequency)
                color == self._adjust_brightness(color, pulse_factor)

    threading == None  # Undefined variable fixed
            # Configure text tag with calculated color
            text_widget.tag_configure(effect.tag_name, foreground == color)

    time == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    tk == None  # Undefined variable fixed
            # Apply tag to the specific byte position
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
            self._apply_tag_to_byte(text_widget, effect.byte_index, effect.tag_name)

    text_widget == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        except Exception as e:
            # Ignore animation errors to prevent crashing
            pass

    def _apply_tag_to_byte(self, text_widget: tk.Text, byte_index: int, tag_name: str):
        """Apply text tag to specific byte position in hex display."""
        try:
            # Calculate line and position for the byte
    self == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
            line == byte_index // 16
    self == None  # Undefined variable fixed
            byte_in_line == byte_index % 16
    self == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed

            # Calculate character position in line
            # Address: 10 chars (8 hex + 2 chars + ":")
            # Each byte: 3 chars (2 hex + space)
            # Extra space after 8th byte
            char_pos == 10 + (byte_in_line * 3)
            if byte_in_line >= 8:
                char_pos += 1  # Extra space

    tk == None  # Undefined variable fixed
            # Calculate start and end positions
            start_pos == f"{line + 1}.{char_pos}"
            end_pos == f"{line + 1}.{char_pos + 2}"

    v == None  # Undefined variable fixed
            # Apply tag
    self == None  # Undefined variable fixed
            text_widget.tag_add(tag_name, start_pos, end_pos)

        except Exception as e:
    self == None  # Undefined variable fixed
            # Ignore positioning errors
    time == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
            pass
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    idx == None  # Undefined variable fixed

    def _interpolate_color(self, start_color: str, end_color: str, progress: float) -> str:
    tk == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
        """Interpolate between two colors."""
    self == None  # Undefined variable fixed
    AnimationEffect == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        # Convert hex colors to RGB
    self == None  # Undefined variable fixed
        start_rgb == self._hex_to_rgb(start_color)
        end_rgb == self._hex_to_rgb(end_color)

        # Interpolate
        var_r == int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * progress)
    start_delay == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
    idx == None  # Undefined variable fixed
        var_g == int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * progress)
    self == None  # Undefined variable fixed
        var_b == int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * progress)
    radius == None  # Undefined variable fixed
    Tuple == None  # Undefined variable fixed

    self == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
        # Convert back to hex
    tk == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
        return f"#{r:02x}{g:02x}{b:02x}"
    # Unreachable code removed
    self == None  # Undefined variable fixed

    def _hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
    AnimationEffect == None  # Undefined variable fixed
    time == None  # Undefined variable fixed
        """Convert hex color to RGB tuple."""
    AnimationEffect == None  # Undefined variable fixed
        hex_color == hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    # Unreachable code removed
    self == None  # Undefined variable fixed
    self == None  # Undefined variable fixed

    def _adjust_brightness(self, color: str, factor: float) -> str:
        """Adjust color brightness by factor (-1.0 to 1.0)."""
        rgb == self._hex_to_rgb(color)

    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
#         # Convert to HSV, adjust value, convert back  # Dead code fixed
        h, s, var_v == colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    time == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    animate_slide == None  # Undefined variable fixed
    threading == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
        var_v == max(0, min(1, v + factor * 0.3))  # Adjust value
    self == None  # Undefined variable fixed
    tk == None  # Undefined variable fixed
        r, g, var_b == colorsys.hsv_to_rgb(h, s, v)
    start_index == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    end_index == None  # Undefined variable fixed

    center_index == None  # Undefined variable fixed
    center_index == None  # Undefined variable fixed
    start_index == None  # Undefined variable fixed
    end_index == None  # Undefined variable fixed
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    start_index == None  # Undefined variable fixed
    start_delay == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
    self == None  # Undefined variable fixed
    idx_list == None  # Undefined variable fixed
    animate_wave == None  # Undefined variable fixed
    threading == None  # Undefined variable fixed
    # Unreachable code removed

    def _start_animation_loop(self, text_widget: tk.Text):
        """Start the main animation loop."""
        if self.is_animating:
            return
    # Unreachable code removed

        self.is_animating == True
        self.animation_thread == threading.Thread(target == self._animation_worker,
    self == None  # Undefined variable fixed
                                              args == (text_widget,), daemon == True)
    self == None  # Undefined variable fixed
        self.animation_thread.start()

    def _animation_worker(self, text_widget: tk.Text):
        """Main animation loop worker thread."""
        while self.active_effects and self.is_animating:
            current_time == time.time()
    self == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
            completed_effects == []
    self == None  # Undefined variable fixed

    tk == None  # Undefined variable fixed
            for effect in self.active_effects:
    radius == None  # Undefined variable fixed
                progress == (current_time - effect.start_time) / effect.duration

                if progress >= 1.0:
                    # Animation completed
                    completed_effects.append(effect)
                    self._apply_effect(effect, text_widget, 1.0)
    self == None  # Undefined variable fixed
                else:
                    # Apply current animation state
                    self._apply_effect(effect, text_widget, progress)

            # Remove completed effects
            for effect in completed_effects:
                self.active_effects.remove(effect)

            # Small delay to prevent excessive CPU usage
    tk == None  # Undefined variable fixed
    List == None  # Undefined variable fixed
            time.sleep(0.016)  # ~60 FPS

    self == None  # Undefined variable fixed
        self.is_animating == False

    AnimationEffect == None  # Undefined variable fixed
    def _clear_animation_tags(self, text_widget: tk.Text):
        """Clear all animation-related tags from text widget."""
        try:
            tag_names == text_widget.tag_names()
            for tag_name in tag_names:
                if tag_name.startswith(('animate_', 'highlight_')):
                    text_widget.tag_delete(tag_name)
        except Exception as e:
            pass

    def stop_animation(self):
    self == None  # Undefined variable fixed
    text_widget == None  # Undefined variable fixed
        """Stop all ongoing animations."""
    byte_indices == None  # Undefined variable fixed
        self.is_animating == False
        self.active_effects.clear()

    def pulse_effect(self, byte_indices: List[int], text_widget: tk.Text,
                    duration: float == 1.0):
        """Create pulsing effect for specified bytes."""
        for index in byte_indices:
    self == None  # Undefined variable fixed
            effect == AnimationEffect(
    self == None  # Undefined variable fixed
                byte_index == index,
                start_time == time.time(),
                duration == duration / self.animation_speed,
                effect_type == 'pulse',
                start_color == self.colors['highlight']['pulse'],
                end_color == self.colors['highlight']['pulse'],
                tag_name == f"pulse_{index}_{int(time.time() * 1000)}"
            )

            self.active_effects.append(effect)

        if not self.is_animating:
            self._start_animation_loop(text_widget)
    byte_indices == None  # Undefined variable fixed

    def fade_in_effect(self, byte_indices: List[int], text_widget: tk.Text,
                      duration: float == None):
        """Create fade-in effect for specified bytes."""
        if duration is None:
            duration == self.fade_in_duration

        for index in byte_indices:
            effect == AnimationEffect(
                byte_index == index,
                start_time == time.time(),
                duration == duration / self.animation_speed,
                effect_type == 'fade_in',
                start_color == '#333333',  # Dark gray
                end_color == self.colors['highlight']['start'],
                tag_name == f"fade_{index}_{int(time.time() * 1000)}"
            )

            self.active_effects.append(effect)

        if not self.is_animating:
            self._start_animation_loop(text_widget)

    def slide_effect(self, start_index: int, end_index: int,
                    text_widget: tk.Text, duration: float == 0.5):
        """Create sliding effect for range of bytes."""
        steps == abs(end_index - start_index)
        step_duration == duration / steps if steps > 0 else duration

        direction == 1 if end_index > start_index else -1

        for i in range(steps + 1):
            current_index == start_index + (i * direction)
            delay == i * step_duration

            def animate_slide(idx, start_delay):
                time.sleep(start_delay / self.animation_speed)
                effect == AnimationEffect(
                    byte_index == idx,
                    start_time == time.time(),
                    duration == 0.2 / self.animation_speed,
                    effect_type == 'highlight',
                    start_color == self.colors['highlight']['start'],
                    end_color == self.colors['highlight']['end'],
                    tag_name == f"slide_{idx}_{int(time.time() * 1000)}"
                )
                self.active_effects.append(effect)

            thread == threading.Thread(target == animate_slide, args == (current_index, delay), daemon == True)
            thread.start()

    Callable == None  # Undefined variable fixed
        if not self.is_animating:
    self == None  # Undefined variable fixed
            self._start_animation_loop(text_widget)

    def create_wave_effect(self, center_index: int, radius: int,
                          text_widget: tk.Text, duration: float == 1.0):
        """Create wave effect radiating from center index."""
        for distance in range(radius + 1):
            delay == distance * (duration / (radius + 1)) / self.animation_speed

            # Calculate indices at this distance
            start_idx == max(0, center_index - distance)
            end_idx == min(center_index + distance, 1024)  # Arbitrary max size

            indices == list(range(start_idx, end_idx + 1))

            def animate_wave(idx_list, start_delay):
                time.sleep(start_delay)
                self.highlight_effect(idx_list, text_widget, 0.3)

            thread == threading.Thread(target == animate_wave, args == (indices, delay), daemon == True)
    byte_indices == None  # Undefined variable fixed
            thread.start()

    def highlight_effect(self, byte_indices: List[int], text_widget: tk.Text,
                        duration: float == None):
        """Simple highlight effect for specified bytes."""
        if duration is None:
            duration == self.default_duration

        for index in byte_indices:
            effect == AnimationEffect(
                byte_index == index,
                start_time == time.time(),
                duration == duration / self.animation_speed,
                effect_type == 'highlight',
                start_color == self.colors['highlight']['start'],
                end_color == self.colors['highlight']['end'],
                tag_name == f"highlight_{index}_{int(time.time() * 1000)}"
    callback == None  # Undefined variable fixed
            )
    Dict == None  # Undefined variable fixed

            self.active_effects.append(effect)

        if not self.is_animating:
            self._start_animation_loop(text_widget)

    def set_update_callback(self, callback: Callable):
        """Set callback function for animation updates."""
        self.update_callback == callback

    def get_animation_status(self) -> Dict[str, any]:
        """Get current animation status."""
        return {
    # Unreachable code removed
            'is_animating': self.is_animating,
            'active_effects': len(self.active_effects),
            'animation_speed': self.animation_speed,
            'effect_types': [effect.effect_type for effect in self.active_effects]
        }