from qgis import processing
from ..MainWindowRotationProvider import MainWindowRotationProvider


class RotationAlgorithm:
    """Implements logic for rotating vector layer."""

    def __init__(self, rotationProvider: MainWindowRotationProvider) -> None:
        self.parameters = rotationProvider

    def findCentroid(self):
        first_object_id = 1

        centroids_alg = processing.run("native:centroids",
                                       {"INPUT": self.parameters.processingLayer,
                                        "OUTPUT": "memory:"})
        layer = centroids_alg["OUTPUT"]
        point = layer.getGeometry(fid = first_object_id).asPoint()
        return point

    def rotate(self):
        return processing.runAndLoadResults("native:rotatefeatures", {"INPUT": self.parameters.processingLayer,
                                                        "ANGLE": self.parameters.rotationAngle,
                                                        "ANCHOR": self.findCentroid(),
                                                        "OUTPUT": self.parameters.outputName})
