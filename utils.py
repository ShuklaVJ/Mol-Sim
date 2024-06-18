import numpy as np

def TanimotoSimilarity(fp1, fp2):
    intersection = np.sum(np.minimum(fp1, fp2))
    union = np.sum(np.maximum(fp1, fp2))
    return intersection / float(union)
