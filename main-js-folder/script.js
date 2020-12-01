function classes(){
    
    class Employee{
        constuctor(name, email, salary){
            this.name = name;
            this.email = email;
            this.salary = salary;
        }
        
        getData(){
            return (`Name: ${this.name}, Email: ${this.email}, Salary: $ ${this.salary}`)
        }

    }
    let emp1 = new Employee('sam', 'iaegia@gmail.com', 250000);
    console.log(emp1.getData());
}


function plotData(){
    function getData(){
        return Math.random();
    }

    Plotly.plot('chart',[{
        y:[getData()],
        type: 'line'   
    }])

    var cnt = 0;

    setInterval(function(){
        Plotly.extendTraces('chart', {y:[[getData()]]}, [0]);
        cnt++;
        if(cnt > 500){
            Plotly.relayout('chart', {
                xaxis:{
                    range:[cnt-500,cnt]
                }
            });
        }
    },20)
}



function todolist(){
    function first(){
        window.open("todolist.html")
    }
    function submit(){
        var userinput = document.getElementById('myInput').value;
        console.log(userinput);
    }
    return{first, submit};    
}

function dbtest(){
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "localhost",
    user: "yourusername",
    password: "yourpassword"
    });

    con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    });
}

function getbg(){
    var url = document.body.style.backgroundImage;
    console.log(url);
}

function pagerank(){
    var ia = 1;
    var ib = 1;
    var ic = 1;
    var id = 1;
    var ta = 2;
    var tb = 1;
    var tc = 1;
    
    var ap = [1];
    var bp = [1];
    var cp = [1];
    var dp = [1];
    
    function calc(iv, con){
        return ((iv * 0.85) / con)
    }

    for (var i; i < 10;i++){
        var av = [];
        var bv = [];
        var cv = [];
        var dv = [];
        av.append(calc(ic, tc));
        bv.append(calc(ia, ta));

        cv.append(calc(ia, ta));
        cv.append(calc(ib, tb));
        cv.append(calc(idd, td));

        ia = sum(av) + 0.15;
        ib = sum(bv) + 0.15;
        ic = sum(cv) + 0.15;
        id = sum(dv) + 0.15;

        ap.append(ia);
        bp.append(ib);
        cp.append(ic);
        dp.append(id);
    }

    console.log(ia,ib,ic,id)

    Plotly.plot('chart',[{
        y:ap,
        type: 'line'   
    }])
}