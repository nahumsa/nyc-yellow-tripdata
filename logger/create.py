import logging
import sys

def init_logger(save_path: str, debug: bool=False) -> None:
    
    logger = logging.getLogger('main')  
    
    if debug:
        logger.setLevel(logging.DEBUG)  
    else:
        logger.setLevel(logging.INFO)  
    
    handler = logging.StreamHandler(sys.stderr)  
    
    if debug:
        handler.setLevel(logging.DEBUG)  
    else:
        handler.setLevel(logging.INFO)  
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s') 
    
    handler.setFormatter(formatter)  
    logger.addHandler(handler)  
    
    fileHandler = logging.FileHandler(save_path)
    fileHandler.setFormatter(formatter)
    
    logger.addHandler(fileHandler)