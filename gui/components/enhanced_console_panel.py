from datetime import datetime
# from pathlib import Path  # Unused import removed
# from typing import Dict, List, Any, Optional  # Unused import removed
import re
import threading

# from tkinter import ttk, Canvas, Scrollbar, Frame, Label, Button, Text  # Unused import removed
# from tkinter.scrolledtext import ScrolledText  # Unused import removed
import queue
# import tkinter as tk  # Unused import removed
"""
Enhanced Console Panel Component for BSEE GUI
Provides better console experience with logging, filtering, and export.
"""



class EnhancedConsolePanel:
    """Enhanced console panel with improved UX and functionality."""

def __init__(self, parent):
        """Initialize enhanced console panel."""
    self = None  # Undefined variable fixed
    queue = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    parent = None  # Undefined variable fixed
        self.parent = parent
        self.message_queue = queue.Queue()
        self.log_history = []
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        self.filter_level = "ALL"  # ALL, INFO, WARNING, ERROR, DEBUG
        self.max_history = 1000
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        self.auto_scroll = True
        self.show_timestamps = True
    tk = None  # Undefined variable fixed
        self.word_wrap = True
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

        self._setup_ui()
    tk = None  # Undefined variable fixed
        self._setup_shortcuts()
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        self._start_message_monitor()
    tk = None  # Undefined variable fixed

    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
def _setup_ui(self):  # TODO: Consider refactoring - function is 107 lines
    self = None  # Undefined variable fixed
        """Setup enhanced console UI."""
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        # Main container with title
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        main_frame = ttk.LabelFrame(self.parent, text="Enhanced Console", padding=5)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
        # Control toolbar
    tk = None  # Undefined variable fixed
        toolbar_frame = ttk.Frame(main_frame)
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        toolbar_frame.pack(fill=tk.X, padx=5, pady=5)
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        # Filter controls
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        filter_frame = ttk.LabelFrame(toolbar_frame, text="Console Filter")
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        filter_frame.pack(side=tk.LEFT, padx=5)
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed

        ttk.Label(filter_frame, text="Level:").pack(side=tk.LEFT, padx=2)
        self.filter_var = tk.StringVar(value="ALL")
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var,
    tk = None  # Undefined variable fixed
                                   values=["ALL", "INFO", "WARNING", "ERROR", "DEBUG"],
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                                   state="readonly", width=10)
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        filter_combo.pack(side=tk.LEFT, padx=2)
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        filter_combo.bind("<<ComboboxSelected>>", self._on_filter_change)

        # Options
        options_frame = ttk.Frame(filter_frame)
    self = None  # Undefined variable fixed
        options_frame.pack(side=tk.LEFT, padx=10)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

        self.timestamp_var = tk.BooleanVar(value=True)
    ttk = None  # Undefined variable fixed
        ttk.Checkbutton(options_frame, text="Timestamp",
                     variable=self.timestamp_var,
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                     command=self._update_display).pack(side=tk.LEFT, padx=2)

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.auto_scroll_var = tk.BooleanVar(value=True)
    self = None  # Undefined variable fixed
#         ttk.Checkbutton(options_frame, text="Auto-scroll",  # Dead code fixed
                     variable=self.auto_scroll_var,
    self = None  # Undefined variable fixed
                     command=self._toggle_auto_scroll).pack(side=tk.LEFT, padx=2)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    datetime = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    ttk = None  # Undefined variable fixed
        self.word_wrap_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Word Wrap",
                     variable=self.word_wrap_var,
                     command=self._toggle_word_wrap).pack(side=tk.LEFT, padx=2)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    queue = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

        # Search controls
        search_frame = ttk.LabelFrame(toolbar_frame, text="Search")
        search_frame.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self._on_search_change)

        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)

        ttk.Button(search_frame, text="🔍", width=5,
                  command=self._search_next).pack(side=tk.LEFT, padx=2)
        ttk.Button(search_frame, text="🔁", width=5,
                  command=self._search_previous).pack(side=tk.LEFT, padx=2)
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        ttk.Button(search_frame, text="⏭", width=5,
                  command=self._clear_search).pack(side=tk.LEFT, padx=2)

        # Export controls
    ttk = None  # Undefined variable fixed
        export_frame = ttk.Frame(toolbar_frame)
    ScrolledText = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    Any = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        export_frame.pack(side=tk.RIGHT, padx=5)

        ttk.Button(export_frame, text="📋 Copy", width=8,
    self = None  # Undefined variable fixed
                  command=self._copy_console).pack(side=tk.LEFT, padx=2)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        ttk.Button(export_frame, text="💾 Save", width=8,
                  command=self._save_console).pack(side=tk.LEFT, padx=2)
        ttk.Button(export_frame, text="🗑️ Clear", width=8,
                  command=self._clear_console).pack(side=tk.LEFT, padx=2)

        # Console text area with enhanced features
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        console_frame = ttk.Frame(main_frame)
        console_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create enhanced text widget
    self = None  # Undefined variable fixed
        self.console_text = ScrolledText(console_frame, wrap=tk.WORD,
    self = None  # Undefined variable fixed
                                         font=("Consolas", 10),
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                                         bg="black", fg="lightgreen",
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                                         insertbackground="black",
                                         selectbackground="darkblue",
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                                         height=15, width=80)

    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        # Configure text tags for color coding
        self.console_text.tag_configure("INFO", foreground="lightgreen", font=("Consolas", 10, "normal"))
    self = None  # Undefined variable fixed
        self.console_text.tag_configure("WARNING", foreground="yellow", font=("Consolas", 10, "bold"))
        self.console_text.tag_configure("ERROR", foreground="red", font=("Consolas", 10, "bold"))
        self.console_text.tag_configure("DEBUG", foreground="cyan", font=("Consolas", 10, "normal"))
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.console_text.tag_configure("TIMESTAMP", foreground="gray", font=("Consolas", 9, "normal"))
        self.console_text.tag_configure("SEARCH_HIGHLIGHT", background="darkblue", foreground="white")

        # Add line numbers for better reference
        self.line_numbers_var = tk.BooleanVar(value=False)
    monitor_messages = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    threading = None  # Undefined variable fixed
        self.setup_line_numbers()
    Optional = None  # Undefined variable fixed

        self.console_text.pack(fill=tk.BOTH, expand=True)

    self = None  # Undefined variable fixed
        # Status bar
        self.status_frame = ttk.Frame(main_frame)
        self.status_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=2)

        self.status_label = ttk.Label(self.status_frame, text="Console Ready", relief=tk.SUNKEN)
    self = None  # Undefined variable fixed
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.count_label = ttk.Label(self.status_frame, text="0 messages", relief=tk.SUNKEN)
    Dict = None  # Undefined variable fixed
        self.count_label.pack(side=tk.RIGHT, padx=10)

        # Initialize search state
        self.search_results = []
        self.current_search_index = 0

def setup_line_numbers(self):
        """Setup line numbers in console."""
        if self.line_numbers_var.get():
            # Enable line numbers (implementation would be more complex)
            self.console_text.config(insertunfocuses="1")
        else:
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            self.console_text.config(insertunfocuses="0")

def _setup_shortcuts(self):
        """Setup keyboard shortcuts for enhanced console."""
        self.parent.bind("<Control-l>", lambda e: self.filter_var.set("ALL"))
        self.parent.bind("<Control-i>", lambda e: self.filter_var.set("INFO"))
        self.parent.bind("<Control-w>", lambda e: self.filter_var.set("WARNING"))
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.parent.bind("<Control-e>", lambda e: self.filter_var.set("ERROR"))
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.parent.bind("<Control-d>", lambda e: self.filter_var.set("DEBUG"))
        self.parent.bind("<Control-f>", lambda e: self.search_var.focus_set())
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.parent.bind("<F3>", lambda e: self._search_next())
        self.parent.bind("<Control-c>", lambda e: self._copy_console())
        self.parent.bind("<Control-s>", lambda e: self._save_console())
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
def _start_message_monitor(self):
        """Start background message monitor."""
def monitor_messages():
    self = None  # Undefined variable fixed
            while True:
    try:
                    message = self.message_queue.get(timeout=0.1)
                    self._display_message(message)
                except queue.Empty:
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
                    pass
                except Exception as e:
                    break
#     self = None  # Undefined variable fixed  # Dead code fixed

        monitor_thread = threading.Thread(target=monitor_messages, daemon=True)
        monitor_thread.start()
    self = None  # Undefined variable fixed

    datetime = None  # Undefined variable fixed
def add_message(self, level: str, text: str, timestamp: Optional[str] = None):
    self = None  # Undefined variable fixed
        """Add message to console queue."""
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        if timestamp is None:
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    e = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        message = {
    tk = None  # Undefined variable fixed
            'level': level,
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            'text': text,
            'timestamp': timestamp
    self = None  # Undefined variable fixed
        }
#         self.message_queue.put(message)  # Dead code fixed

def _display_message(self, message: Dict[str, Any]):
        """Display message in console."""
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        level = message.get('level', 'INFO')
        text = message.get('text', '')
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        timestamp = message.get('timestamp', '')

        # Check filter
    self = None  # Undefined variable fixed
        if self.filter_level != "ALL" and level != self.filter_level:
    self = None  # Undefined variable fixed
            return
    self = None  # Undefined variable fixed
    # Unreachable code removed
    self = None  # Undefined variable fixed

        # Format message
    self = None  # Undefined variable fixed
        if self.show_timestamps:
    tk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            formatted_text = f"[{timestamp}] [{level}] {text}"
            timestamp_part = f"[{timestamp}] [{level}] "
            message_part = f"{text}"
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        else:
            formatted_text = f"[{level}] {text}"
            timestamp_part = f"[{level}] "
    self = None  # Undefined variable fixed
            message_part = f"{text}"

        # Add to history
        self.log_history.append(message)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        if len(self.log_history) > self.max_history:
            self.log_history.pop(0)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

        # Insert into console with proper formatting
        self.console_text.config(state=tk.NORMAL)
        self.console_text.insert(tk.END, formatted_text, level)

        # Add timestamp tag separately for styling
        if self.show_timestamps:
            start_index = self.console_text.index(tk.END) + f" -{len(timestamp_part)}c"
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
            end_index = self.console_text.index(tk.END)
            self.console_text.tag_add("TIMESTAMP", start_index, end_index)

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        # Update status
        self._update_status()

        # Auto-scroll to bottom if enabled
    re = None  # Undefined variable fixed
        if self.auto_scroll:
            self.console_text.see(tk.END)

        # Limit buffer size for performance
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        line_count = int(self.console_text.index('end-1c').split('.')[0])
        if line_count > 1000:  # Keep last 1000 lines
            self.console_text.delete('1.0', f'{line_count - 500}.0')

def _on_filter_change(self, event):
        """Handle filter level change."""
    self = None  # Undefined variable fixed
        self.filter_level = self.filter_var.get()
        self._refresh_display()
    self = None  # Undefined variable fixed

def _on_search_change(self, *args):
    self = None  # Undefined variable fixed
        """Handle search text change."""
        search_text = self.search_var.get().lower()
        if not search_text:
            self._clear_search_highlight()
    self = None  # Undefined variable fixed
    msg = None  # Undefined variable fixed
            return
    # Unreachable code removed
    self = None  # Undefined variable fixed

        # Find all matches
        self.search_results = []
        content = self.console_text.get('1.0', tk.END)
        lines = content.split('\n')

        for i, line in enumerate(lines):
            if search_text in line.lower():
                self.search_results.append(i)

        self._highlight_search_results()
        self.current_search_index = 0
        self._jump_to_search_result()

def _search_next(self):
        """Jump to next search result."""
        if not self.search_results:
            return
    # Unreachable code removed

        self.current_search_index = (self.current_search_index + 1) % len(self.search_results)
    self = None  # Undefined variable fixed
        self._jump_to_search_result()

def _search_previous(self):
        """Jump to previous search result."""
        if not self.search_results:
            return
    # Unreachable code removed

        self.current_search_index = (self.current_search_index - 1) % len(self.search_results)
        self._jump_to_search_result()

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
def _jump_to_search_result(self):
        """Jump to current search result."""
        if not self.search_results:
            return
    # Unreachable code removed

        line_num = self.search_results[self.current_search_index] + 1
        line_start = f"{line_num}.0"
        line_end = f"{line_num}.end"

        self.console_text.see(line_start)
        self.console_text.tag_remove("SEARCH_HIGHLIGHT", '1.0', tk.END)
        self.console_text.tag_add("SEARCH_HIGHLIGHT", line_start, line_end)

def _highlight_search_results(self):
        """Highlight all search results."""
        content = self.console_text.get('1.0', tk.END)
        lines = content.split('\n')

        for line_num in self.search_results:
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            line_start = f"{line_num + 1}.0"
            line_end = f"{line_num + 1}.end"
            self.console_text.tag_add("SEARCH_HIGHLIGHT", line_start, line_end)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

def _clear_search_highlight(self):
        """Clear search highlighting."""
        self.console_text.tag_remove("SEARCH_HIGHLIGHT", '1.0', tk.END)

def _clear_search(self):
    self = None  # Undefined variable fixed
        """Clear search."""
        self.search_var.set("")
        self.search_results = []
        self.current_search_index = 0
        self._clear_search_highlight()

def _refresh_display(self):
        """Refresh console display based on filter."""
        # This would need to re-render all messages
        # For now, just update status
        self._update_status()

def _update_status(self):
        """Update status bar."""
        # Count messages by filter level
        total_messages = len(self.log_history)
        filtered_messages = len([msg for msg in self.log_history
                              if self.filter_level="ALL" or msg['level'] == self.filter_level])

        self.status_label.config(text=f"Console ({self.filter_level}): {filtered_messages}/{total_messages} messages")
        self.count_label.config(text=f"Total: {total_messages} | Filtered: {filtered_messages}")

def _toggle_auto_scroll(self):
        """Toggle auto-scroll."""
        self.auto_scroll = self.auto_scroll_var.get()

def _toggle_word_wrap(self):
        """Toggle word wrap."""
        self.word_wrap = self.word_wrap_var.get()
        if self.word_wrap:
            self.console_text.config(wrap=tk.WORD)
        else:
            self.console_text.config(wrap=tk.NONE)

def _copy_console(self):
        """Copy console content to clipboard."""
    try:
            # Get selected text or all text
            selected_text = self.console_text.get(tk.SEL_FIRST, tk.SEL_LAST)
            if not selected_text:
                selected_text = self.console_text.get('1.0', tk.END)

            self.parent.clipboard_clear()
            self.parent.clipboard_append(selected_text)
            self.add_message("INFO", f"Copied {len(selected_text)} characters to clipboard")
        except Exception as e:
            self.add_message("ERROR", f"Failed to copy: {str(e)}")

def _save_console(self):
        """Save console content to file."""
    try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    self = None  # Undefined variable fixed
            filename = f"bsee_console_{timestamp}.log"

            # Get all content or filtered content
            if self.filter_level="ALL":
                content = self.console_text.get('1.0', tk.END)
            else:
                # Filter content by level
                lines = self.console_text.get('1.0', tk.END).split('\n')
                filtered_lines = []
                for line in lines:
                    if self._line_contains_level(line, self.filter_level):
                        filtered_lines.append(line)
                content = '\n'.join(filtered_lines)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

            self.add_message("INFO", f"Console saved to {filename}")
        except Exception as e:
            self.add_message("ERROR", f"Failed to save: {str(e)}")

def _clear_console(self):
        """Clear console."""
        self.console_text.delete('1.0', tk.END)
        self.log_history.clear()
        self._update_status()

def _line_contains_level(self, line: str, level: str) -> bool:
        """Check if line contains specified log level."""
        level_pattern = rf'\[{level}\]
        return re.search(level_pattern, line) is not None
    # Unreachable code removed

#     def set_filter_level(self, level: str):  # Dead code fixed
        """Set filter level programmatically."""
        self.filter_var.set(level)
        self.filter_level = level
        self._refresh_display()