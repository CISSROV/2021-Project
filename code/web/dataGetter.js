// This code is for fetching data to be displayed in a table in json
// The json should be a list of lists with two entries, i.e. like a x by 2 array 

var intervalID = 0
var compressed = false;

function getData() {
    xmlhttp = new XMLHttpRequest()
    xmlhttp.onreadystatechange = function() {
        if ( this.readyState == 4 && this.status == 200 ) {
            myObj = JSON.parse(this.responseText)
            txt = '<table id="dataTable">'
            txt += '<tr><th>Time</th><th>Temperature (&deg;C)</th></tr>'
            for (x in myObj.reverse()) 
            {
                txt += '<tr><td>' + myObj[x][0] + '</td><td>' + myObj[x][1] + '</td></tr>'
            }
            document.getElementById('dataTable').innerHTML = txt

            if (compressed) {
                compress()
            }
            document.getElementById('dataError').hidden = true;
        }
        else {
            if (this.readyState == 4) {
                document.getElementById('dataError').hidden = false;
            }
        }
    }
    xmlhttp.open('GET', 'data.json', true)
    xmlhttp.send()
    //console.log('Update!')
}

function stopUpdating() {
    clearInterval( intervalID )
    document.getElementById('live').style['display'] = 'none'
    document.getElementById('stop').hidden = true
    document.getElementById('start').hidden = false
}

function startUpdating() {
    intervalID = setInterval (getData, 10000)
    document.getElementById('live').style['display'] = 'inline'
    document.getElementById('stop').hidden = false
    document.getElementById('start').hidden = true
}

function compress() {
    var elements = document.getElementsByTagName('td')
    for (i = 0; i < elements.length; i++)
    {
        elements[i].setAttribute('class','compressed')
    }
    compressed = true

    document.getElementById('compress').hidden = true
    document.getElementById('decompress').hidden = false
}

function decompress() {
    var elements = document.getElementsByTagName('td')
    for (i = 0; i < elements.length; i++)
    {
        elements[i].setAttribute('class','')
    }
    compressed = false

    document.getElementById('compress').hidden = false
    document.getElementById('decompress').hidden = true
}


getData()
intervalID = setInterval ( getData, 10000 )
