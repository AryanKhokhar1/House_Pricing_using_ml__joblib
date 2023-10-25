from django.apps import AppConfig
import html
import pathlib
import os

class PricePredictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'price_predict'