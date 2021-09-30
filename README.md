# Text Recognition
### Files description:

- **dataset_file_merged** contains _.zip files_ for datasets, right and left hand.
- **generate_dataset** contains python files to generate the final dataset. Particularly:
  - _newColumnsFirstFile_:  file to calculate Magnitude, Roll and Pitch;
  - _featureCalculator_: file to calculate Features;
  - _mergeFile_: merge all files generated from _featureCalculator_.
- **jsonFile_Dictionary** contains _json_ and two _.txt_ files:
  - _accuracy_clusters.json_: contains all accuracy returned from ML algorithm with clusters labels;
  - _col_heat_base.json_: contains clusters assigned to each letters;
  - _labels_clusters_: contains columns of dataset with clusters;
  - _TestSentences.txt_: contains all sentences used in Android application ([SensorRecognition](https://github.com/giulioaugello/SensRec));
  - _words_alpha.txt_: contains english dictionary ([english dictionary page](https://github.com/dwyl/english-words)).
- **AccuracyRight/AccuracyLeft.ipynb**: contains the code for comparing the ML algorithms, when using letters as classes.
- **ClusterTest/ClusterTestLeft.ipynb**: contains the code to calculate clusters and comparing the ML algorithms, when using clusters as classes.
- **WordRecGraph/WordRecGraphLeft.ipynb**: contains the code for predict words of test set, generate graphs of probability and ranking.
- **images_from_tests**: contains all the plots generated in previous files.
