from app.core.config import settings
import logging

logging.basicConfig(level=settings.LOG_LEVEL)
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logger = logging.getLogger(__name__)
