from qgis import processing
from qgis.core import QgsProcessingException
import logging
from ..MainWindowRotationProvider import MainWindowRotationProvider

basicConfig = logging.basicConfig(filename = "Turn_plugin.log", filemode = "w", format = '%(asctime)s - %(message)s', datefmt = '%d-%b-%y %H:%M:%S')

class RotationAlgorithm:
    """Implements logic for rotating vector layer."""

    def __init__(self, rotationProvider: MainWindowRotationProvider) -> None:
        self.parameters = rotationProvider

    def findCentroid(self):
        """Implements finding of centroids in the layer."""
        first_object_id = 1

        try:
            centroids_alg = processing.run("native:centroids",
                                        {"INPUT": self.parameters.processingLayer,
                                            "OUTPUT": "memory:"})
            layer = centroids_alg["OUTPUT"]
            point = layer.getGeometry(fid = first_object_id).asPoint()
        except QgsProcessingException:
            logging.exception("QgsProcessingException while finding anchor centroid.")

        return point

    def rotate(self):
        """Rotates vector layer on given angle around anchor point."""
        try:
            return processing.runAndLoadResults("native:rotatefeatures", {"INPUT": self.parameters.processingLayer,
                                                            "ANGLE": self.parameters.rotationAngle,
                                                            "ANCHOR": self.findCentroid(),
                                                            "OUTPUT": self.parameters.outputName})
        except QgsProcessingException:
            logging.exception("QgsProcessingException while rotating features.")
