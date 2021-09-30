# Dataset-Code-Text_Recognition

- **dataset_file_merged** contains *.zip files* of datasets, for right and left hand
- **generate_dataset** contains python files to generate the final dataset. Particularly:
  - *newColumnsFirstFile*:  file to calculate Magnitude, Roll and Pitch;
  - *featureCalculator*: file to calculate Features;
  - *mergeFile*: merge all files generated from *featureCalculator*.
