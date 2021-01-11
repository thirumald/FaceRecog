# ---- coding: utf-8 ----
# ===================================================
# Author: Susanta Biswas
# ===================================================
'''Description: Base class to handle persistent data 
storage'''
# ===================================================
from abc import ABC, abstractclassmethod, abstractmethod

class PersistentStorage(ABC):
    @abstractmethod
    def add_data(self):
        pass

    @abstractmethod
    def get_all_data(self):
        pass 
    