import numpy as np
import pandas as pd

colunas = [f"hora_{i+1}" for i in range(10)]

regioes = ["us-east-1", "us-west-2", "eu-central-1", "sa-east-1"]

df = pd.DataFrame(index=regioes, columns=colunas)

print(df)