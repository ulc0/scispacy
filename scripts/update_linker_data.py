# Databricks notebook source
# MAGIC %pip freeze
# MAGIC %pip install -r /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/compute/requirements_scispacy_support.txt
# MAGIC %pip install scipy==1.10.1
# MAGIC %restart_python

# COMMAND ----------


from scispacy.linking_utils import KnowledgeBase
from scispacy.candidate_generation import CandidateGenerator, create_tfidf_ann_index
from scispacy.linking import EntityLinker
from scispacy.umls_utils import UmlsKnowledgeBase
from scispacy.abbreviation import AbbreviationDetector

#import scispacy.linking_utils as linking_utils 
#import scispacy.candidate_generation as candidate_generation
#import scispacy.umls_utils as umls_utils
#import scispacy.linking as linking


# COMMAND ----------

# MAGIC %md
# MAGIC umls download path  
# MAGIC /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/2024AA/META/ 
# MAGIC json path   
# MAGIC /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl/  
# MAGIC * 

# COMMAND ----------

# MAGIC %sh
# MAGIC python3 export_umls_json.py --meta_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/2024AA/META --output_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl/umls_kb.jsonl
# MAGIC #python3 export_umls_json.py --meta_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/rxnorm/rrf/ --output_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl/rxnorm_kb.jsonl

# COMMAND ----------

# MAGIC %md
# MAGIC python3 create_linker.py --kb_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl/umls_kb.jsonl --output_path /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl

# COMMAND ----------

"""
proformaLinkerPaths = {
    ann_index="https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/data/linkers/2023-04-23/umls/nmslib_index.bin",  # noqa
    tfidf_vectorizer="https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/data/linkers/2023-04-23/umls/tfidf_vectorizer.joblib",  # noqa
    tfidf_vectors="https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/data/linkers/2023-04-23/umls/tfidf_vectors_sparse.npz",  # noqa
    concept_aliases_list="https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/data/linkers/2023-04-23/umls/concept_aliases.json",  # noqa
}
"""

# COMMAND ----------

base_dir='/Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/'
out_dir=base_dir+'linker/umls/'

# COMMAND ----------

# https://learn.microsoft.com/en-us/azure/databricks/files/
kb_path=f"{base_dir}jsonl/umls_kb.jsonl"
kb = KnowledgeBase(file_path=kb_path)

# COMMAND ----------

import tempfile, os
from scispacy.candidate_generation import CandidateGenerator, create_tfidf_ann_index, MentionCandidate
import tempfile
 
temp_dir = tempfile.mkdtemp() #.TemporaryDirectory()
print(temp_dir)
# use temp_dir, and when done:
umls_concept_aliases, tfidf_vectorizer, ann_index = create_tfidf_ann_index(temp_dir, kb)
os.environ["TEMP_DIR"]=temp_dir
"""
ls -ll temp_dir 
cd temp_dir
#cp concept_aliases.json /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
#cp tfidf_vectors_sparse.npz /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
#cp tfidf_vectorizer.joblib /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
#cp nmslib_index.bin /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
cp * /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
ls /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
"""

# COMMAND ----------

"""
dbutils.fs.ls(temp_dir)
dbutils.fs.cp(temp_dir+'/concept_aliases.json',out_dir)
dbutils.fs.cp(temp_dir+'/tfidf_vectors_sparse.npz',out_dir )
dbutils.fs.cp(temp_dir+'/tfidf_vectorizer.joblib',out_dir )
dbutils.fs.cp(temp_dir+'/nmslib_index.bin',out_dir )
dbutils.fs.ls(out_dir)
"""


# COMMAND ----------

# MAGIC %sh
# MAGIC ls -ll $TEMP_DIR 
# MAGIC cd $TEMP_DIR
# MAGIC #cp concept_aliases.json /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
# MAGIC #cp tfidf_vectors_sparse.npz /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
# MAGIC #cp tfidf_vectorizer.joblib /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
# MAGIC #cp nmslib_index.bin /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
# MAGIC cp * /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
# MAGIC ls /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/linker/umls/
# MAGIC

# COMMAND ----------

"""
    tfidf_vectorizer_path = f"{out_path}/tfidf_vectorizer.joblib"
    ann_index_path = f"{out_path}/nmslib_index.bin"
    tfidf_vectors_path = f"{out_path}/tfidf_vectors_sparse.npz"
    umls_concept_aliases_path = f"{out_path}/concept_aliases.json"
"""

# COMMAND ----------

# MAGIC %md
# MAGIC cd /tmp/tmpazmsqksw
# MAGIC cp concept_aliases.json /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/
# MAGIC cp tfidf_vectors_sparse.npz /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/
# MAGIC cp tfidf_vectorizer.joblib /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/
# MAGIC cp nmslib_index.bin /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/umls

# COMMAND ----------

from scispacy.candidate_generation import LinkerPaths
UmlsLinkerPaths = LinkerPaths(
    ann_index="nmslib_index.bin",  # noqa
    tfidf_vectorizer="tfidf_vectorizer.joblib",  # noqa
    tfidf_vectors="tfidf_vectors_sparse.npz",  # noqa
    concept_aliases_list="concept_aliases.json",  # noqa
)


# COMMAND ----------

# MAGIC %sh
# MAGIC ls /tmp

# COMMAND ----------

output_path='dbfs:/Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl'
#output_path='abfss://cdh@davsynapseanalyticsdev.dfs.core.windows.net/machinelearning/scispacy/kbs'
#output_path='/dbfs/kb'
#output_path='/Workspace/CDH'
#output_path='/Workspace/Shared/scispacy'
#os.makedirs(output_path, exist_ok=True)
output_path='.'


# COMMAND ----------

import os
from scispacy.candidate_generation import create_tfidf_ann_index

output_path='dbfs:/Volumes/edav_dev_cdh_test/dev_cdh_ml_test/data/jsonl'
#output_path='abfss://cdh@davsynapseanalyticsdev.dfs.core.windows.net/machinelearning/scispacy/kbs'
#output_path='/dbfs/kb'
#output_path='/Workspace/CDH'
#output_path='/Workspace/Shared/scispacy'
#os.makedirs(output_path, exist_ok=True)
output_path='.'

#create_tfidf_ann_index(output_path, kb)
