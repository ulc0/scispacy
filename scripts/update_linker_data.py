# Databricks notebook source
# MAGIC %md
# MAGIC umls download path  
# MAGIC /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/2024AA/META/ 
# MAGIC json path   
# MAGIC /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl/  
# MAGIC * 

# COMMAND ----------

# MAGIC %sh
# MAGIC python3 export_umls_json.py --meta_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/2024AA/META --output_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl/umls_kb.jsonl
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC python3 create_linker.py --kb_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl/umls_kb.jsonl --output_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl

# COMMAND ----------

from scispacy.candidate_generation import create_tfidf_ann_index
from scispacy.linking_utils import KnowledgeBase
kb_path='/Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl/umls_kb.jsonl'
output_path='/dbfs/Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl'

# COMMAND ----------


#os.makedirs(output_path, exist_ok=True)
kb = KnowledgeBase(file_path=kb_path)



# COMMAND ----------

create_tfidf_ann_index(output_path, kb)
