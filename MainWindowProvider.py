class MainWindowProvider:
    """Reads information from UI of main window and transferres it into processing algorithm."""
    def __init__(self, processingLayerName: str, processMethod: str, rotationAngle: int = 0, outputName: str = "Rotated points") -> None:
        self.processingLayerName: str = processingLayerName
        self.processMethod: str = processMethod
        self.rotationAngle: int = rotationAngle
        self.outputName: str = outputName