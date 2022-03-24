from math import ceil
from flask import Flask, render_template, request
import catchBias, urlReader, catchCategory
app = Flask(__name__, template_folder='templates', static_folder="static", static_url_path='/static')
SCOREMAP = {
    4: ("extreme", "left"),
    3: ("strong", "left"),
    2: ("moderate", "left"),
    1: ("minimal", "left"),
    0: ("none", "neutral"),
    -1: ("minimal", "right"),
    -2: ("moderate", "right"),
    -3: ("strong", "right"),
    -4: ("extreme", "right")
}
@app.route('/',methods=['GET','POST'])
def mainpage():
    return render_template('index.html')

@app.route('/textsubmit', methods=['POST'])
def textsubmit():
    rawText = request.form['text']
    biasResult = catchBias.getBias(rawText)
    categoryResult = catchCategory.getCategory(rawText)
    results = [["User Input Text",categoryResult]]
    results[0].append(biasResult)
    results[0].extend(SCOREMAP[biasResult])
    votingMap = [biasResult,0,0] if biasResult > 0 else [0,1,0] if biasResult==0 else [0,0,biasResult]
    print(results)
    return render_template('result.html',results=results,votingMap=votingMap, overview=SCOREMAP[biasResult])

@app.route('/urlsubmit', methods=['POST'])
def urlsubmit():
    results = urlReader.analyzerURL(request.form['text'])
    votingSum = 0
    numSum = 0
    votingMap = [0,0,0]
    for index, result in enumerate(results):
        numSum += 1
        if result[2] > 0:
            votingMap[0] += result[2]*0.5
            votingSum += result[2]
        elif result[2] == 0:
            votingMap[1] += 1
            votingSum += result[2]
        else:
            votingMap[2] -= result[2]*0.5
            votingSum += result[2]
        results[index].extend(SCOREMAP[result[2]])
    votingAvg = ceil(votingSum/numSum) if numSum!=0 else 0
    overview = SCOREMAP[votingAvg]
    return render_template('result.html',results=results,votingMap=votingMap, overview=overview)
