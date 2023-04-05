import logging

from celery.bin.control import inspect
from celery.result import AsyncResult
from django.middleware.common import CommonMiddleware
from django.core.cache import cache

LOG = logging.getLogger(__name__)


class RequestLoggingMiddleware(CommonMiddleware):
    def process_request(self, request):
        LOG.info(f'Received request from {request.META["REMOTE_ADDR"]}')
        LOG.info(f'Request method: {request.method}')
        LOG.info(f'Request path: {request.path}')
        LOG.info(f'Request body: {request.body}')
        LOG.info(f'Request headers: {request.headers}')
        LOG.info(f'Request query parameters: {request.GET}')


class CeleryUsageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the Celery worker usage
        worker_inspector = inspect()
        worker_stats = worker_inspector.stats()
        if worker_stats:
            LOG.info(f'Celery worker usage: {worker_stats}')

        # Log the Celery queue usage
        queue_inspector = inspect()
        queue_stats = queue_inspector.active_queues()
        if queue_stats:
            LOG.info(f'Celery queue usage: {queue_stats}')

        response = self.get_response(request)
        return response


class CeleryTaskLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before the view is called, check if there is a currently executing Celery task
        # stored in cache
        task_id = cache.get('current_task')
        if task_id:
            # If there is a task, log the task id and queue
            task = AsyncResult(task_id)
            logger = logging.getLogger(__name__)
            logger.info(f'Executing Celery task {task_id} on queue {task.backend}')

        response = self.get_response(request)

        # After the view is called, clear the stored task id from cache
        cache.delete('current_task')

        return response


from django.conf import settings
from django.utils import timezone
import logging

class CeleryUsageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Get current number of workers and tasks in the queue
        workers = settings.CELERY_WORKER_POOL.num_workers()
        tasks_in_queue = settings.CELERY_WORKER_POOL.tasks_pending()

        # Log the worker and queue usage
        logger = logging.getLogger(__name__)
        logger.info(f'Celery worker usage: {workers} workers at {timezone.now()}')
        logger.info(f'Tasks in queue: {tasks_in_queue} at {timezone.now()}')

        return response
