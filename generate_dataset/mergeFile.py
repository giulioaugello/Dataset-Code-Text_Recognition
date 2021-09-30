import csv
import os


def mergeFiles():
    with open('C:\\Users\\giuli\\Desktop\\ds Left\\merged\\' + 'mergedFileLeft.csv', 'w', newline='') as dest:

        header = ["AxMean", "AxMed", "AxStd", "AxVar", "AxMax", "AxMin",
                      "AyMean", "AyMed", "AyStd", "AyVar", "AyMax", "AyMin",
                      "AzMean", "AzMed", "AzStd", "AzVar", "AzMax", "AzMin",
                      "AMagMean", "AMagMed", "AMagStd", "AMagVar", "AMagMax", "AMagMin",
                      "AMagXYMean", "AMagXYMed", "AMagXYStd", "AMagXYVar", "AMagXYMax", "AMagXYMin",
                      "AMagXZMean", "AMagXZMed", "AMagXZStd", "AMagXZVar", "AMagXZMax", "AMagXZMin",
                      "AMagYZMean", "AMagYZMed", "AMagYZStd", "AMagYZVar", "AMagYZMax", "AMagYZMin",
                      "ARollMean", "ARollMed", "ARollStd", "ARollVar", "ARollMax", "ARollMin",
                      "APitchMean", "APitchMed", "APitchStd", "APitchVar", "APitchMax", "APitchMin",
                      "GxMean", "GxMed", "GxStd", "GxVar", "GxMax", "GxMin",
                      "GyMean", "GyMed", "GyStd", "GyVar", "GyMax", "GyMin",
                      "GzMean", "GzMed", "GzStd", "GzVar", "GzMax", "GzMin",
                      "GMagMean", "GMagMed", "GMagStd", "GMagVar", "GMagMax", "GMagMin",
                      "GMagXYMean", "GMagXYMed", "GMagXYStd", "GMagXYVar", "GMagXYMax", "GMagXYMin",
                      "GMagXZMean", "GMagXZMed", "GMagXZStd", "GMagXZVar", "GMagXZMax", "GMagXZMin",
                      "GMagYZMean", "GMagYZMed", "GMagYZStd", "GMagYZVar", "GMagYZMax", "GMagYZMin",
                      "GRollMean", "GRollMed", "GRollStd", "GRollVar", "GRollMax", "GRollMin",
                      "GPitchMean", "GPitchMed", "GPitchStd", "GPitchVar", "GPitchMax", "GPitchMin",
                      "MaxMean", "MaxMed", "MaxStd", "MaxVar", "MaxMax", "MaxMin",
                      "MayMean", "MayMed", "MayStd", "MayVar", "MayMax", "MayMin",
                      "MazMean", "MazMed", "MazStd", "MazVar", "MazMax", "MazMin",
                      "MaMagMean", "MaMagMed", "MaMagStd", "MaMagVar", "MaMagMax", "MaMagMin",
                      "MaMagXYMean", "MaMagXYMed", "MaMagXYStd", "MaMagXYVar", "MaMagXYMax", "MaMagXYMin",
                      "MaMagXZMean", "MaMagXZMed", "MaMagXZStd", "MaMagXZVar", "MaMagXZMax", "MaMagXZMin",
                      "MaMagYZMean", "MaMagYZMed", "MaMagYZStd", "MaMagYZVar", "MaMagYZMax", "MaMagYZMin",
                      "MaRollMean", "MaRollMed", "MaRollStd", "MaRollVar", "MaRollMax", "MaRollMin",
                      "MaPitchMean", "MaPitchMed", "MaPitchStd", "MaPitchVar", "MaPitchMax", "MaPitchMin",
                      "OxMean", "OxMed", "OxStd", "OxVar", "OxMax", "OxMin",
                      "OyMean", "OyMed", "OyStd", "OyVar", "OyMax", "OyMin",
                      "OzMean", "OzMed", "OzStd", "OzVar", "OzMax", "OzMin",
                      "OMagMean", "OMagMed", "OMagStd", "OMagVar", "OMagMax", "OMagMin",
                      "OMagXYMean", "OMagXYMed", "OMagXYStd", "OMagXYVar", "OMagXYMax", "OMagXYMin",
                      "OMagXZMean", "OMagXZMed", "OMagXZStd", "OMagXZVar", "OMagXZMax", "OMagXZMin",
                      "OMagYZMean", "OMagYZMed", "OMagYZStd", "OMagYZVar", "OMagYZMax", "OMagYZMin",
                      "ORollMean", "ORollMed", "ORollStd", "ORollVar", "ORollMax", "ORollMin",
                      "OPitchMean", "OPitchMed", "OPitchStd", "OPitchVar", "OPitchMax", "OPitchMin",
                      "GrxMean", "GrxMed", "GrxStd", "GrxVar", "GrxMax", "GrxMin",
                      "GryMean", "GryMed", "GryStd", "GryVar", "GryMax", "GryMin",
                      "GrzMean", "GrzMed", "GrzStd", "GrzVar", "GrzMax", "GrzMin",
                      "GrMagMean", "GrMagMed", "GrMagStd", "GrMagVar", "GrMagMax", "GrMagMin",
                      "GrMagXYMean", "GrMagXYMed", "GrMagXYStd", "GrMagXYVar", "GrMagXYMax", "GrMagXYMin",
                      "GrMagXZMean", "GrMagXZMed", "GrMagXZStd", "GrMagXZVar", "GrMagXZMax", "GrMagXZMin",
                      "GrMagYZMean", "GrMagYZMed", "GrMagYZStd", "GrMagYZVar", "GrMagYZMax", "GrMagYZMin",
                      "GrRollMean", "GrRollMed", "GrRollStd", "GrRollVar", "GrRollMax", "GrRollMin",
                      "GrPitchMean", "GrPitchMed", "GrPitchStd", "GrPitchVar", "GrPitchMax", "GrPitchMin",
                      "PreMean", "PreMed", "PreStd", "PreVar", "PreMax", "PreMin",
                      "View", "User", "Hand", "Smartphone"]

        writer = csv.writer(dest)
        writer.writerow(header)
        print("files", len(files))
        for f in files:
            csvStart = open(f, 'r')
            # print(os.path.basename(f))
            filename = os.path.basename(csvStart.name)
            with open(path + filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                lineSkip = 0
                for row in csv_reader:
                    if lineSkip == 0:
                        lineSkip += 1
                    else:
                        writer.writerow(row)

        dest.close()


path = "C:\\Users\\giuli\\Desktop\\ds Left\\features\\"
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
mergeFiles()
