from networksecurity.entity.artifact_entity import classficationmetricArtifact
from networksecurity.exception.exception import customException
from sklearn.metrics import f1_score,precision_score,recall_score


def get_classification_score(y_true,y_pred)->classficationmetricArtifact:
    try:
        model_f1_score=f1_score(y_true,y_pred)
        model_recall_score = recall_score(y_true,y_pred)
        model_precision_Score=precision_score(y_true,y_pred)

        classification_metric = classficationmetricArtifact(f1_score=model_f1_score,
        precision_score=model_precision_Score,recall_score=model_recall_score)
        return classification_metric
    except Exception as e:
        raise networksecurity(e,sys)
            













