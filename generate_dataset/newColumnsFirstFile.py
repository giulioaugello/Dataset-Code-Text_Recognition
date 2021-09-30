import csv
import math
import numpy as np
import os


def calcMagnitude(sensorAxes):
    xyz = [float(sensorAxes[0]), float(sensorAxes[1]), float(sensorAxes[2])]
    xy = [float(sensorAxes[0]), float(sensorAxes[1])]
    xz = [float(sensorAxes[0]), float(sensorAxes[2])]
    yx = [float(sensorAxes[1]), float(sensorAxes[2])]
    magXYZ = np.linalg.norm(xyz)
    magXY = np.linalg.norm(xy)
    magXZ = np.linalg.norm(xz)
    magYZ = np.linalg.norm(yx)
    dataRows = [magXYZ, magXY, magXZ, magYZ]
    return dataRows


def calcRoll(sensorAxes):
    return math.atan2(float(sensorAxes[1]), float(sensorAxes[2]))


def calcPitch(sensorAxes):
    return math.atan2(-float(sensorAxes[0]), math.sqrt(pow(float(sensorAxes[1]), 2) + pow(float(sensorAxes[2]), 2)))


def calcAngleDegrees(x):
    return x * 180 / math.pi


def createFile(f):
    csvStart = open(f, 'r')
    filename = os.path.basename(csvStart.name)
    filenameSplitted = filename.split("-")
    with open(path + filename) as csv_file:
        with open('C:\\Users\\giuli\\Desktop\\ds Left\\newColumns\\' + 'new-' + filename, 'w', newline='') as dest:
            csv_reader = csv.reader(csv_file, delimiter=',')
            oldCSVHeader = next(csv_reader)  # return the header of the previous file

            # accellerometro = Acc, giroscopio = Gy, magnetometro = Ma, orientamento = Or, gravitazione = Gr
            header = [oldCSVHeader[1], oldCSVHeader[2], oldCSVHeader[3], "AccMag", "AccMagXY", "AccMagXZ", "AccMagYZ",
                      "AccRoll", "AccPitch",
                      oldCSVHeader[4], oldCSVHeader[5], oldCSVHeader[6], "GyMag", "GyMagXY", "GyMagXZ", "GyMagYZ",
                      "GyRoll", "GyPitch",
                      oldCSVHeader[7], oldCSVHeader[8], oldCSVHeader[9], "MaMag", "MaMagXY", "MaMagXZ", "MaMagYZ",
                      "MaRoll", "MaPitch",
                      oldCSVHeader[10], oldCSVHeader[11], oldCSVHeader[12], "OrMag", "OrMagXY", "OrMagXZ", "OrMagYZ",
                      "OrRoll", "OrPitch",
                      oldCSVHeader[13], oldCSVHeader[14], oldCSVHeader[15], "GrMag", "GrMagXY", "GrMagXZ", "GrMagYZ",
                      "GrRoll", "GrPitch",
                      oldCSVHeader[16], oldCSVHeader[17], oldCSVHeader[18], oldCSVHeader[19], filenameSplitted[1],
                      oldCSVHeader[20]]  # 51

            writer = csv.writer(dest)
            writer.writerow(header)  # write header

            line_count = 1

            for row in csv_reader:
                if line_count == 0:

                    line_count += 1

                else:

                    # axes of each sensors
                    accAxes = [row[1], row[2], row[3]]
                    gyAxes = [row[4], row[5], row[6]]
                    maAxes = [row[7], row[8], row[9]]
                    orAxes = [row[10], row[11], row[12]]
                    grAxes = [row[13], row[14], row[15]]

                    # roll e pitch in gradianti
                    data = [row[1], row[2], row[3], calcMagnitude(accAxes)[0], calcMagnitude(accAxes)[1],
                            calcMagnitude(accAxes)[2], calcMagnitude(accAxes)[3], calcRoll(accAxes),
                            calcPitch(accAxes),
                            row[4], row[5], row[6], calcMagnitude(gyAxes)[0], calcMagnitude(gyAxes)[1],
                            calcMagnitude(gyAxes)[2], calcMagnitude(gyAxes)[3], calcRoll(gyAxes),
                            calcPitch(gyAxes),
                            row[7], row[8], row[9], calcMagnitude(maAxes)[0], calcMagnitude(maAxes)[1],
                            calcMagnitude(maAxes)[2], calcMagnitude(maAxes)[3], calcRoll(maAxes),
                            calcPitch(maAxes),
                            row[10], row[11], row[12], calcMagnitude(orAxes)[0], calcMagnitude(orAxes)[1],
                            calcMagnitude(orAxes)[2], calcMagnitude(orAxes)[3], calcRoll(orAxes),
                            calcPitch(orAxes),
                            row[13], row[14], row[15], calcMagnitude(grAxes)[0], calcMagnitude(grAxes)[1],
                            calcMagnitude(grAxes)[2], calcMagnitude(grAxes)[3], calcRoll(grAxes),
                            calcPitch(grAxes), row[16], row[17]]

                    """
                    # roll e pitch in gradi
                    data = [row[1], row[2], row[3], calcMagnitude(accAxes)[0], calcMagnitude(accAxes)[1],
                            calcMagnitude(accAxes)[2], calcMagnitude(accAxes)[3], calcAngleDegrees(calcRoll(accAxes)),
                            calcAngleDegrees(calcPitch(accAxes)),
                            row[4], row[5], row[6], calcMagnitude(gyAxes)[0], calcMagnitude(gyAxes)[1],
                            calcMagnitude(gyAxes)[2], calcMagnitude(gyAxes)[3], calcAngleDegrees(calcRoll(gyAxes)),
                            calcAngleDegrees(calcPitch(gyAxes)),
                            row[7], row[8], row[9], calcMagnitude(maAxes)[0], calcMagnitude(maAxes)[1],
                            calcMagnitude(maAxes)[2], calcMagnitude(maAxes)[3], calcAngleDegrees(calcRoll(maAxes)),
                            calcAngleDegrees(calcPitch(maAxes)),
                            row[10], row[11], row[12], calcMagnitude(orAxes)[0], calcMagnitude(orAxes)[1],
                            calcMagnitude(orAxes)[2], calcMagnitude(orAxes)[3], calcAngleDegrees(calcRoll(orAxes)),
                            calcAngleDegrees(calcPitch(orAxes)),
                            row[13], row[14], row[15], calcMagnitude(grAxes)[0], calcMagnitude(grAxes)[1],
                            calcMagnitude(grAxes)[2], calcMagnitude(grAxes)[3], calcAngleDegrees(calcRoll(grAxes)),
                            calcAngleDegrees(calcPitch(grAxes)), row[16], row[17]]
                    """

                    writer.writerow(data)

                    line_count += 1

            dest.close()


path = "C:\\Users\\giuli\\Desktop\\ds Left\\raw\\"
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))

print("files", len(files))

for f in files:
    createFile(f)
    # print(os.path.basename(f))
