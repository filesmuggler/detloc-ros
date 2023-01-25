import torch

class ModelWrapper:
    """Class for wrapping the model loading and preparation for inference.
    """
    def __init__(self):
        self.model = None
        
    def load_model(self,path_to_repo:str,model_name:str)->bool:
        """Loading model from Torch Hub

        Args:
            path_to_repo (str): eg. 'ultralytics/yolov5'
            model_name (str):eg. 'yolov5s'

        Returns:
            bool: if the model was correctly loaded
        """
        self.model = torch.hub.load(path_to_repo, model_name, pretrained=True)
        if self.model is not None:
            return True
        else:
            return False

    def get_model(self) -> torch.nn.Module:
        """ Returns ML model

        Returns:
            torch.nn.Module: the model
        """
        return self.model

    def _save_model_from_web(self,path_to_repo: str, model_name) -> bool:
        # TODO: Saving the model from web should be solved with the use
        # of ONNX runtime for handling different models
        pass
        