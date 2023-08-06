cwlVersion: v1.0
class: CommandLineTool

baseCommand: ["python3", "script.py"]

inputs:
  data_file:
    type: File
    inputBinding:
      prefix: "--data_file"
      position: 1

outputs:
  result:
    type: File
    outputBinding:
      glob: "results.txt"

requirements:
  DockerRequirement:
    dockerPull: "ml_analysis_image"
  InitialWorkDirRequirement:
    listing:
      - class: File
        location: "script.py"
