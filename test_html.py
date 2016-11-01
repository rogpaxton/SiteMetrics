# write-html.py

f = open('html_test.html','w')

message = """
    <!DOCTYPE html>
    <html>
    <body>
    <h1> Popup for site location</h1><br>
    <div>
    <img src="small_jpeg.jpg">
    </div>
    </body>
    </html>
    """

#    <img id="RC51" src="/small_jpeg.jpg" alt="RVT" style="width:48px;height:49px;">

f.write(message)
f.close()
