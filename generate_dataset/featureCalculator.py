import csv
import statistics
import os

rowToWrite = []

# view = "0"
Ax = []
Ay = []
Az = []
AMag = []
AMagXY = []
AMagXZ = []
AMagYZ = []
ARoll = []
APitch = []
Gx = []
Gy = []
Gz = []
GMag = []
GMagXY = []
GMagXZ = []
GMagYZ = []
GRoll = []
GPitch = []
Mx = []
My = []
Mz = []
MaMag = []
MaMagXY = []
MaMagXZ = []
MaMagYZ = []
MaRoll = []
MaPitch = []
Ox = []
Oy = []
Oz = []
OMag = []
OMagXY = []
OMagXZ = []
OMagYZ = []
ORoll = []
OPitch = []
Grx = []
Gry = []
Grz = []
GrMag = []
GrMagXY = []
GrMagXZ = []
GrMagYZ = []
GrRoll = []
GrPitch = []
Pre = []


def appendValues(row):
    Ax.append(float(row[0]))
    Ay.append(float(row[1]))
    Az.append(float(row[2]))
    AMag.append(float(row[3]))
    AMagXY.append(float(row[4]))
    AMagXZ.append(float(row[5]))
    AMagYZ.append(float(row[6]))
    ARoll.append(float(row[7]))
    APitch.append(float(row[8]))
    Gx.append(float(row[9]))
    Gy.append(float(row[10]))
    Gz.append(float(row[11]))
    GMag.append(float(row[12]))
    GMagXY.append(float(row[13]))
    GMagXZ.append(float(row[14]))
    GMagYZ.append(float(row[15]))
    GRoll.append(float(row[16]))
    GPitch.append(float(row[17]))
    Mx.append(float(row[18]))
    My.append(float(row[19]))
    Mz.append(float(row[20]))
    MaMag.append(float(row[21]))
    MaMagXY.append(float(row[22]))
    MaMagXZ.append(float(row[23]))
    MaMagYZ.append(float(row[24]))
    MaRoll.append(float(row[25]))
    MaPitch.append(float(row[26]))
    Ox.append(float(row[27]))
    Oy.append(float(row[28]))
    Oz.append(float(row[29]))
    OMag.append(float(row[30]))
    OMagXY.append(float(row[31]))
    OMagXZ.append(float(row[32]))
    OMagYZ.append(float(row[33]))
    ORoll.append(float(row[34]))
    OPitch.append(float(row[35]))
    Grx.append(float(row[36]))
    Gry.append(float(row[37]))
    Grz.append(float(row[38]))
    GrMag.append(float(row[39]))
    GrMagXY.append(float(row[40]))
    GrMagXZ.append(float(row[41]))
    GrMagYZ.append(float(row[42]))
    GrRoll.append(float(row[43]))
    GrPitch.append(float(row[44]))
    Pre.append(float(row[46]))


def featureFunction():
    calcFeature(Ax)
    calcFeature(Ay)
    calcFeature(Az)
    calcFeature(AMag)
    calcFeature(AMagXY)
    calcFeature(AMagXZ)
    calcFeature(AMagYZ)
    calcFeature(ARoll)
    calcFeature(APitch)
    calcFeature(Gx)
    calcFeature(Gy)
    calcFeature(Gz)
    calcFeature(GMag)
    calcFeature(GMagXY)
    calcFeature(GMagXZ)
    calcFeature(GMagYZ)
    calcFeature(GRoll)
    calcFeature(GPitch)
    calcFeature(Mx)
    calcFeature(My)
    calcFeature(Mz)
    calcFeature(MaMag)
    calcFeature(MaMagXY)
    calcFeature(MaMagXZ)
    calcFeature(MaMagYZ)
    calcFeature(MaRoll)
    calcFeature(MaPitch)
    calcFeature(Ox)
    calcFeature(Oy)
    calcFeature(Oz)
    calcFeature(OMag)
    calcFeature(OMagXY)
    calcFeature(OMagXZ)
    calcFeature(OMagYZ)
    calcFeature(ORoll)
    calcFeature(OPitch)
    calcFeature(Grx)
    calcFeature(Gry)
    calcFeature(Grz)
    calcFeature(GrMag)
    calcFeature(GrMagXY)
    calcFeature(GrMagXZ)
    calcFeature(GrMagYZ)
    calcFeature(GrRoll)
    calcFeature(GrPitch)
    calcFeature(Pre)


def clearArray():
    Ax.clear()
    Ay.clear()
    Az.clear()
    AMag.clear()
    AMagXY.clear()
    AMagXZ.clear()
    AMagYZ.clear()
    ARoll.clear()
    APitch.clear()
    Gx.clear()
    Gy.clear()
    Gz.clear()
    GMag.clear()
    GMagXY.clear()
    GMagXZ.clear()
    GMagYZ.clear()
    GRoll.clear()
    GPitch.clear()
    Mx.clear()
    My.clear()
    Mz.clear()
    MaMag.clear()
    MaMagXY.clear()
    MaMagXZ.clear()
    MaMagYZ.clear()
    MaRoll.clear()
    MaPitch.clear()
    Ox.clear()
    Oy.clear()
    Oz.clear()
    OMag.clear()
    OMagXY.clear()
    OMagXZ.clear()
    OMagYZ.clear()
    ORoll.clear()
    OPitch.clear()
    Grx.clear()
    Gry.clear()
    Grz.clear()
    GrMag.clear()
    GrMagXY.clear()
    GrMagXZ.clear()
    GrMagYZ.clear()
    GrRoll.clear()
    GrPitch.clear()
    Pre.clear()
    rowToWrite.clear()


def calcFeature(sensorValues):
    if len(sensorValues) < 2:
        sensorValues.append(sensorValues[0])
    mean = statistics.mean(sensorValues)
    median = statistics.median(sensorValues)
    stdev = statistics.stdev(sensorValues)
    variance = statistics.variance(sensorValues)
    maxVal = max(sensorValues)
    minVal = min(sensorValues)

    rowToWrite.append(mean)
    rowToWrite.append(median)
    rowToWrite.append(stdev)
    rowToWrite.append(variance)
    rowToWrite.append(maxVal)
    rowToWrite.append(minVal)


def createFileFeature(f):
    csvStart = open(f, 'r')
    filename = os.path.basename(csvStart.name)
    # filenameSplitted = filename.split("-")
    linesReader = len(list(csvStart)) - 2  # ritorna il numero di righe del reader (tolgo header e start da 0)
    # print("num row", linesReader)
    with open(path + filename) as csv_file:
        with open('C:\\Users\\giuli\\Desktop\\prove\\features\\' + 'feature-' + filename, 'w',
                  newline='') as dest:
            csv_reader = csv.reader(csv_file, delimiter=',')
            oldCSVHeader = next(csv_reader)  # restituisce l'header del precedente file

            # accellerometro = A, giroscopio = G, magnetometro = Ma, orientamento = O, gravitazione = Gr
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
                      oldCSVHeader[45], oldCSVHeader[47], oldCSVHeader[48], oldCSVHeader[49], oldCSVHeader[50]]

            writer = csv.writer(dest)
            writer.writerow(header)  # scrivo l'header

            view = "0"

            lastIndex = None

            # index sarà l'indice della prima nuova lettera
            for index, row in enumerate(csv_reader):

                if index == 0:
                    lastIndex = 0

                    appendValues(row)
                    view = row[45]

                elif row[45] == view:
                    lastIndex += 1

                    appendValues(row)

                    if lastIndex == linesReader:

                        featureFunction()

                        rowToWrite.append(view)
                        rowToWrite.append(oldCSVHeader[47])
                        rowToWrite.append(oldCSVHeader[48])
                        rowToWrite.append(oldCSVHeader[49])

                        if row[45] != '-1':
                            writer.writerow(rowToWrite)

                        clearArray()

                elif row[45] != view:  # controllare se sono all'ultima riga prima di questo

                    lastIndex += 1

                    featureFunction()

                    rowToWrite.append(view)
                    rowToWrite.append(oldCSVHeader[47])
                    rowToWrite.append(oldCSVHeader[48])
                    rowToWrite.append(oldCSVHeader[49])

                    if row[45] == '-1':
                        writer.writerow(rowToWrite)

                    clearArray()

                    appendValues(row)
                    view = row[45]

            dest.close()


path = "C:\\Users\\giuli\\Desktop\\prove\\newColumns\\"
files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))

print("files", len(files))

for f in files:
    createFileFeature(f)
    # print(os.path.basename(f))