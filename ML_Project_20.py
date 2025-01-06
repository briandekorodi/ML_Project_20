#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:14:32 2025

@author: bdekorodi
"""

import pandas as pd
import numpy as np

learn_dataset = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/learn_dataset.csv')  
learn_dataset_sport = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/learn_dataset_sport.csv')
learn_dataset_retired_pension = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/learn_dataset_retired_pension.csv')
learn_dataset_retired_jobs = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/learn_dataset_retired_jobs.csv')
learn_dataset_retired_former = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/learn_dataset_retired_former.csv')
learn_dataset_job = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/learn_dataset_job.csv')
learn_dataset_emp_type = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/learn_dataset_emp_type.csv')

test_dataset = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/test_dataset.csv')
test_dataset_sport = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/test_dataset_sport.csv')
test_dataset_retired_pension = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/test_dataset_retired_pension.csv')
test_dataset_retired_jobs = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/test_dataset_retired_jobs.csv')
test_dataset_retired_former = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/test_dataset_retired_former.csv')
test_dataset_job = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/test_dataset_job.csv')
test_dataset_emp_type = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/test_dataset_emp_type.csv')

code_work_desc = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_work_desc.csv')  
code_work_desc_n2 = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_work_desc_n2.csv')
code_work_desc_n1 = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_work_desc_n1.csv')
code_work_desc_map = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_work_desc_map.csv')
code_work_condition = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_work_condition.csv')
code_Type_of_contract = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_Type_of_contract.csv')
code_SPORTS = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_SPORTS.csv')
code_Occupation_42 = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_Occupation_42.csv')
code_JOB_CATEGORY = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_JOB_CATEGORY.csv')
code_household_type = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_household_type.csv')
code_employer_type = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_employer_type.csv')
code_employee_count = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_employee_count.csv')
code_emp_type = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_emp_type.csv')
ode_ECO_SECT = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_ECO_SECT.csv')
code_DEGREE = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_DEGREE.csv')
code_activity_type = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/code_activity_type.csv')

city_adm = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/city_adm.csv')
city_loc = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/city_loc.csv')
city_pop = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/city_pop.csv')
departments = pd.read_csv('/Users/bdekorodi/Desktop/ML_20/project-20-files/departments.csv')
