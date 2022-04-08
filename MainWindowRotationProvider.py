from qgis.core import QgsVectorLayer

class MainWindowRotationProvider:
    """Reads information from UI of main window and transfers it into processing algorithm."""
    def __init__(self, processingLayer: QgsVectorLayer, processMethod: str, rotationAngle: int = 0, outputName: str = "Rotated points") -> None:
        self.processingLayer: QgsVectorLayer = processingLayer
        self.processMethod: str = processMethod
        self.rotationAngle: int = rotationAngle
        self.outputName: str = outputName