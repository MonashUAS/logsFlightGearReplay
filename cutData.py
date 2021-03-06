
import numpy as np

def getSection(data,field,startTime,endTime):
    # Find times that are within the range
    ind = np.where((data.timeVec>=startTime) & (data.timeVec<=endTime))[0]
    # Get time values
    timeData = data.timeVec[ind]
    # Get field values
    fieldData = []
    for index in ind:
        fieldData.append(data.fields[index][data.headers[field]])
    
    # Convert field data to floats
    fieldData = np.array(fieldData)
    fieldData = fieldData.astype(np.float)
    
    return timeData, fieldData

def addDataToPlot(axes,subplot,timeData,fieldData,yLim=False):
    # Plot it
    subplot.set_xdata(timeData)
    subplot.set_ydata(fieldData)
    # Setting Time limits
    mint = min(timeData)
    maxt = max(timeData)
    if mint != maxt:
        axes.set_xlim(mint,maxt)
    else:
        axes.set_xlim(mint,mint+1)
    # Setting y limits
    if not yLim:
        minf = min(fieldData)
        maxf = max(fieldData)
        if minf != maxf:
            axes.set_ylim(minf,maxf)
        else:
            axes.set_ylim(minf,minf+1)
    else:
        # Set according to data for all time
        axes.set_ylim(yLim[0],yLim[1])

    