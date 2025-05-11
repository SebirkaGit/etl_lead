from extract import *
from transform import *
from load import *
import logging

log("ETL Job Started")
log("Extactphase Started")
extracted_data = extract()
log("Exract Phase Ended")

log("Transform Job Started")
transformed_data = transform( extracted_data)
log("transform Job Ended")

log("Load Job Started")
load(targetfile, transformed_data)
log("Load Job Ended")

log("ETL Job Ended")

