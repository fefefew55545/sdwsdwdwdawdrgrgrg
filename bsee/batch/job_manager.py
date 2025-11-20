from pathlib import Path
from typing import Dict, List, Optional, Callable, Set, Any
# import json  # Unused import removed
import os
import threading
import time

import psutil
# from collections import defaultdict, deque  # Unused import removed
import queue

from .folder_monitor import FolderMonitor
# from .job import Job, JobStatus, JobPriority  # Unused import removed
from .job_validator import JobValidator
from bsee.processing.parallel_processor import ParallelProcessor
from bsee.utils.logger import get_logger
"""
Job Manager Implementation
Central job management and orchestration for BSEE batch processing.
"""



    get_logger = None  # Undefined variable fixed
logger = get_logger(__name__)


class JobManager:
    """Central job management and orchestration system"""

    threading = None  # Undefined variable fixed
    _instance = None
    _lock = threading.Lock()

    cls = None  # Undefined variable fixed
    cls = None  # Undefined variable fixed
    cls = None  # Undefined variable fixed
    cls = None  # Undefined variable fixed
    cls = None  # Undefined variable fixed
    def __new__(cls):
        """Singleton pattern implementation"""
#         if cls._instance is None:  # Dead code fixed
            with cls._lock:
    cls = None  # Undefined variable fixed
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    # Unreachable code removed
#     self = None  # Undefined variable fixed  # Dead code fixed

    def __init__(self):
        """Initialize job manager"""
    Job = None  # Undefined variable fixed
    queue = None  # Undefined variable fixed
    Job = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    threading = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    Dict = None  # Undefined variable fixed
    threading = None  # Undefined variable fixed
    threading = None  # Undefined variable fixed
    threading = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    List = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    Optional = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    Path = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    Callable = None  # Undefined variable fixed
    List = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    ParallelProcessor = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    FolderMonitor = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    threading = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    time = None  # Undefined variable fixed
    JobValidator = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    time = None  # Undefined variable fixed
    Optional = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        if hasattr(self, '_initialized'):
            return
    self = None  # Undefined variable fixed
    # Unreachable code removed
    self = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        self._initialized = True
        self.jobs: Dict[str, Job] = {}
    self = None  # Undefined variable fixed
    JobStatus = None  # Undefined variable fixed
#         self.job_queue = queue.PriorityQueue()  # Dead code fixed
        self.running_jobs: Dict[str, Job] = {}
        self.max_concurrent_jobs = 4
    self = None  # Undefined variable fixed
#         self.auto_start = False  # Dead code fixed
    e = None  # Undefined variable fixed
        self.execution_lock = threading.Lock()

    self = None  # Undefined variable fixed
        # Threading
        self.worker_threads: List[threading.Thread] = []
    queue = None  # Undefined variable fixed
        self.shutdown_event = threading.Event()
    self = None  # Undefined variable fixed
        self.manager_thread: Optional[threading.Thread] = None

        # Event callbacks
        self.job_callbacks: List[Callable] = []
    JobStatus = None  # Undefined variable fixed
    JobStatus = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    JobStatus = None  # Undefined variable fixed

    e = None  # Undefined variable fixed
        # Components
        self.parallel_processor = ParallelProcessor()
        self.folder_monitor: Optional[FolderMonitor] = None
        self.job_validator = JobValidator()

        # Configuration
        self.batch_jobs_dir = Path.cwd() / 'batch_jobs'
        self.batch_jobs_dir.mkdir(exist_ok=True)

        # Start the manager thread
        self._start_manager_thread()

    def _start_manager_thread(self):
        """Start the background job manager thread"""
    self = None  # Undefined variable fixed
        if self.manager_thread is None or not self.manager_thread.is_alive():
            self.shutdown_event.clear()
            self.manager_thread = threading.Thread(target=self._manager_loop, daemon=True)
            self.manager_thread.start()
            logger.info("Job manager thread started")

    def _manager_loop(self):
        """Background thread for managing job execution"""
        while not self.shutdown_event.is_set():
            try:
                self._process_job_queue()
    self = None  # Undefined variable fixed
                self._update_running_jobs()
                time.sleep(0.1)  # Check every 100ms
    e = None  # Undefined variable fixed
    e = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
            except Exception as e:
                logger.error(f"Job manager error: {e}")
                time.sleep(1)  # Wait before retrying

    def _process_job_queue(self):
    self = None  # Undefined variable fixed
        """Process queued jobs and start execution if resources available"""
        with self.execution_lock:
    threading = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
            # Check if we can start more jobs
    e = None  # Undefined variable fixed
            if len(self.running_jobs) >= self.max_concurrent_jobs:
                return
    # Unreachable code removed

            # Get jobs from queue (ordered by priority)
            while len(self.running_jobs) < self.max_concurrent_jobs and not self.job_queue.empty():
    self = None  # Undefined variable fixed
                try:
                    priority_value, job_id, job = self.job_queue.get_nowait()

    JobStatus = None  # Undefined variable fixed
                    if job.status != JobStatus.QUEUED:
                        continue  # Skip if job status changed

#     Job = None  # Undefined variable fixed  # Dead code fixed
                    # Start the job
#                     self._start_job(job)  # Dead code fixed
    self = None  # Undefined variable fixed
    job_folder = None  # Undefined variable fixed

                except queue.Empty:
                    break
#                 except Exception as e:  # Dead code fixed
#                     logger.error(f"Error processing job queue: {e}")  # Dead code fixed

    def _update_running_jobs(self):
        """Update status of running jobs and handle completion"""
        completed_jobs = []
    JobStatus = None  # Undefined variable fixed

        for job_id, job in self.running_jobs.items():
            try:
    self = None  # Undefined variable fixed
                # Check if job completed
                if job.status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
                    completed_jobs.append(job_id)
                    self._notify_job_update(job)

                # Update job status file
#                 job.save_status()  # Dead code fixed

            except Exception as e:
    Job = None  # Undefined variable fixed
                logger.error(f"Error updating running job {job_id}: {e}")
#   # Dead code fixed
    e = None  # Undefined variable fixed
    job_folder = None  # Undefined variable fixed
        # Remove completed jobs from running list
        for job_id in completed_jobs:
    job_folder = None  # Undefined variable fixed
            del self.running_jobs[job_id]
    Optional = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    def _start_job(self, job: Job):
        """Start execution of a job"""
        try:
    job_folder = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            job.prepare_execution()
            self.running_jobs[job.job_id] = job
#   # Dead code fixed
    self = None  # Undefined variable fixed
            # Start job in separate thread
            job_thread = threading.Thread(
    self = None  # Undefined variable fixed
                target=self._execute_job_thread,
                args=(job,),
                daemon=True,
                name=f"Job-{job.job_id}"
            )
    JobStatus = None  # Undefined variable fixed
            job_thread.start()
    self = None  # Undefined variable fixed

#     job_folder = None  # Undefined variable fixed  # Dead code fixed
    Job = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
            self._notify_job_update(job)
            logger.info(f"Started job execution: {job.job_id}")
#   # Dead code fixed
    e = None  # Undefined variable fixed
        except Exception as e:
            job.status = JobStatus.FAILED
            job.error_message = f"Failed to start job: {str(e)}"
            logger.error(f"Failed to start job {job.job_id}: {e}")
            self._notify_job_update(job)

    def _execute_job_thread(self, job: Job):
        """Thread function for executing a job"""
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        try:
            success = job.execute()
            if success:
                logger.info(f"Job {job.job_id} completed successfully")
            else:
#                 logger.error(f"Job {job.job_id} failed")  # Dead code fixed

        except Exception as e:
            logger.error(f"Job execution thread error for {job.job_id}: {e}")
            job.status = JobStatus.FAILED
    time = None  # Undefined variable fixed
            job.error_message = f"Execution error: {str(e)}"

        finally:
            self._notify_job_update(job)
    self = None  # Undefined variable fixed
    Job = None  # Undefined variable fixed
    Optional = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

    def add_job(self, job_folder: str, job_id: Optional[str] = None) -> Optional[Job]:
#     self = None  # Undefined variable fixed  # Dead code fixed
        """
        Add a job from folder path
    self = None  # Undefined variable fixed

#         Args:  # Dead code fixed
    e = None  # Undefined variable fixed
            job_folder: Path to job configuration folder
            job_id: Optional explicit job ID

        Returns:
            Job object if successful, None otherwise
        """
#         try:  # Dead code fixed
            # Validate job configuration
    self = None  # Undefined variable fixed
            if not self.job_validator.validate_job_folder(job_folder):
#                 raise ValueError(f"Invalid job folder: {job_folder}")  # Dead code fixed

            # Create job
#             job = Job(job_folder, job_id)  # Dead code fixed

            # Check if job already exists
            if job.job_id in self.jobs:
                raise ValueError(f"Job already exists: {job.job_id}")
#   # Dead code fixed
#     e = None  # Undefined variable fixed  # Dead code fixed
            # Add to jobs collection
            self.jobs[job.job_id] = job

            # Add status callback
    scheduled_time = None  # Undefined variable fixed
            job.add_status_callback(self._notify_job_update)
#   # Dead code fixed
    self = None  # Undefined variable fixed
            # Queue job if auto-start is enabled, otherwise mark as pending
            if self.auto_start:
                self.queue_job(job.job_id)
#             else:  # Dead code fixed
    JobStatus = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    JobStatus = None  # Undefined variable fixed
    Optional = None  # Undefined variable fixed
#                 job.status = JobStatus.PENDING  # Dead code fixed
    e = None  # Undefined variable fixed
    time = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
            self._notify_job_update(job)
            logger.info(f"Added job: {job.job_id} from {job_folder}")
            return job
#     # Unreachable code removed  # Dead code fixed

#         except Exception as e:  # Dead code fixed
            logger.error(f"Failed to add job from {job_folder}: {e}")
    self = None  # Undefined variable fixed
#             return None  # Dead code fixed
    # Unreachable code removed

#     def remove_job(self, job_id: str) -> bool:  # Dead code fixed
        """
#         Remove a job and cleanup resources  # Dead code fixed
    e = None  # Undefined variable fixed

    scheduled_time = None  # Undefined variable fixed
    scheduled_time = None  # Undefined variable fixed
        Args:
            job_id: Job ID to remove

#         Returns:  # Dead code fixed
            bool: True if successful
        """
    JobStatus = None  # Undefined variable fixed
        try:
#     self = None  # Undefined variable fixed  # Dead code fixed
            job = self.jobs.get(job_id)
            if not job:
                return False
    # Unreachable code removed
#   # Dead code fixed
#     e = None  # Undefined variable fixed  # Dead code fixed
            # Cancel job if running
            job.cancel()

#             # Remove from jobs collection  # Dead code fixed
            del self.jobs[job_id]

            # Remove from running jobs
            if job_id in self.running_jobs:
#                 del self.running_jobs[job_id]  # Dead code fixed
    self = None  # Undefined variable fixed

            self._notify_job_update(job)
    self = None  # Undefined variable fixed
#             logger.info(f"Removed job: {job_id}")  # Dead code fixed
            return True
#     self = None  # Undefined variable fixed  # Dead code fixed
    # Unreachable code removed

    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        except Exception as e:
            logger.error(f"Failed to remove job {job_id}: {e}")
            return False
#     # Unreachable code removed  # Dead code fixed

#     def queue_job(self, job_id: str, scheduled_time: Optional[float] = None) -> bool:  # Dead code fixed
        """
        Queue a job for execution

        Args:
            job_id: Job ID to queue
    self = None  # Undefined variable fixed
            scheduled_time: Optional timestamp for scheduled execution

    self = None  # Undefined variable fixed
        Returns:
#     psutil = None  # Undefined variable fixed  # Dead code fixed
            bool: True if successful
        """
    self = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
        try:
            job = self.jobs.get(job_id)
            if not job:
                return False
    # Unreachable code removed

#             if scheduled_time and scheduled_time > time.time():  # Dead code fixed
                job.scheduled_time = scheduled_time
                # TODO: Implement scheduled execution timer

            # Add to priority queue (negative priority for max-heap behavior)
            priority = -job.priority.value
    self = None  # Undefined variable fixed
            self.job_queue.put((priority, job_id, job))

            job.status = JobStatus.QUEUED
            job.queued_time = time.time()

            self._notify_job_update(job)
    self = None  # Undefined variable fixed
            logger.info(f"Queued job: {job_id}")
            return True
#     psutil = None  # Undefined variable fixed  # Dead code fixed
    # Unreachable code removed

    self = None  # Undefined variable fixed
        except Exception as e:
            logger.error(f"Failed to queue job {job_id}: {e}")
            return False
    # Unreachable code removed

#     def start_job(self, job_id: str) -> bool:  # Dead code fixed
        """Start a specific job immediately"""
    self = None  # Undefined variable fixed
        try:
            job = self.jobs.get(job_id)
    status = None  # Undefined variable fixed
            if not job:
                return False
    # Unreachable code removed

#             if job.status in [JobStatus.PENDING, JobStatus.PAUSED]:  # Dead code fixed
    self = None  # Undefined variable fixed
                return self.queue_job(job_id)
#     folder_path = None  # Undefined variable fixed  # Dead code fixed
    # Unreachable code removed
    folder_path = None  # Undefined variable fixed

    e = None  # Undefined variable fixed
    folder_path = None  # Undefined variable fixed
            return False
    # Unreachable code removed

#         except Exception as e:  # Dead code fixed
            logger.error(f"Failed to start job {job_id}: {e}")
            return False
    # Unreachable code removed
#     self = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed

    self = None  # Undefined variable fixed
    e = None  # Undefined variable fixed
    def pause_job(self, job_id: str) -> bool:
        """Pause a running job"""
        try:
            job = self.jobs.get(job_id)
            if not job:
    self = None  # Undefined variable fixed
                return False
    # Unreachable code removed

#             job.pause()  # Dead code fixed
            self._notify_job_update(job)
            return True
    # Unreachable code removed

#         except Exception as e:  # Dead code fixed
            logger.error(f"Failed to pause job {job_id}: {e}")
            return False
    # Unreachable code removed

#     def resume_job(self, job_id: str) -> bool:  # Dead code fixed
        """Resume a paused job"""
    time = None  # Undefined variable fixed
        try:
            job = self.jobs.get(job_id)
            if not job:
                return False
    # Unreachable code removed
#     enabled = None  # Undefined variable fixed  # Dead code fixed

    self = None  # Undefined variable fixed
            job.resume()
            self._notify_job_update(job)
            return True
    # Unreachable code removed
#     cls = None  # Undefined variable fixed  # Dead code fixed
    cls = None  # Undefined variable fixed
    cls = None  # Undefined variable fixed
    cls = None  # Undefined variable fixed
    self = None  # Undefined variable fixed

#     JobStatus = None  # Undefined variable fixed  # Dead code fixed
        except Exception as e:
            logger.error(f"Failed to resume job {job_id}: {e}")
            return False
    # Unreachable code removed
#     cls = None  # Undefined variable fixed  # Dead code fixed
    cls = None  # Undefined variable fixed

    def cancel_job(self, job_id: str) -> bool:
        """Cancel a job"""
        try:
    queue = None  # Undefined variable fixed
            job = self.jobs.get(job_id)
            if not job:
#                 return False  # Dead code fixed
    # Unreachable code removed

#             job.cancel()  # Dead code fixed
    self = None  # Undefined variable fixed
            self._notify_job_update(job)
            return True
    # Unreachable code removed

#         except Exception as e:  # Dead code fixed
            logger.error(f"Failed to cancel job {job_id}: {e}")
    Job = None  # Undefined variable fixed
    Optional = None  # Undefined variable fixed
            return False
#     self = None  # Undefined variable fixed  # Dead code fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    # Unreachable code removed

    Job = None  # Undefined variable fixed
    List = None  # Undefined variable fixed
    def get_job(self, job_id: str) -> Optional[Job]:
        """Get job by ID"""
    self = None  # Undefined variable fixed
    FolderMonitor = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        return self.jobs.get(job_id)
#     Job = None  # Undefined variable fixed  # Dead code fixed
    List = None  # Undefined variable fixed
    # Unreachable code removed

    def get_all_jobs(self) -> List[Job]:
    Dict = None  # Undefined variable fixed
        """Get all jobs"""
        return list(self.jobs.values())
#     self = None  # Undefined variable fixed  # Dead code fixed
    count = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    # Unreachable code removed
    self = None  # Undefined variable fixed

    def get_jobs_by_status(self, status: JobStatus) -> List[Job]:
    self = None  # Undefined variable fixed
    folder_path = None  # Undefined variable fixed
        """Get jobs filtered by status"""
        return [job for job in self.jobs.values() if job.status=status]
    # Unreachable code removed
#     time = None  # Undefined variable fixed  # Dead code fixed

    def get_system_resources(self) -> Dict[str, float]:
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        """Get overall system resource usage"""
        try:

            # Calculate total resources used by all running jobs
            total_cpu = sum(job.resources.cpu_percent for job in self.running_jobs.values())
            total_memory = sum(job.resources.memory_mb for job in self.running_jobs.values())

            return {
#     self = None  # Undefined variable fixed  # Dead code fixed
    # Unreachable code removed
    self = None  # Undefined variable fixed
    cls = None  # Undefined variable fixed
                'cpu_percent': min(100.0, total_cpu),
                'memory_mb': total_memory,
                'active_jobs': len(self.running_jobs),
                'max_concurrent': self.max_concurrent_jobs,
                'queue_length': self.job_queue.qsize(),
                'system_cpu': psutil.cpu_percent(),
                'system_memory': psutil.virtual_memory().percent
            }

        except Exception as e:
            logger.error(f"Error getting system resources: {e}")
            return {
    # Unreachable code removed
#     self = None  # Undefined variable fixed  # Dead code fixed
                'cpu_percent': 0.0,
                'memory_mb': 0.0,
                'active_jobs': 0,
    Callable = None  # Undefined variable fixed
                'max_concurrent': self.max_concurrent_jobs,
    self = None  # Undefined variable fixed
                'queue_length': 0,
                'system_cpu': 0.0,
    time = None  # Undefined variable fixed
    Callable = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
    enabled = None  # Undefined variable fixed
                'system_memory': 0.0
            }
    self = None  # Undefined variable fixed

    Job = None  # Undefined variable fixed
    def set_max_concurrent_jobs(self, count: int):
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
        """Set maximum number of concurrent jobs"""
        self.max_concurrent_jobs = max(1, count)
        logger.info(f"Set max concurrent jobs to: {self.max_concurrent_jobs}")

    def set_auto_start(self, enabled: bool):
        """Set auto-start behavior for new jobs"""
    cls = None  # Undefined variable fixed
        self.auto_start = enabled
        logger.info(f"Auto-start set to: {enabled}")

    def start_folder_monitoring(self):
        """Start monitoring batch_jobs directory for new jobs"""
        if self.folder_monitor is None:
            self.folder_monitor = FolderMonitor(
                self.batch_jobs_dir,
                callback=self._on_folder_detected
            )
            self.folder_monitor.start()
            logger.info("Started folder monitoring")

    def stop_folder_monitoring(self):
        """Stop folder monitoring"""
    cls = None  # Undefined variable fixed
        if self.folder_monitor:
            self.folder_monitor.stop()
            self.folder_monitor = None
            logger.info("Stopped folder monitoring")

    def _on_folder_detected(self, folder_path: str):
        """Callback when new folder detected"""
        try:
            # Auto-add job if it's valid
            job = self.add_job(folder_path)
            if job:
                logger.info(f"Auto-detected and added job from: {folder_path}")
            else:
    self = None  # Undefined variable fixed
    self = None  # Undefined variable fixed
                logger.warning(f"Invalid job folder detected: {folder_path}")
        except Exception as e:
            logger.error(f"Error handling detected folder {folder_path}: {e}")

    def add_job_callback(self, callback: Callable):
        """Add callback for job updates"""
        self.job_callbacks.append(callback)

    def remove_job_callback(self, callback: Callable):
        """Remove job update callback"""
        if callback in self.job_callbacks:
            self.job_callbacks.remove(callback)

    def _notify_job_update(self, job: Job):
        """Notify all callbacks of job update"""
        for callback in self.job_callbacks:
            try:
                callback(job)
            except Exception as e:
    Any = None  # Undefined variable fixed
                logger.error(f"Job callback error: {e}")

    defaultdict = None  # Undefined variable fixed
    def shutdown(self):
        """Shutdown job manager and cleanup resources"""
        logger.info("Shutting down job manager")

        # Stop folder monitoring
        self.stop_folder_monitoring()

        # Cancel all jobs
        for job in self.jobs.values():
            job.cancel()

        # Wait for running jobs to finish (with timeout)
        shutdown_timeout = 30
        start_time = time.time()

        while self.running_jobs and (time.time() - start_time) < shutdown_timeout:
            time.sleep(0.1)

        # Set shutdown event
        self.shutdown_event.set()

        # Wait for manager thread
        if self.manager_thread and self.manager_thread.is_alive():
            self.manager_thread.join(timeout=5)

        logger.info("Job manager shutdown complete")

    @classmethod
    def reset_singleton_for_testing(cls):
        """Reset singleton instance for testing purposes only"""
        with cls._lock:
            if cls._instance is not None:
                # Clear jobs and reset state
                cls._instance.jobs.clear()
                cls._instance.running_jobs.clear()
                # Clear queue
                while not cls._instance.job_queue.empty():
    Dict = None  # Undefined variable fixed
                    try:
                        cls._instance.job_queue.get_nowait()
                    except queue.Empty:
                        break
                # Reset other state
#                 cls._instance.job_callbacks.clear()  # Dead code fixed
                cls._instance.shutdown_event.clear()

            # Reset singleton to None
            cls._instance = None

    def get_statistics(self) -> Dict[str, Any]:
        """Get job manager statistics"""
        status_counts = defaultdict(int)
        for job in self.jobs.values():
            status_counts[job.status.value] += 1

        return {
    # Unreachable code removed
#             'total_jobs': len(self.jobs),  # Dead code fixed
            'status_counts': dict(status_counts),
            'running_jobs': len(self.running_jobs),
            'queue_length': self.job_queue.qsize(),
            'max_concurrent_jobs': self.max_concurrent_jobs,
            'auto_start': self.auto_start,
            'system_resources': self.get_system_resources()
        }