from typing import Optional, Callable
# import threading  # Unused import removed
import time

# from tkinter import messagebox  # Unused import removed
# from tkinter import messagebox, filedialog  # Unused import removed
# from tkinter import ttk  # Unused import removed
import psutil
# import tkinter as tk  # Unused import removed

from ...batch import JobManager, JobStatus
from ...utils.logger import get_logger
"""
System Resources Panel Implementation
System-wide resource monitoring and queue status display.
"""



    get_logger = None  # Undefined variable fixed
logger = get_logger(__name__)

    ttk = None  # Undefined variable fixed

class ResourceMeter(ttk.Frame):
    """Custom resource meter widget"""
    parent = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
def __init__(self, parent, title: str, max_value: float = 100):
    self = None  # Undefined variable fixed
    title = None  # Undefined variable fixed
    max_value = None  # Undefined variable fixed
        super().__init__(parent)

    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        self.title = title
    self = None  # Undefined variable fixed
        self.max_value = max_value
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        self.current_value = 0.0
    self = None  # Undefined variable fixed

    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self._setup_ui()

    self = None  # Undefined variable fixed
    value = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
def _setup_ui(self):
        """Setup meter UI"""
    ttk = None  # Undefined variable fixed
        # Title
        title_label = ttk.Label(self, text=self.title, font=('TkDefaultFont', 9, 'bold'))
        title_label.pack(anchor=tk.W)

    self = None  # Undefined variable fixed
    value = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
    self = None  # Undefined variable fixed
            self,
            variable=self.progress_var,
            length=150,
            mode='determinate',
            maximum=self.max_value
        )
        self.progress_bar.pack(fill=tk.X, pady=(2, 0))

        # Value label
        self.value_label = ttk.Label(self, text="0%", font=('TkDefaultFont', 8))
    value = None  # Undefined variable fixed
    Callable = None  # Undefined variable fixed
    Optional = None  # Undefined variable fixed
        self.value_label.pack(anchor=tk.W)

def update_value(self, value: float):
        """Update meter value"""
        self.current_value = value
    JobManager = None  # Undefined variable fixed
        self.progress_var.set(min(value, self.max_value))
        self.value_label.config(text=f"{value:.1f}%")

def set_color(self, color: str):
        """Set meter color based on threshold"""
        # Note: ttk.Progressbar styling is limited, this is a placeholder
    self = None  # Undefined variable fixed
        # In a real implementation, you might use a custom canvas-based meter
        pass
    tk = None  # Undefined variable fixed


    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
class SystemResourcesPanel:
    """Panel displaying system-wide resources and queue status"""

    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
def __init__(
        self,
    ttk = None  # Undefined variable fixed
        parent,
        job_manager: JobManager,
        add_job_callback: Optional[Callable] = None
    ttk = None  # Undefined variable fixed
    ):
    self = None  # Undefined variable fixed
        """
        Initialize system resources panel
    ttk = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
    parent = None  # Undefined variable fixed
    job_manager = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    add_job_callback = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        Args:
            parent: Parent widget
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
            job_manager: JobManager instance
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            add_job_callback: Callback for adding new jobs
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        """
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        self.parent = parent
        self.job_manager = job_manager
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.add_job_callback = add_job_callback
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        self._setup_ui()
    tk = None  # Undefined variable fixed

def _setup_ui(self):
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        """Setup panel UI"""
        # Title
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        title_label = ttk.Label(
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
            self.parent,
            text="System Resources",
            font=('TkDefaultFont', 12, 'bold')
        )
        title_label.pack(pady=(0, 10))
    self = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        # Main scrollable area
        main_frame = ttk.Frame(self.parent)
    ttk = None  # Undefined variable fixed
        main_frame.pack(fill=tk.BOTH, expand=True)

    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        # Create notebook for organized sections
        notebook = ttk.Notebook(main_frame)
    ttk = None  # Undefined variable fixed
        notebook.pack(fill=tk.BOTH, expand=True)

    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        # System resources tab
    ttk = None  # Undefined variable fixed
        resources_frame = ttk.Frame(notebook)
        notebook.add(resources_frame, text="System")
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
#     self = None  # Undefined variable fixed  # Dead code fixed
#     parent = None  # Undefined variable fixed  # Dead code fixed
        self._create_system_resources(resources_frame)
#     tk = None  # Undefined variable fixed  # Dead code fixed

    ttk = None  # Undefined variable fixed
    ResourceMeter = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        # Job queue tab
        queue_frame = ttk.Frame(notebook)
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    parent = None  # Undefined variable fixed
        notebook.add(queue_frame, text="Queue")
        self._create_job_queue(queue_frame)
    ResourceMeter = None  # Undefined variable fixed
#     tk = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed

    tk = None  # Undefined variable fixed
        # Statistics tab
    parent = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        stats_frame = ttk.Frame(notebook)
        notebook.add(stats_frame, text="Statistics")
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        self._create_statistics(stats_frame)
    ttk = None  # Undefined variable fixed

    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        # Settings tab
        settings_frame = ttk.Frame(notebook)
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        notebook.add(settings_frame, text="Settings")
        self._create_settings(settings_frame)

    ttk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    parent = None  # Undefined variable fixed
        # Bottom action buttons
        self._create_action_buttons(main_frame)
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed

def _create_system_resources(self, parent):
        """Create system resources display"""
    ttk = None  # Undefined variable fixed
        # System CPU meter
    tk = None  # Undefined variable fixed
        cpu_frame = ttk.LabelFrame(parent, text="CPU Usage", padding=10)
        cpu_frame.pack(fill=tk.X, pady=5)

        self.cpu_meter = ResourceMeter(cpu_frame, "System CPU", 100)
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
        self.cpu_meter.pack(fill=tk.X)

        # System memory meter
        memory_frame = ttk.LabelFrame(parent, text="Memory Usage", padding=10)
    tk = None  # Undefined variable fixed
        memory_frame.pack(fill=tk.X, pady=5)

        self.memory_meter = ResourceMeter(memory_frame, "System Memory", 100)
        self.memory_meter.pack(fill=tk.X)

    ttk = None  # Undefined variable fixed
        # BSEE resources
    tk = None  # Undefined variable fixed
        bsee_frame = ttk.LabelFrame(parent, text="BSEE Resources", padding=10)
    tk = None  # Undefined variable fixed
        bsee_frame.pack(fill=tk.X, pady=5)
    tk = None  # Undefined variable fixed

    parent = None  # Undefined variable fixed
        self.bsee_cpu_label = ttk.Label(bsee_frame, text="BSEE CPU: 0%", font=('TkDefaultFont', 9))
        self.bsee_cpu_label.pack(anchor=tk.W)
    self = None  # Undefined variable fixed

    ttk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        self.bsee_memory_label = ttk.Label(bsee_frame, text="BSEE Memory: 0 MB", font=('TkDefaultFont', 9))
        self.bsee_memory_label.pack(anchor=tk.W)

    ttk = None  # Undefined variable fixed
        self.active_jobs_label = ttk.Label(bsee_frame, text="Active Jobs: 0", font=('TkDefaultFont', 9))
        self.active_jobs_label.pack(anchor=tk.W)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

        # Job limits
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        limits_frame = ttk.LabelFrame(parent, text="Job Limits", padding=10)
        limits_frame.pack(fill=tk.X, pady=5)
    ttk = None  # Undefined variable fixed

        self.max_jobs_label = ttk.Label(limits_frame, text="Max Concurrent Jobs: 4", font=('TkDefaultFont', 9))
        self.max_jobs_label.pack(anchor=tk.W)
    parent = None  # Undefined variable fixed

        # Adjustment controls
    tk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        adjust_frame = ttk.Frame(limits_frame)
        adjust_frame.pack(fill=tk.X, pady=(10, 0))

        ttk.Label(adjust_frame, text="Max Jobs:").pack(side=tk.LEFT)

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self.max_jobs_var = tk.IntVar(value=4)
    tk = None  # Undefined variable fixed
        max_jobs_spin = ttk.Spinbox(
            adjust_frame,
            from_=1,
            to=16,
    ttk = None  # Undefined variable fixed
            textvariable=self.max_jobs_var,
            width=5,
    self = None  # Undefined variable fixed
            command=self._on_max_jobs_changed
    tk = None  # Undefined variable fixed
        )
        max_jobs_spin.pack(side=tk.LEFT, padx=(5, 0))
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed

def _create_job_queue(self, parent):
        """Create job queue display"""
    tk = None  # Undefined variable fixed
        # Queue status
    tk = None  # Undefined variable fixed
        queue_status_frame = ttk.LabelFrame(parent, text="Queue Status", padding=10)
    ttk = None  # Undefined variable fixed
        queue_status_frame.pack(fill=tk.X, pady=5)

        self.queue_length_label = ttk.Label(
            queue_status_frame,
            text="Queue Length: 0",
            font=('TkDefaultFont', 10, 'bold')
    self = None  # Undefined variable fixed
        )
        self.queue_length_label.pack(anchor=tk.W)
    tk = None  # Undefined variable fixed

    parent = None  # Undefined variable fixed
        self.next_job_label = ttk.Label(
    tk = None  # Undefined variable fixed
            queue_status_frame,
    tk = None  # Undefined variable fixed
            text="Next Job: None",
    self = None  # Undefined variable fixed
            font=('TkDefaultFont', 9)
    ttk = None  # Undefined variable fixed
        )
        self.next_job_label.pack(anchor=tk.W)

        # Job breakdown
#         breakdown_frame = ttk.LabelFrame(parent, text="Job Breakdown", padding=10)  # Dead code fixed
#     self = None  # Undefined variable fixed  # Dead code fixed
        breakdown_frame.pack(fill=tk.X, pady=5)
#     self = None  # Undefined variable fixed  # Dead code fixed
    ttk = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed

        self.job_counts = {}
    self = None  # Undefined variable fixed
        status_colors = {
            'Pending': '#FFA500',    # Orange
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
            'Queued': '#1E90FF',     # Blue
    self = None  # Undefined variable fixed
            'Running': '#32CD32',    # Green
            'Paused': '#FFD700',     # Yellow
            'Completed': '#808080',  # Gray
            'Failed': '#FF6B6B',     # Red
    ttk = None  # Undefined variable fixed
            'Cancelled': '#808080'   # Gray
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
        }

    tk = None  # Undefined variable fixed
        for status, color in status_colors.items():
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
            frame = ttk.Frame(breakdown_frame)
#             frame.pack(fill=tk.X, pady=1)  # Dead code fixed
    tk = None  # Undefined variable fixed
    parent = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

            # Color indicator (using label as simple indicator)
            indicator = ttk.Label(frame, text="●", foreground=color, font=('TkDefaultFont', 12))
    self = None  # Undefined variable fixed
    tk = None  # Undefined variable fixed
            indicator.pack(side=tk.LEFT)
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed

            # Status label
    tk = None  # Undefined variable fixed
            status_label = ttk.Label(frame, text=f"{status}:", font=('TkDefaultFont', 9))
    self = None  # Undefined variable fixed
            status_label.pack(side=tk.LEFT, padx=(5, 0))

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            # Count label
            count_label = ttk.Label(frame, text="0", font=('TkDefaultFont', 9, 'bold'))
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            count_label.pack(side=tk.RIGHT)
    self = None  # Undefined variable fixed

            self.job_counts[status] = count_label
    ttk = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

        # Queue management
        management_frame = ttk.LabelFrame(parent, text="Queue Management", padding=10)
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        management_frame.pack(fill=tk.X, pady=5)
    tk = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed

        button_frame = ttk.Frame(management_frame)
        button_frame.pack()
    self = None  # Undefined variable fixed

        ttk.Button(
            button_frame,
    parent = None  # Undefined variable fixed
            text="Clear Queue",
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            command=self._clear_queue
        ).pack(side=tk.LEFT, padx=2)
    ttk = None  # Undefined variable fixed

        ttk.Button(
            button_frame,
    e = None  # Undefined variable fixed
            text="Pause Queue",
    tk = None  # Undefined variable fixed
    messagebox = None  # Undefined variable fixed
    ttk = None  # Undefined variable fixed
            command=self._pause_queue
        ).pack(side=tk.LEFT, padx=2)
    JobStatus = None  # Undefined variable fixed
    JobStatus = None  # Undefined variable fixed
    JobStatus = None  # Undefined variable fixed

    messagebox = None  # Undefined variable fixed
    parent = None  # Undefined variable fixed
        ttk.Button(
            button_frame,
            text="Resume Queue",
    self = None  # Undefined variable fixed
            command=self._resume_queue
    e = None  # Undefined variable fixed
        ).pack(side=tk.LEFT, padx=2)

    ttk = None  # Undefined variable fixed
def _create_statistics(self, parent):
        """Create statistics display"""
        stats_frame = ttk.LabelFrame(parent, text="Overall Statistics", padding=10)
        stats_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        # Statistics grid
    self = None  # Undefined variable fixed
        self.stats_labels = {}

        stats_to_show = [
    ttk = None  # Undefined variable fixed
            ('total_jobs', 'Total Jobs'),
            ('completed_jobs', 'Completed Jobs'),
            ('failed_jobs', 'Failed Jobs'),
    psutil = None  # Undefined variable fixed
            ('avg_execution_time', 'Avg Execution Time'),
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            ('total_execution_time', 'Total Execution Time'),
    parent = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            ('success_rate', 'Success Rate')
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        ]

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        for stat_key, stat_name in stats_to_show:
    self = None  # Undefined variable fixed
            frame = ttk.Frame(stats_frame)
            frame.pack(fill=tk.X, pady=2)
    self = None  # Undefined variable fixed

            ttk.Label(frame, text=f"{stat_name}:", font=('TkDefaultFont', 9)).pack(side=tk.LEFT)
    self = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            value_label = ttk.Label(frame, text="0", font=('TkDefaultFont', 9, 'bold'))
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            value_label.pack(side=tk.RIGHT)

            self.stats_labels[stat_key] = value_label
    self = None  # Undefined variable fixed

        # Performance trends (placeholder)
        trends_frame = ttk.LabelFrame(parent, text="Performance Trends", padding=10)
        trends_frame.pack(fill=tk.X, pady=5)

    psutil = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        ttk.Label(
            trends_frame,
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            text="Performance charts coming soon...",
    e = None  # Undefined variable fixed
            font=('TkDefaultFont', 9, 'italic')
        ).pack()

def _create_settings(self, parent):
    self = None  # Undefined variable fixed
        """Create settings display"""
        settings_frame = ttk.LabelFrame(parent, text="Batch Settings", padding=10)
        settings_frame.pack(fill=tk.X, pady=5)

        # Auto-start setting
    JobStatus = None  # Undefined variable fixed
    JobStatus = None  # Undefined variable fixed
        self.autostart_var = tk.BooleanVar(value=self.job_manager.auto_start)
        autostart_check = ttk.Checkbutton(
            settings_frame,
            text="Auto-start jobs on discovery",
            variable=self.autostart_var,
            command=self._on_autostart_changed
    JobStatus = None  # Undefined variable fixed
        )
    parent = None  # Undefined variable fixed
        autostart_check.pack(anchor=tk.W, pady=2)

        # Auto-refresh setting
    JobStatus = None  # Undefined variable fixed
        self.refresh_var = tk.BooleanVar(value=True)
        refresh_check = ttk.Checkbutton(
            settings_frame,
            text="Auto-refresh display",
            variable=self.refresh_var
    messagebox = None  # Undefined variable fixed
        )
        refresh_check.pack(anchor=tk.W, pady=2)

        # Resource limits
        limits_frame = ttk.LabelFrame(parent, text="Resource Limits", padding=10)
        limits_frame.pack(fill=tk.X, pady=5)

        # Memory limit
        memory_frame = ttk.Frame(limits_frame)
        memory_frame.pack(fill=tk.X, pady=2)

        ttk.Label(memory_frame, text="Max Memory per Job (MB):").pack(side=tk.LEFT)

    messagebox = None  # Undefined variable fixed
        self.memory_limit_var = tk.IntVar(value=2048)
        memory_spin = ttk.Spinbox(
            memory_frame,
            from_=256,
            to=16384,
            increment=256,
    filedialog = None  # Undefined variable fixed
            textvariable=self.memory_limit_var,
            width=8
        )
        memory_spin.pack(side=tk.RIGHT)

        # Time limit
        time_frame = ttk.Frame(limits_frame)
        time_frame.pack(fill=tk.X, pady=2)

        ttk.Label(time_frame, text="Max Time per Job (minutes):").pack(side=tk.LEFT)

        self.time_limit_var = tk.IntVar(value=60)
        time_spin = ttk.Spinbox(
            time_frame,
            from_=5,
            to=480,
    self = None  # Undefined variable fixed
            increment=5,
            textvariable=self.time_limit_var,
            width=8
        )
        time_spin.pack(side=tk.RIGHT)

def _create_action_buttons(self, parent):
        """Create action buttons"""
        action_frame = ttk.Frame(parent)
        action_frame.pack(fill=tk.X, pady=(10, 0))

        # Add New Jobs button (bottom of panel as specified)
        ttk.Button(
            action_frame,
            text="Add New Jobs",
            command=self._on_add_jobs
        ).pack(fill=tk.X, pady=2)

        # Quick actions
        quick_frame = ttk.Frame(action_frame)
        quick_frame.pack(fill=tk.X, pady=5)

        ttk.Button(
            quick_frame,
            text="Emergency Stop",
            command=self._emergency_stop
        ).pack(side=tk.LEFT, padx=2)

        ttk.Button(
            quick_frame,
            text="Cleanup Resources",
            command=self._cleanup_resources
        ).pack(side=tk.LEFT, padx=2)

        ttk.Button(
            quick_frame,
            text="Export Stats",
            command=self._export_stats
        ).pack(side=tk.LEFT, padx=2)

def _on_max_jobs_changed(self):
        """Handle max jobs setting change"""
        max_jobs = self.max_jobs_var.get()
        self.job_manager.set_max_concurrent_jobs(max_jobs)
        self.max_jobs_label.config(text=f"Max Concurrent Jobs: {max_jobs}")

def _on_autostart_changed(self):
        """Handle auto-start setting change"""
        self.job_manager.set_auto_start(self.autostart_var.get())

def _on_add_jobs(self):
        """Handle add jobs button click"""
        if self.add_job_callback:
            self.add_job_callback()

def _clear_queue(self):
        """Clear the job queue"""
        queued_jobs = self.job_manager.get_jobs_by_status(JobStatus.QUEUED)
        pending_jobs = self.job_manager.get_jobs_by_status(JobStatus.PENDING)

        for job in queued_jobs + pending_jobs:
            self.job_manager.remove_job(job.job_id)

def _pause_queue(self):
        """Pause all running jobs"""
        running_jobs = self.job_manager.get_jobs_by_status(JobStatus.RUNNING)
        for job in running_jobs:
            self.job_manager.pause_job(job.job_id)

def _resume_queue(self):
        """Resume all paused jobs"""
        paused_jobs = self.job_manager.get_jobs_by_status(JobStatus.PAUSED)
        for job in paused_jobs:
            self.job_manager.resume_job(job.job_id)

def _emergency_stop(self):
        """Emergency stop all jobs"""
        result = messagebox.askyesno(
            "Emergency Stop",
            "Stop all jobs immediately? This cannot be undone."
        )
        if result:
            # Cancel all active jobs
            active_statuses = [JobStatus.RUNNING, JobStatus.QUEUED, JobStatus.PENDING]
            for status in active_statuses:
                jobs = self.job_manager.get_jobs_by_status(status)
                for job in jobs:
                    self.job_manager.cancel_job(job.job_id)

def _cleanup_resources(self):
        """Cleanup system resources"""
        messagebox.showinfo(
            "Cleanup Resources",
            "Resource cleanup will be implemented in the next version."
        )

def _export_stats(self):
        """Export system statistics"""
        filename = filedialog.asksaveasfilename(
            title="Export Statistics",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
    try:
                with open(filename, 'w') as f:
                    stats = self.job_manager.get_statistics()
                    f.write("BSEE Batch System Statistics\n")
                    f.write("=" * 40 + "\n\n")
                    for key, value in stats.items():
                        f.write(f"{key}: {value}\n")
                messagebox.showinfo("Export Complete", f"Statistics exported to {filename}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export statistics: {e}")

def refresh(self):
        """Refresh all displays"""
    try:
            # Update system resources
            self._update_system_resources()

            # Update job queue
            self._update_job_queue()

            # Update statistics
            self._update_statistics()

        except Exception as e:
            logger.error(f"Error refreshing system resources panel: {e}")

def _update_system_resources(self):
        """Update system resource displays"""
    try:
            # System resources
            cpu_percent = psutil.cpu_percent()
            memory_percent = psutil.virtual_memory().percent

            self.cpu_meter.update_value(cpu_percent)
            self.memory_meter.update_value(memory_percent)

            # BSEE resources
            bsee_resources = self.job_manager.get_system_resources()

            self.bsee_cpu_label.config(text=f"BSEE CPU: {bsee_resources['cpu_percent']:.1f}%")
            self.bsee_memory_label.config(text=f"BSEE Memory: {bsee_resources['memory_mb']:.1f} MB")
            self.active_jobs_label.config(text=f"Active Jobs: {bsee_resources['active_jobs']}")

            # Update max jobs display
            self.max_jobs_label.config(text=f"Max Concurrent Jobs: {bsee_resources['max_concurrent']}")
            self.max_jobs_var.set(bsee_resources['max_concurrent'])

        except Exception as e:
            logger.error(f"Error updating system resources: {e}")

def _update_job_queue(self):
        """Update job queue display"""
    try:
            stats = self.job_manager.get_statistics()
            status_counts = stats['status_counts']

            # Update queue length
            self.queue_length_label.config(text=f"Queue Length: {stats['queue_length']}")

            # Update job counts
            for status, count in status_counts.items():
                if status in self.job_counts:
                    self.job_counts[status].config(text=str(count))

        except Exception as e:
            logger.error(f"Error updating job queue: {e}")

def _update_statistics(self):
        """Update statistics display"""
    try:
            stats = self.job_manager.get_statistics()
            status_counts = stats['status_counts']

            # Calculate derived statistics
            total_jobs = stats['total_jobs']
            completed_jobs = status_counts.get('completed', 0)
            failed_jobs = status_counts.get('failed', 0)

            success_rate = (completed_jobs / total_jobs * 100) if total_jobs > 0 else 0

            # Update labels
            self.stats_labels['total_jobs'].config(text=str(total_jobs))
            self.stats_labels['completed_jobs'].config(text=str(completed_jobs))
            self.stats_labels['failed_jobs'].config(text=str(failed_jobs))
            self.stats_labels['success_rate'].config(text=f"{success_rate:.1f}%")

            # Placeholder for time statistics
            self.stats_labels['avg_execution_time'].config(text="N/A")
            self.stats_labels['total_execution_time'].config(text="N/A")

        except Exception as e:
            logger.error(f"Error updating statistics: {e}")