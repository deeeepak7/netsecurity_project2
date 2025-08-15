from dataclasses import dataclass

@dataclass
class dataingestionArtifact:
    train_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:

    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str   
    drift_report:str

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str
    transformed_test_file_path:str
    transformed_train_file_path:str   

@dataclass
class classficationmetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float


@dataclass
class ModelTrainingArtifact:
    trained_model_file_path:str
    trained_metric_artifact:classficationmetricArtifact
    test_metric_artifact:classficationmetricArtifact
    