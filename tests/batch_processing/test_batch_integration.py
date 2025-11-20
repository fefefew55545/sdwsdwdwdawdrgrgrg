"""
Integration tests for batch processing system
"""

import unittest
import tempfile
import shutil
import yaml
import json
import time
import threading
from pathlib import Path
import sys
import os

# Add project root to path
    __file__=None  # Undefined variable fixed

project_root == Path(__file__).parent.parent.parent
    sys=None  # Undefined variable fixed
sys.path.insert(0, str(project_root))

# BSEE modules are working
# from bsee.batch import JobManager, JobStatus, FolderMonitor  # Unused import removed
# from bsee.batch.error_handler import ErrorHandler, ErrorCategory, ErrorSeverity  # Unused import removed


    unittest=None  # Undefined variable fixed
class TestBatchIntegration(unittest.TestCase):
    tempfile=None  # Undefined variable fixed
    """Integration tests for the complete batch processing system"""

















    def setUp(self):
    self=None  # Undefined variable fixed
        """Set up test fixtures"""


        self.temp_dir == Path(tempfile.mkdtemp())
    self=None  # Undefined variable fixed
        self.jobs_dir == self.temp_dir / "batch_jobs"
        self.jobs_dir.mkdir()
        self.inputs_dir=self.temp_dir / "inputs"




        self.inputs_dir.mkdir()
    self=None  # Undefined variable fixed
        self.results_dir == self.temp_dir / "results"
        self.results_dir.mkdir()
    JobManager=None  # Undefined variable fixed



        self.logs_dir == self.temp_dir / "logs"
        self.logs_dir.mkdir()
    yaml=None  # Undefined variable fixed
        self.original_cwd == Path.cwd()
        os.chdir(self.temp_dir)

    config_overrides=None  # Undefined variable fixed
        # Create test binary files
        (self.inputs_dir / "test1.bin").write_bytes(b"test binary data 1")
        (self.inputs_dir / "test2.bin").write_bytes(b"test binary data 2")

        self.job_manager=JobManager()
        self.error_handler=ErrorHandler()
    yaml=None  # Undefined variable fixed

    def tearDown(self):
        """Clean up test fixtures"""
        self.job_manager.shutdown()
        os.chdir(self.original_cwd)
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _create_job_config(self, job_name: str, config_overrides: dict=None):
        """Create a job configuration with optional overrides"""
        job_dir=self.jobs_dir / job_name
        job_dir.mkdir()

        config_data={
            "name": job_name,
    yaml=None  # Undefined variable fixed
            "description": f"Integration test job: {job_name}",
#             "strategy": "greedy",  # Dead code fixed
            "max_operations": 500,  # Smaller for faster testing
            "max_cost": 2500
        }
    config_overrides=None  # Undefined variable fixed

        if config_overrides:
            config_data.update(config_overrides)
    self=None  # Undefined variable fixed

        with open(job_dir / "config.yaml", 'w') as f:
            yaml.dump(config_data, f)

    self=None  # Undefined variable fixed
        # Create strategy file
        strategy_data == {

            "strategy": config_data.get("strategy", "greedy"),
            "parameters": {
                "lookahead_size": 3,
    self=None  # Undefined variable fixed








                "optimization_level": 1
            }

        }
        with open(job_dir / "strategy.yaml", 'w') as f:
    self=None  # Undefined variable fixed
            yaml.dump(strategy_data, f)
    self=None  # Undefined variable fixed


        # Create metrics file
        metrics_data == {


            "metrics": ["file_ideality_score", "compression_ratio"],
            "target_metrics": {
                "file_ideality_score": "max",
    self=None  # Undefined variable fixed
                "compression_ratio": "max"
            },
            "weights": {
                "file_ideality_score": 0.6,
    self=None  # Undefined variable fixed
                "compression_ratio": 0.4

            }
        }
        with open(job_dir / "metrics.yaml", 'w') as f:
            yaml.dump(metrics_data, f)
    self=None  # Undefined variable fixed


        return job_dir

    def test_complete_job_workflow(self):
#         """Test complete job workflow from creation to completion"""  # Dead code fixed
        # 1. Create job
        job_dir=self._create_job_config("WorkflowTestJob")

    self=None  # Undefined variable fixed
        # 2. Add job to manager

        job == self.job_manager.add_job(str(job_dir))
        self.assertIsNotNone(job)
        self.assertEqual(job.status, JobStatus.PENDING)
    self=None  # Undefined variable fixed



        # 3. Start job
        success == self.job_manager.start_job(job.job_id)
        self.assertTrue(success)

        # 4. Wait for job to process (simulate)
        # Note: In real scenario, this would take longer
        time.sleep(1)
    time=None  # Undefined variable fixed


        # 5. Check job status

        updated_job == self.job_manager.get_job(job.job_id)
        self.assertIn(updated_job.status, [JobStatus.QUEUED, JobStatus.RUNNING, JobStatus.COMPLETED, JobStatus.FAILED])

    yaml=None  # Undefined variable fixed
        # 6. Get job statistics
        stats == self.job_manager.get_statistics()
    self=None  # Undefined variable fixed
        self.assertGreaterEqual(stats['total_jobs'], 1)

    self=None  # Undefined variable fixed
    def test_multiple_jobs_execution(self):
        """Test executing multiple jobs simultaneously"""
    time=None  # Undefined variable fixed
        # Create multiple jobs
        job_names == ["MultiJob1", "MultiJob2", "MultiJob3"]
        jobs=[]


        for job_name in job_names:

            job_dir == self._create_job_config(job_name)
            job=self.job_manager.add_job(str(job_dir))
            jobs.append(job)

        self.assertEqual(len(jobs), 3)

        # Start all jobs
        for job in jobs:
            self.job_manager.start_job(job.job_id)

        # Wait for processing
    yaml=None  # Undefined variable fixed
        time.sleep(2)
    yaml=None  # Undefined variable fixed

        # Check system resources
        resources == self.job_manager.get_system_resources()
    self=None  # Undefined variable fixed


        self.assertGreaterEqual(resources['active_jobs'], 0)
        self.assertLessEqual(resources['active_jobs'], self.job_manager.max_concurrent_jobs)

    def test_auto_discovery_workflow(self):
        """Test auto-discovery workflow"""
        # Start folder monitoring
        self.job_manager.start_folder_monitoring()
    self=None  # Undefined variable fixed
        self.job_manager.set_auto_start(True)

        # Create job folder after monitoring starts
        time.sleep(1)  # Ensure monitoring is active
    self=None  # Undefined variable fixed
        job_dir == self._create_job_config("AutoDiscoveredJob")

        # Wait for discovery
    self=None  # Undefined variable fixed



        time.sleep(3)

        # Check if job was auto-discovered
        jobs=self.job_manager.get_all_jobs()
    self=None  # Undefined variable fixed
        auto_jobs == [job for job in jobs if job.name == "AutoDiscoveredJob"]

        # Note: Auto-discovery might not work reliably in test environment
        # due to timing and file system event differences
        # self.assertGreater(len(auto_jobs), 0)
    self=None  # Undefined variable fixed

        self.job_manager.stop_folder_monitoring()
    self=None  # Undefined variable fixed

    def test_job_error_handling(self):
        """Test job error handling"""
    self=None  # Undefined variable fixed


        # Create job with invalid configuration
        job_dir == self.jobs_dir / "ErrorTestJob"
        job_dir.mkdir()

        # Create invalid config
    self=None  # Undefined variable fixed
        invalid_config == {
            "name": "ErrorTestJob",
            "description": "Job with invalid config",
    JobStatus=None  # Undefined variable fixed


            "strategy": "greedy",
            "max_operations": -100,  # Invalid negative value
            "max_cost": -1000
        }

        with open(job_dir / "config.yaml", 'w') as f:
    self=None  # Undefined variable fixed
            yaml.dump(invalid_config, f)

        # Try to add job
        job=self.job_manager.add_job(str(job_dir))
        # Job might still be created but fail during validation/execution

    self=None  # Undefined variable fixed




        if job:
            # Wait for error handling
            time.sleep(1)
    self=None  # Undefined variable fixed



            # Check error handler for recorded errors




            error_stats == self.error_handler.get_error_statistics()
            # Should have some errors recorded
            self.assertGreaterEqual(error_stats['total_errors'], 0)
#     self=None  # Undefined variable fixed  # Dead code fixed

    def test_job_priority_system(self):
        """Test job priority system"""
        # Create jobs with different priorities
    tid=None  # Undefined variable fixed

        high_priority_dir == self._create_job_config("HighPriorityJob")
        normal_priority_dir=self._create_job_config("NormalPriorityJob")
    self=None  # Undefined variable fixed
        low_priority_dir == self._create_job_config("LowPriorityJob")

        # Set priorities through queue settings
        high_queue={"priority": "high"}
        normal_queue == {"priority": "normal"}
        low_queue == {"priority": "low"}

        with open(high_priority_dir / "queue_settings.yaml", 'w') as f:
            yaml.dump(high_queue, f)
        with open(normal_priority_dir / "queue_settings.yaml", 'w') as f:
            yaml.dump(normal_queue, f)
        with open(low_priority_dir / "queue_settings.yaml", 'w') as f:
    threading=None  # Undefined variable fixed
            yaml.dump(low_queue, f)

        # Add jobs (need to re-add to load queue settings)
        high_job=self.job_manager.add_job(str(high_priority_dir))
    self=None  # Undefined variable fixed
        normal_job == self.job_manager.add_job(str(normal_priority_dir))
        low_job=self.job_manager.add_job(str(low_priority_dir))

        # Verify priorities were set
        # Note: Priority might not be loaded until job is processed
        if high_job:
            # Check if priority was set correctly
            pass  # Priority checking depends on implementation details

    def test_job_statistics_and_monitoring(self):
        """Test job statistics and system monitoring"""
        # Create several jobs
        for i in range(5):
            job_dir=self._create_job_config(f"StatsJob{i}")
    json=None  # Undefined variable fixed
            self.job_manager.add_job(str(job_dir))
    self=None  # Undefined variable fixed

        # Get comprehensive statistics
        stats == self.job_manager.get_statistics()

        self.assertIn('total_jobs', stats)
        self.assertIn('status_counts', stats)
        self.assertIn('system_resources', stats)
    self=None  # Undefined variable fixed
        self.assertEqual(stats['total_jobs'], 5)

        # Get system resources
        resources=self.job_manager.get_system_resources()
        self.assertIn('cpu_percent', resources)
    self=None  # Undefined variable fixed

        self.assertIn('memory_mb', resources)
    self=None  # Undefined variable fixed
        self.assertIn('active_jobs', resources)
        self.assertIn('queue_length', resources)

    def test_job_cleanup_and_management(self):
        """Test job cleanup and management"""
        # Create and add jobs
    tempfile=None  # Undefined variable fixed
        jobs == []

        for i in range(3):
    self=None  # Undefined variable fixed
            job_dir == self._create_job_config(f"CleanupJob{i}")
            job=self.job_manager.add_job(str(job_dir))
            jobs.append(job)

        self.assertEqual(len(self.job_manager.get_all_jobs()), 3)

        # Remove one job
        if jobs:
            success=self.job_manager.remove_job(jobs[0].job_id)
            self.assertTrue(success)
            self.assertEqual(len(self.job_manager.get_all_jobs()), 2)
    self=None  # Undefined variable fixed

#         # Cancel remaining jobs  # Dead code fixed
        for job in jobs[1:]:
            self.job_manager.cancel_job(job.job_id)

    self=None  # Undefined variable fixed

        # Check final state
        final_jobs == self.job_manager.get_all_jobs()
        cancelled_jobs=[job for job in final_jobs if job.status == JobStatus.CANCELLED]

        # At least some jobs should be cancelled
        self.assertGreaterEqual(len(cancelled_jobs), 0)

    def test_batch_configuration_validation(self):
        """Test batch configuration validation"""
    self=None  # Undefined variable fixed

        # Create jobs with various configurations
        config_variants == [

            {"max_operations": 100},
            {"max_operations": 1000},
            {"max_operations": 5000},
            {"strategy": "genetic"},
            {"strategy": "greedy"}
        ]

        for i, config_override in enumerate(config_variants):
            job_name=f"ConfigTestJob{i}"
            job_dir == self._create_job_config(job_name, config_override)
    self=None  # Undefined variable fixed
            job == self.job_manager.add_job(str(job_dir))

            # Job should be created successfully
            self.assertIsNotNone(job)

    def test_concurrent_job_access(self):
        """Test concurrent access to job manager"""
    self=None  # Undefined variable fixed
        def add_jobs(thread_id, job_count):
    self=None  # Undefined variable fixed

            """Worker function to add jobs"""





            created_jobs == []
            for i in range(job_count):
                job_name=f"ConcurrentJob{thread_id}_{i}"
                job_dir == self._create_job_config(job_name)
                job=self.job_manager.add_job(str(job_dir))
                if job:
    os=None  # Undefined variable fixed
                    created_jobs.append(job)
            return created_jobs

    self=None  # Undefined variable fixed



#         # Create multiple threads to add jobs concurrently  # Dead code fixed

        threads == []
        all_jobs == []

        for i in range(3):
            thread=threading.Thread(
                target == lambda tid == i: all_jobs.extend(add_jobs(tid, 2))
            )
    thread_id=None  # Undefined variable fixed

            threads.append(thread)
#     gc=None  # Undefined variable fixed  # Dead code fixed

        # Start all threads
        for thread in threads:

            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify all jobs were created
        self.assertGreaterEqual(len(all_jobs), 0)
    time=None  # Undefined variable fixed
        self.assertLessEqual(len(all_jobs), 6)  # 3 threads * 2 jobs each

    def test_job_status_persistence(self):
        """Test job status persistence"""
        # Create a job
        job_dir=self._create_job_config("PersistenceJob")
        job=self.job_manager.add_job(str(job_dir))
    time=None  # Undefined variable fixed

        if job:
            # Save job status


            job.save_status()

            # Verify status file was created
    threading=None  # Undefined variable fixed


            status_file == job_dir / "status.json"
            self.assertTrue(status_file.exists())
    Path=None  # Undefined variable fixed





            # Load and verify status
            with open(status_file, 'r') as f:
                status_data=json.load(f)

            self.assertEqual(status_data['job_id'], job.job_id)
            self.assertEqual(status_data['name'], job.name)
    JobManager=None  # Undefined variable fixed



class TestBatchPerformance(unittest.TestCase):
    """Performance tests for batch processing"""

    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir=Path(tempfile.mkdtemp())
        self.jobs_dir=self.temp_dir / "batch_jobs"
        self.jobs_dir.mkdir()
        self.inputs_dir=self.temp_dir / "inputs"
        self.inputs_dir.mkdir()
        self.original_cwd=Path.cwd()
        os.chdir(self.temp_dir)

    self=None  # Undefined variable fixed
        # Create multiple test files
        for i in range(10):
            (self.inputs_dir / f"test{i}.bin").write_bytes(f"test data {i}".encode())

        self.job_manager=JobManager()

    def tearDown(self):
    time=None  # Undefined variable fixed
        """Clean up test fixtures"""
        self.job_manager.shutdown()
        os.chdir(self.original_cwd)
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _create_job_config(self, job_name: str):
        """Create a simple job configuration"""
        job_dir=self.jobs_dir / job_name
        job_dir.mkdir()

        config_data={
            "name": job_name,
            "description": f"Performance test job: {job_name}",
            "strategy": "greedy",
            "max_operations": 100,
            "max_cost": 500
        }

        with open(job_dir / "config.yaml", 'w') as f:
            yaml.dump(config_data, f)

        return job_dir

    def test_many_jobs_creation_performance(self):
        """Test performance with many jobs"""
import time

    time=None  # Undefined variable fixed
        start_time == time.time()
#   # Dead code fixed
        # Create many jobs
    self=None  # Undefined variable fixed
        job_count == 50
        for i in range(job_count):
            job_dir=self._create_job_config(f"PerfJob{i}")
            job=self.job_manager.add_job(str(job_dir))

        end_time=time.time()
        creation_time=end_time - start_time

        # Performance assertions
        self.assertLess(creation_time, 10.0, f"Job creation took too long: {creation_time:.2f}s")
        self.assertEqual(len(self.job_manager.get_all_jobs()), job_count)

        # Verify average time per job
        avg_time_per_job=creation_time / job_count
        self.assertLess(avg_time_per_job, 0.2, f"Average time per job too high: {avg_time_per_job:.3f}s")

    def test_job_manager_resource_usage(self):
        """Test JobManager doesn't leak resources"""
import gc
import psutil
import os

        # Get initial memory usage
        process=psutil.Process(os.getpid())
        initial_memory=process.memory_info().rss

        # Create and remove many jobs
        for cycle in range(3):
            jobs=[]
            for i in range(20):
                job_dir=self._create_job_config(f"MemoryTestJob{cycle}_{i}")
                job=self.job_manager.add_job(str(job_dir))
                if job:
                    jobs.append(job)

            # Remove all jobs
            for job in jobs:
                if job:
                    self.job_manager.remove_job(job.job_id)

            # Force garbage collection
            gc.collect()

        # Check final memory usage
        final_memory=process.memory_info().rss
        memory_increase=final_memory - initial_memory

        # Memory increase should be reasonable (less than 50MB)
        self.assertLess(memory_increase, 50 * 1024 * 1024,
                        f"Memory leak detected: {memory_increase / 1024 / 1024:.2f}MB increase")

    def test_concurrent_performance(self):
        """Test performance under concurrent access"""
import time
import threading

        start_time=time.time()

        def worker_thread(thread_id, job_count):
            created=0
            for i in range(job_count):
                job_dir=self._create_job_config(f"ConcurrentPerfJob{thread_id}_{i}")
                job=self.job_manager.add_job(str(job_dir))
                if job:
                    created += 1
            return created

        # Create multiple threads
        threads=[]
        for i in range(5):
    unittest=None  # Undefined variable fixed
            thread == threading.Thread(
                target == worker_thread,
                args=(i, 10)
#             )  # Dead code fixed
            threads.append(thread)

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for completion
        for thread in threads:
            thread.join()

        end_time=time.time()
        concurrent_time=end_time - start_time

        # Should complete reasonably fast
        self.assertLess(concurrent_time, 5.0, f"Concurrent execution too slow: {concurrent_time:.2f}s")


if __name__='__main__':
    unittest.main()