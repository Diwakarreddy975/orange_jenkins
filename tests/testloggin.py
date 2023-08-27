import inspect
import logging

class logs:
    import logging

    def loggingDemo(self):
        logger_name=inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # Check if there are no handlers attached
        if not logger.handlers:
            file_handler = logging.FileHandler(f"{logger_name}.log")
            formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.INFO)

        return logger

    # Example usage




