from src.logger import logging
from src.exception import CustomException
from src.utils import load_object
from dataclasses import dataclass
import os 
import pandas as pd

class predict:
    def __init__(self):
        self.model_path=os.path.join("artifect","model.pkl")
        self.precoeser_path=os.path.join("artifect","process.pkl")

    def model_predtion(self,feature):
        model=load_object(self.model_path)
        precoeser=load_object(self.precoeser_path)

        SS_feaure=precoeser.transform(feature)
        predict=model.predict(feature)
        return predict



class Custom_data:
    def __init__(self, mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,
    worst_concave_points, worst_symmetry,worst_fractal_dimension):
        self.mean_radius=float(mean_radius)
        self.mean_texture=float(mean_texture)
        self.mean_perimeter=float(mean_perimeter)
        self.mean_area=float(mean_area)
        self.mean_smoothness=float(mean_smoothness)
        self.mean_compactness=float(mean_compactness)
        self.mean_concavity=float(mean_concavity)
        self.mean_concave_points=float(mean_concave_points)
        self.mean_symmetry=float(mean_symmetry)
        self.mean_fractal_dimension=float(mean_fractal_dimension)
        self.radius_error=float(radius_error)
        self.texture_error=float(texture_error)
        self.perimeter_error=float(perimeter_error)
        self.area_error=float(area_error)
        self.smoothness_error=float(smoothness_error)
        self.compactness_error=float(compactness_error)
        self.concavity_error=float(concavity_error)
        self.concave_points_error=float(concave_points_error)
        self.symmetry_error=float(symmetry_error)
        self.fractal_dimension_error=float(fractal_dimension_error)
        self.worst_radius=float(worst_radius)
        self.worst_texture=float(worst_texture)
        self.worst_perimeter=float(worst_perimeter)
        self.worst_area=float(worst_area)
        self.worst_smoothness=float(worst_smoothness)
        self.worst_compactness=float(worst_compactness)
        self.worst_concavity=float(worst_concavity)
        self.worst_concave_points=float(worst_concave_points)
        self.worst_symmetry=float(worst_symmetry)
        self.worst_fractal_dimension=float(worst_fractal_dimension)

    def export_as_data_frame(self):
        dic={
            "mean radius":[self.mean_radius],
            "mean texture":[self.mean_texture],
            "mean perimeter":[self.mean_perimeter],
            "mean area":[self.mean_area],
            "mean smoothness":[self.mean_smoothness],
            "mean compactness":[self.mean_compactness],
            "mean concavity":[self.mean_concavity],
            "mean concave points":[self.mean_concave_points],
            "mean symmetry":[self.mean_symmetry],
            "mean fractal dimension":[self.mean_fractal_dimension],
            "radius error":[self.radius_error],
            "texture error":[self.texture_error],
            "perimeter error":[self.perimeter_error],
            "area error":[self.area_error],
            "smoothness error":[self.smoothness_error],
            "compactness error":[self.compactness_error],
            "concavity error":[self.concavity_error],
            "concave points error":[self.concave_points_error],
            "symmetry error":[self.symmetry_error],
            "fractal dimension error":[self.fractal_dimension_error],
            "worst radius":[self.worst_radius],
            "worst texture":[self.worst_texture],
            "worst perimeter":[self.worst_perimeter],
            "worst area":[self.worst_area],
            "worst smoothness":[self.worst_smoothness],
            "worst compactness":[self.worst_compactness],
            "worst concavity":[self.worst_concavity],
            "worst concave points":[self.worst_concave_points],
            "worst symmetry":[self.worst_symmetry],
            "worst fractal dimension":[self.worst_fractal_dimension]

        }
        data=pd.DataFrame(dic)
        return data

# cd=Custom_data(17.99,10.38,122.8,1001.0,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019.0,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189)
# df=cd.export_as_data_frame()
# print(df)
# pred=predict()
# print(pred.model_predtion(df))

    






