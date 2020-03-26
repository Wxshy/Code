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
    return {

    first(){
        window.open("todolist.html")
    },
    submit(){
        var userinput = document.getElementById('myInput').value;
        console.log(userinput);
    }
    }
}